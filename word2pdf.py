import os
from docx2pdf import convert

# 获取当前文件夹中的所有文件
files = os.listdir()
# 遍历所有文件
for file in files:
    # 如果文件是Word文档
    if file.endswith(".docx"):
        # 将Word文档转换为PDF
        convert(file)
