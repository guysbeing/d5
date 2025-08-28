import asyncio
from playwright.async_api import async_playwright
import csv

async def fetch_all_blog_links():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        links = []


        max_page = 20
        for i in range(1, max_page + 1):
            url = f"https://mitadmissions.org/blogs/page/{i}/"
            await page.goto(url)
            await page.wait_for_selector("a.post-tease__h__link")

            links_elements = await page.query_selector_all("a.post-tease__h__link")
            for el in links_elements:
                href = await el.get_attribute("href")
                links.append(href)

            print(f"已抓取第 {i} 页，共 {len(links)} 个链接")

        await browser.close()

        # 保存链接到 CSV
        with open("blog_links.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["link"])
            for link in links:
                writer.writerow([link])

        print(f"抓取完成，总共 {len(links)} 个链接")

asyncio.run(fetch_all_blog_links())
