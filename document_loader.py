from pypdf import PdfReader


def load_pdf(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text

## Testing / direct execution code
if __name__ == "__main__":

    text = load_pdf("documents/company_policy.pdf")

    print(text)