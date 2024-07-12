# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 13:28:49 2024

@author: mkim3

"""
import fitz  #If you are using Python 3.8, install pymupdf module

def convert_pdf_to_images(pdf_path, output_folder, dpi=300, crop_percentage=None):
    zoom = dpi / 72
    doc = fitz.open(pdf_path)
    for page_number in range(len(doc)):
        page = doc.load_page(page_number)

        if crop_percentage:
            rect = page.rect  
            x0 = rect.width * crop_percentage[0]
            y0 = rect.height * crop_percentage[1] 
            x1 = rect.width * crop_percentage[2]
            y1 = rect.height * crop_percentage[3]
            page.set_cropbox(fitz.Rect(x0, y0, x1, y1))

        mat = fitz.Matrix(zoom, zoom)  
        pix = page.get_pixmap(matrix=mat) 

        output_path = f"{output_folder}/{pdf_path.split('.')[0]}_page_{page_number + 1}.png"
        pix.save(output_path)
        print(f"Saved: {output_path}")
        

pdf_path = "Record_7s.pdf"
output_folder = "outputs"
crop_percentage = ((1.10/5.8), (1.75/7.5), (5.6/5.8), (3.4/7.5))  # Crop percentage (left, top, right, bottom)
convert_pdf_to_images(pdf_path, output_folder, dpi=300, crop_percentage=crop_percentage)