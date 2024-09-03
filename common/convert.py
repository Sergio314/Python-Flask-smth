import sys
import subprocess
import re
import os


supported_formats = ["docx", "pdf"]

def convert_to(src, outdir=None, timeout=None, fileType=None):
    if fileType not in supported_formats:
        raise ValueError(f"Invalid output format: {fileType}. Choose one of {supported_formats}")
    if fileType == "docx":
        args = [libreoffice_exec(), '--headless', '--convert-to', fileType+":writer_pdf_Export", src]
    else:
        args = [libreoffice_exec(), '--headless', '--convert-to', fileType, src]


    process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    match = re.search('-> (.*?) using filter', process.stdout.decode())

    if match is None:
        raise LibreOfficeError(process.stdout.decode())
    generated_pdf = match.group(1)
    
    if outdir:
        # Move the generated PDF to the specified output directory
        output_path = os.path.join(outdir, os.path.basename(generated_pdf))
        os.rename(generated_pdf, output_path)
        return output_path
    else:
        return generated_pdf
    
def libreoffice_exec():
    return 'libreoffice'

class LibreOfficeError(Exception):
    def __init__(self, output):
        self.output = output

if __name__ == '__main__':
    outdir = sys.argv[1] if len(sys.argv) > 2 else None
    print('Converted to ' + convert_to(sys.argv[2], outdir))