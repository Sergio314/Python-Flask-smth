#!/usr/bin/env python3
import os
import argparse
import tkinter as tk
from flask import Flask
from flask_cors import CORS
from logzero import logger
from tkinter import filedialog
from common.errors import InternalServerError
from common.convert import convert_to, LibreOfficeError
from subprocess import TimeoutExpired

# IF YOU WANT TO RUN SCRIPT JUST ONCE, JUST REMOVE ALL FLASK STUFF, YOU CAN exec not this file but convert_one_file.py in maindir
def create_app(config=None):
    app = Flask(__name__)

    # See http://flask.pocoo.org/docs/latest/config/
    app.config.update(dict(DEBUG=True))
    app.config.update(config or {})

    # Setup CORS headers to allow all domains
    # https://flask-cors.readthedocs.io/en/latest/
    CORS(app)

    # Definition of the routes
    @app.route("/")
    def hello_world():
        logger.info("/")
        return "Hello World"

    return app

def select_file_convert():
    root = tk.Tk()
    root.withdraw()

    # Open file input dialog to select DOCX file
    file_path = filedialog.askopenfilename(
        title='Select DOCX file to convert to PDF:',
        filetypes=[("DOCX Files", "*.docx")]
    )

    if file_path:
        print(f"Selected file: {file_path}")
        try:
            # Ask user for save location and filename for PDF
            out_filename = filedialog.asksaveasfilename(
                title='Enter name for a PDF file:',
                defaultextension=".pdf",
                filetypes=[("PDF Files", "*.pdf")]
            )
            if not out_filename:
                print("Save cancelled.")
                return None, None
            
             # Extract directory and filename from the chosen save path
            output_dir = os.path.dirname(out_filename)

            result = convert_to(file_path, outdir=output_dir, timeout=15)
            print(f"File successfully converted to: {result}")

        except LibreOfficeError:
            raise InternalServerError({'message': 'Error during conversion'})
        except TimeoutExpired:
            raise InternalServerError({'message': 'Timeout during conversion'})
        
        return file_path, out_filename
    else:
        print("No file selected. Exiting...")
        return None, None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", action="store", default="8000")

    args = parser.parse_args()
    port = int(args.port)

    # First, select file and output directory
    file_path, output_dir = select_file_convert()

    if file_path and output_dir:
        # Continue with Flask application if selection was successful
        app = create_app()
        app.run(host="0.0.0.0", port=port)
    else:
        # Exit if file or directory selection was unsuccessful
        print("Exiting script due to incomplete selections.")
