import pdfplumber

def extract_text_from_pdf(file):
    try:
        with pdfplumber.open(file) as the_file:
            full_text=''
            for page in sorted(the_file.pages, key=lambda p: p.page_number):
                page_text = page.extract_text(x_tolerance=2, y_tolerance=3)
                if page_text:
                    full_text+=page_text + "\n"
            return full_text.strip()
    except Exception as e:
        raise ExtractionError(f"Unexpected error: {str(e)}")
        



class ExtractionError(Exception):
    pass
