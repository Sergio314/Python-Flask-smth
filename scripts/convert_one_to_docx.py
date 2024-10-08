#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog
from common.errors import InternalServerError
from common.convert import convert_to, LibreOfficeError
from subprocess import TimeoutExpired
import os

def convert_one_to_docx(fileTypeTo):
    root = tk.Tk()
    root.withdraw()

    # Open file input dialog to select PDF file
    file_path = filedialog.askopenfilename(
        title='Select 1 file to convert to DOCX:',
        filetypes=[("PDF Files", "*.pdf")]
    )

    if file_path:
        print(f"Selected file: {file_path}")
        try:
            # Ask user for save location and filename for PDF
            out_filename = filedialog.asksaveasfilename(
                title='Enter name for the DOCX file:',
                defaultextension=".docx",
                filetypes=[("DOCX Files", "*.docx")]
            )

            if not out_filename:
                print("Save operation canceled.")
                return

            # Extract directory and filename from the chosen save path
            output_dir = os.path.dirname(out_filename)

            # Perform the conversion and save the file to the selected location
            result = convert_to(file_path, outdir=output_dir, timeout=15, fileType=fileTypeTo, out_filename=out_filename)
            print(f"File successfully converted to: {result}")

        except LibreOfficeError:
            raise InternalServerError({'message': 'Error during conversion'})
        except TimeoutExpired:
            raise InternalServerError({'message': 'Timeout during conversion'})

    else:
        print("No file selected. Exiting...")

if __name__ == "__main__":
    # Run the file selection and conversion process
    select_file_convert("docx")
    # The script will automatically exit after the conversion is done
