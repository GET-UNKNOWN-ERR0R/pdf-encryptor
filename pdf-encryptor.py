from PyPDF2 import PdfReader, PdfWriter
import getpass

def encrypt_pdf(input_pdf, output_pdf, password):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(password)
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)
    print(f"The PDF has been encrypted and saved as {output_pdf}")

if __name__ == "__main__":
    input_pdf = input("Enter the input PDF file path (with .pdf extension): ")
    try:
        with open(input_pdf, "rb") as file:
            pass
    except FileNotFoundError:
        print("The specified file was not found. Please check the file path.")
        exit(1)
    output_pdf = input("Enter the output PDF file path (with .pdf extension): ")
    password = getpass.getpass(prompt="Enter the numeric password for encryption: ")
    if not password.isdigit():
        print("The password must be a number. Please try again.")
        exit(1)
    encrypt_pdf(input_pdf, output_pdf, password)
