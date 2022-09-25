import json
import pypdfium2 as pdfium
import pytesseract
from PIL import Image
import cv2
import os
import numpy as np
import PyPDF2
from os.path import join
from tempfile import TemporaryDirectory
from pdf2image import convert_from_path
from img2pdf import convert
from Json_dict import Find_Keys_and_Values

j=0
RESP_DICT = {
    "code": [],
    "data": {
        "mvr_reports": {"report_provided_by": [],"customer": [],"actor": [],
            "customer_ref": [],"customer_sub": [],"date_completed": [],"first_name": [],"last_name": [],"license_no": [],"state": []
        },
        "mvr_driver_reports": {"driver_name": [],"social_sec_no": [],"dob": []},
        "mvr_driver_license": {
            f"{j}": {"license": [],"license_state": [],"issue": [],"expires": [],"status": [],"class": [],"restrictions": []},
        },
        "violations": {},"actions": {
            f"{j}": {
                "type": [],"order_date": [],"start_date": [],"thru_date": [],"end_date": [],"sp": [],"code": [],"acd": [],"description": []},},
        "cdl": {"med_status": [],"cert_status": [],"issue_date": [],"expiry_date": [],"cert_date": [],"posted_date": [],"examiner": [],
            "examiner_phone": [],"juris": [],"examiner_lic": [],"examiner_regno": [],"examiner_type": [],"restrictions": []}
    },
    "message": [],
    "status": {"created_at": [],"statusCode": [],"statusMessage": []}
}

def Grey_Scale(file_name,output_name):

    with TemporaryDirectory() as temp_dir:
        images = convert_from_path(file_name, output_folder=temp_dir,grayscale=True, fmt="jpeg", thread_count=4)

        image_list = list()
        for page_number in range(1, len(images) + 1):
            path = join(temp_dir, "page_" + str(page_number) + ".jpeg")
            image_list.append(path)
            images[page_number - 1].save(path, "JPEG")
        with open(output_name, "bw") as gray_pdf:
            gray_pdf.write(convert(image_list))

def create_Json(text):

    with open(r"C:\Users\AKther NAveedV\PycharmProjects\OCR\uploads\demofile2.txt","a") as f:
        for i in text:
            i = i.encode("ascii", "ignore")
            i = i.decode()
            f.write(f"{i}")
    txt = ""
    with open(r"C:\Users\AKther NAveedV\PycharmProjects\OCR\uploads\demofile2.txt", 'r') as f:
        for line in f:
            Dict = Find_Keys_and_Values(line,RESP_DICT)
            txt = txt + line

    os.remove(r"C:\Users\AKther NAveedV\PycharmProjects\OCR\uploads\demofile2.txt")
    return json.dumps(txt)

def image_processing(image):

    image = cv2.resize(np.array(image), None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.erode(image, kernel, iterations=1)
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    image = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)

    return image

def pdf_to_image(name):
    import time
    pdfFileObj = open(name, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj,strict=False)
    pdfWriter = PyPDF2.PdfFileWriter()
    x = pdfReader.numPages
    Y = 10
    if x>=30:
        Y = 5
    for page in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(page)
        pageObj.scale(.2, .2)
        pdfWriter.addPage(pageObj)

    newFile = open(r"C:\Users\AKther NAveedV\PycharmProjects\OCR\uploads\image_2.pdf", 'wb')
    pdfWriter.write(newFile)
    pdfFileObj.close()
    newFile.close()

    os.remove(name)
    pdf = pdfium.PdfDocument(r'C:\Users\AKther NAveedV\PycharmProjects\OCR\uploads\image_2.pdf')
    size = (7016, 4961)
    page_indices = [i for i in range(len(pdf))]
    renderer = pdf.render_topil(page_indices=page_indices,)

    text , i = "" , 0
    for image, index in zip(renderer, page_indices):
        i = i + 1
        print(i)
        image = image_processing(image)
        image = Image.fromarray(np.uint8(image)).convert('RGB')
        image = image.resize(size, Image.ANTIALIAS)
        image.thumbnail(size, Image.ANTIALIAS)

        image.save(r"C:\Users\AKther NAveedV\PycharmProjects\OCR\uploads\image_1.png")
        time.sleep(2)
        image.save(r"C:\Users\AKther NAveedV\PycharmProjects\OCR\uploads\image_2.tiff", 'TIFF')
        image = Image.open(r"C:\Users\AKther NAveedV\PycharmProjects\OCR\uploads\image_2.tiff")

        text = text + pytesseract.image_to_data(image)
        image.close()
        os.remove(r"C:\Users\AKther NAveedV\PycharmProjects\OCR\uploads\image_2.tiff")

    pdf.close()
#    os.remove(r"C:\Users\AKther NAveedV\PycharmProjects\OCR\uploads\image_2.pdf")
    return create_Json(text)