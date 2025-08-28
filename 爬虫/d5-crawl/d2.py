import asyncio
import csv
import os
from playwright.async_api import async_playwright
import pandas as pd

CSV_FILE = "mit_admissions_details.csv"

async def fetch_blog_details():
    # 先读取链接 CSV
    df_links = pd.read_csv("blog_links.csv")
    links = df_links["link"].tolist()

    # 读取已抓取数据
    existing_data = {}
    if os.path.exists(CSV_FILE):
        df_existing = pd.read_csv(CSV_FILE)
        for _, row in df_existing.iterrows():
            existing_data[row["URL"]] = row

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for url in links:
            await page.goto(url)
            await page.wait_for_selector(".post-type-post")

            # 标题
            title_el = await page.query_selector(".page-topper__title")
            title = await title_el.inner_text() if title_el else "N/A"

            # 副标题
            subtitle_el = await page.query_selector(".page-topper__sub")
            subtitle = await subtitle_el.inner_text() if subtitle_el else ""

            # 作者
            author_el = await page.query_selector(".page-topper__title__name")
            author = await author_el.inner_text() if author_el else "N/A"

            # 时间
            time_el = await page.query_selector("time")
            time = await time_el.inner_text() if time_el else "N/A"

            # 内容与图片
            content_el = await page.query_selector(".article__body")
            content = ""
            images = []

            if content_el:
                children = await content_el.query_selector_all(":scope > *")
                for child in children:
                    tag_name = await child.evaluate("el => el.tagName")
                    tag_name = tag_name.lower()

                    if tag_name == "p":
                        text = await child.inner_text()
                        if text.strip():
                            content += text.strip() + "!#@p!#@"
                    elif tag_name == "div":
                        seen_imgs = set()

                        # 先抓当前 div 下所有 img
                        img_tags = await child.query_selector_all("img")
                        for img_tag in img_tags:
                            src = await img_tag.get_attribute("src")
                            if src and src not in seen_imgs:
                                seen_imgs.add(src)
                                images.append(src)
                                content += f"!#@img[{src}]!#@"

                        # 如果有轮播按钮，处理尚未抓取的图片
                        carousel_next_btn = await child.query_selector(".js-carousel-next")
                        if carousel_next_btn:
                            while True:
                                await carousel_next_btn.click()
                                await asyncio.sleep(0.5)  # 等待轮播动画加载

                                current_img = await child.query_selector("img")
                                src = await current_img.get_attribute("src") if current_img else None
                                if not src or src in seen_imgs:
                                    break  # 已经抓过或不存在就停止
                                seen_imgs.add(src)
                                images.append(src)
                                content += f"!#@img[{src}]!#@"

            # 写入或更新 CSV
            existing_data[url] = {
                "URL": url,
                "Title": title,
                "Subtitle": subtitle,
                "Author": author,
                "Time": time,
                "Content": content,
                "Images In Article": ";".join(images)
            }

            # 每抓取一篇就保存
            with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["Title","Subtitle","Author","Time","Content","Images In Article","URL"])
                writer.writeheader()
                for row in existing_data.values():
                    writer.writerow(row)

            print(f"抓取完成并保存: {title}")

        await browser.close()

asyncio.run(fetch_blog_details())
