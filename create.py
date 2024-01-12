from PyPDF2 import PdfReader, PdfWriter

# Open PDF
file_pdf = PdfReader(r'C:\Users\dipud\PycharmProjects\pdfMarker\test.pdf')


def create_pdf(password: str):
    out_pdf = PdfWriter()
    for i in range(len(file_pdf.pages)):
        page_details = file_pdf.pages[i]
        out_pdf.add_page(page_details)
    out_pdf.encrypt(password)
    with open('question.pdf', 'wb') as f:
        out_pdf.write(f)


