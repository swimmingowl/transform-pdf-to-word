import pdfplumber

pdf_file = '填入你的文件地址'

with pdfplumber.open(pdf_file) as pdf:
    for page_num, page in enumerate(pdf.pages):
        min_x0 = float('inf')
        max_x1 = float('-inf')

        for word in page.extract_words():
            min_x0 = min(min_x0, word['x0'])
            max_x1 = max(max_x1, word['x1'])

        distance = max_x1 - min_x0
        print(f'Page {page_num + 1}: The distance between the leftmost and rightmost words is {distance}')
