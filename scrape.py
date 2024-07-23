import fitz

def scrape_pdf(pdf):
    pdf_doc = fitz.open(pdf)
    text = ''

    for page_num in range(len(pdf_doc)):
        page = pdf_doc.load_page(page_num)
        text += page.get_text('text') + '\n'

    text = text.replace('CONTINUE', '')

    return text

pdf = 'files/rise.pdf'
extracted_text = scrape_pdf(pdf)
print(f'extracted text from "{pdf}"')

with open('extracted_text.txt', 'w', encoding='utf-8') as file:
    file.write(extracted_text)