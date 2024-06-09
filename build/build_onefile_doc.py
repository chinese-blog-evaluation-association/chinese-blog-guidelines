import os, re

output: str = ""

# 插入README.md


# 将 README.md 不提倡的设计和提倡的设计 中的链接（例./doc/cbgb001.md）换为文章内部锚点（例#cbgb001）
def change_link_in_readme(matched: re.Match) -> str:
    return str(matched.group(0)).replace("./doc/", "#").removesuffix(".md").upper()


with open(f"./README.md", mode="r", encoding="utf-8") as f:
    readme_md: str = (
        re.sub(r"./doc/[A-Za-z0-9]+.md", change_link_in_readme, f.read()) + "\n"
    )
    output += readme_md


# 插入解释文档
# 筛选文件名
doc_files: list[str] = [
    file_name for file_name in os.listdir("./doc") if file_name.endswith(".md")
]


def change_link_in_explanation(matched: re.Match) -> str:
    return f"[Example](#{str(matched.group(0)[-21:-6]).upper()})"


for file_name in doc_files:
    with open(f"./doc/{file_name}", mode="r", encoding="utf-8") as f:
        # 将一级标题转换为二级标题
        title: str = f"## {f.readline()[3:10]}\n"

        # 二级标题转换为三级标题
        content: str = f.read().replace("##", "###")

        # 将解释文件中的示例文件链接指向示例对应的二级标题
        content = re.sub(
            r"\[Example\]\([A-Za-z0-9/.]+-example.html\)",
            change_link_in_explanation,
            content,
        )

        # 追加到末尾
        output += title + content + "\n"


# 插入示例文档（注：由于当前均为单 HTML 文件，因此目前仅扫描 .html 文件，不扫描 .css 和 .js 文件）
# 筛选文件夹名
example_dirs: list[str] = [
    dir_name for dir_name in os.listdir("./example") if dir_name.startswith("cbg")
]

for dir_name in example_dirs:
    with open(
        f"./example/{dir_name}/{dir_name}-example.html", mode="r", encoding="utf-8"
    ) as f:
        # 生成标题
        title: str = f"## {dir_name.upper()}-EXAMPLE\n\n"

        # 读取示例文件，生成代码块样式
        content: str = f"```html\n{f.read()}```"

        # 追加到末尾
        output += title + content + "\n\n"

# 输出结果

with open("output.md", mode="w+", encoding="utf-8") as f:
    f.write(output.removesuffix("\n"))
