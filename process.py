import os
import shutil

def archive_pdf():
    # 归档到文件夹
    pdf_file_list = os.listdir("./")
    for item in pdf_file_list:
        if os.path.isfile(item) and item.lower().endswith(".pdf"):
            dir_name = item[0].upper()
            if not os.path.exists(dir_name):
                os.mkdir(f"./{dir_name}")
            shutil.move(item, f"{dir_name}/{item}")


def generate_md():
    # 生成Markdown
    dir_list = os.listdir("./")
    pdf_dict = {}
    for item in dir_list:
        if os.path.isdir(item) and item.isalpha():
            pdf_dict[item] = os.listdir(item)
    print(pdf_dict)
    md_start = """# 常用python库的速查表
    收集常用python库的速查表"""
    md_index = "\n\n"
    for item in dir_list:
        if os.path.isdir(item) and item.isalpha():
            temp = f"[{item}](#{item})\t"
            md_index += temp

    md_content = "\n\n"
    for key in pdf_dict.keys():
        md_content += f"## {key}\n"
        for item in pdf_dict[key]:
            temp = f"- [{item}](./{key}/{item})\n\n"
            md_content += temp

    f = open("README.md", mode='w', encoding='utf-8')
    f.write(md_start + md_index + md_content)
    f.close()

if __name__ == '__main__':
    archive_pdf()
    generate_md()
