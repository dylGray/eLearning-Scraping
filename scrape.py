import fitz

def scrape_pdf(pdf):
    try:
        pdf_doc = fitz.open(pdf)
    except FileNotFoundError:
        print(f'ERROR: the file "{pdf}" was not found')
        return None
    except Exception as e:
        print(f'an error occurred while opening the file - {e}')
        return None
    
    text = ''

    try:
        for page_num in range(len(pdf_doc)):
            page = pdf_doc.load_page(page_num)
            text += page.get_text('text') + '\n'
    except Exception as e:
        print(f'an error occurred while opening the file - {e}')

    text = text.replace('CONTINUE', '')
    text = text.replace('Complete the content above before moving on.', '')
    text = text.replace('Click the first lesson below or Start above to begin.', '')

    return text

pdf = 'files/day5/our-need-for-approval-and-how-it-affects-selling.pdf'
extracted_text = scrape_pdf(pdf)

if extracted_text is not None:
    try:
        with open('extracted_text.txt', 'w', encoding='utf-8') as file:
            file.write(extracted_text)
        print(f'extracted text from "{pdf}" and wrote to "extracted_text.txt" successfully.')
    except Exception as e:
        print(f'an error occurred while writing to "extracted_text.txt" - {e}')