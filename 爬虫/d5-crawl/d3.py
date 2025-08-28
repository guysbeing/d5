import pandas as pd
import re

INPUT_FILE = "mit_admissions_details.csv"
OUTPUT_FILE = "mit_admissions_cleaned.csv"

# 读取原文件
df = pd.read_csv(INPUT_FILE)

# 去掉 Author 前缀 "by "（忽略大小写）
df["Author"] = df["Author"].apply(lambda x: x[3:] if str(x).lower().startswith("by ") else x)

# 去掉 Title 末尾的 "by ..." 后缀
df["Title"] = df["Title"].apply(lambda x: re.sub(r'\s+by\s+.*$', '', str(x), flags=re.IGNORECASE))

# 保留所需列
columns_to_keep = ["Title", "Subtitle", "Author", "Time", "Content", "Images In Article"]
df_cleaned = df[columns_to_keep]

# 保存为新文件
df_cleaned.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

print(f"已生成 {OUTPUT_FILE}，共 {len(df_cleaned)} 条记录")
