#!/usr/bin/env python3
"""
Documentation

See also https://www.python-boilerplate.com/flask
"""
import os
import argparse
import tkinter as tk
from flask import Flask, jsonify
from flask_cors import CORS
from logzero import logger
from tkinter import filedialog

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

    @app.route("/foo/<someId>")
    def foo_url_arg(someId):
        logger.info("/foo/%s", someId)
        return jsonify({"echo": someId})

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

        # Open directory selection dialog for output directory
        output_dir = filedialog.askdirectory(
            title="Select Output Directory:",
            mustexist=True
        )

        if output_dir:
            print(f"Selected output directory: {output_dir}")
            # Prepare paths for further processing (conversion, etc.)
            # At this point, you could call your conversion function
            return file_path, output_dir
        else:
            print("No output directory selected. Exiting...")
            return None, None
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
