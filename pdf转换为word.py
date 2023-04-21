import pdfplumber
import os

def convert_pdf_to_md(pdf_path, md_path):
    with pdfplumber.open(pdf_path) as pdf:
        page_texts = []

        for page in pdf.pages:
            page_text = ''
            prev_word = None

            for word in page.extract_words():
                if prev_word:
                    x_diff = word["x0"] - prev_word["x1"]
                    y_diff = abs(word["top"] - prev_word["top"])

                    if 10 < abs(x_diff) < "填写pdf的宽度" :
                        page_text += '\n\n'
                    else:
                        page_text += ' '

                page_text += word["text"]
                prev_word = word

            page_texts.append(page_text)

        md_text = '\n\n'.join(page_texts)

    with open(md_path, 'w', encoding='utf-8') as md_file:
        md_file.write(md_text)

pdf_path = '填入地址'  # 请将此路径替换为您下载的 PDF 文件的路径
md_path = '填入地址'  # 输出的 Markdown 文件的路径
convert_pdf_to_md(pdf_path, md_path)

print("PDF 转换为 Markdown 完成。")
