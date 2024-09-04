from InquirerPy import inquirer
from scripts.convert_one_to_docx import convert_one_to_docx 
from scripts.convert_one_to_pdf import convert_one_to_pdf

def main_menu():
    while True:
        choice = inquirer.select(
            message="Hello, this is a converter project, where you can access some options:",
            choices=[
                "Convert file from DOCX -> PDF",
                "Convert file from PDF -> DOCX",
                "QUIT"
            ],
            default="Convert ONE file from DOCX -> PDF",
        ).execute()

        if choice == "Convert ONE file from DOCX -> PDF":
            convert_one_to_pdf("pdf")
        elif choice == "Convert ONE file from PDF -> DOCX":
            convert_one_to_docx("docx")
        elif choice == "QUIT":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main_menu()