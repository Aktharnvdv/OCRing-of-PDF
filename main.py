from PIL import Image
import pytesseract
from flask import Flask, render_template, request
import os
import json
from text_extraction import pdf_to_image

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg','pdf']

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'uploads\\')

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods = ['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('Uploads.html', msg = 'No file selected')

        file = request.files['file']
        if file.filename == '':
            return render_template('Uploads.html', msg = 'No file')

        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

            if file.filename.rsplit('.', 1)[1].lower() != 'pdf':
                extracted = ocr_core(file)
                return render_template('Uploads.html',msg = 'OCR completed',extracted = json.dumps(extracted),img_src = UPLOAD_FOLDER + file.filename)
            else:
                text = pdf_to_image(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
                return render_template('Uploads.html', msg='OCR completed',extracted=text, img_src=UPLOAD_FOLDER + file.filename)
    else:
        return render_template('Uploads.html')

if __name__ == '__main__':
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    app.run()
