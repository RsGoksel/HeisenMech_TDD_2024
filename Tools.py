""" Author: RsMech - 12.06.2024 : Written for Teknofest2024_TDDİ """

import cv2
import re
import json
import os
import glob
import pytesseract

import numpy as np

from PyPDF2    import PdfReader, PdfWriter
from pdf2image import convert_from_path

def preprocess_image(image):
    
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    
    _, binary = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    binary = cv2.medianBlur(binary, 3)
    
    return binary

def extract_pages_from_pdf_writer(file_path, start_page, end_page):

    """
    Tek bir pdf dosyası için istenen aralıkta sayfaları arkaplanda OCR ile çalışarak text olarak alır 
    """
    
    pdf_reader = PdfReader(file_path)
    pdf_writer = PdfWriter()

    for page_num in range(start_page - 1, end_page):  # Convert to zero-based index
        pdf_writer.add_page(pdf_reader.pages[page_num])
        
    pdf_writer.write('temp.pdf')  # Save PdfWriter content to a temporary file
    pages = convert_from_path('temp.pdf')  # Convert PDF pages to images
    all_text = []
    for page in pages:
        processed_image = preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang='tur')
        all_text.append(text)
    return "\n".join(all_text)


def extract_singlepage_from_pdf_writer(file_path, page_num):
    """
    Tek bir pdf dosyası için istenen tek bir sayfayı arkaplanda OCR ile çalışarak text olarak alır """
    pdf_reader = PdfReader(file_path)
    pdf_writer = PdfWriter()
    
    pdf_writer.add_page(pdf_reader.pages[page_num - 1])  # Convert to zero-based index
    pdf_writer.write('temp.pdf')  # Save PdfWriter content to a temporary file
    
    pages = convert_from_path('temp.pdf')  # Convert PDF pages to images
    page = pages[0]  # There will be only one page
    processed_image = preprocess_image(page)
    text = pytesseract.image_to_string(processed_image, lang='tur')
    
    return text
    

def write2text(root, file_name='', text=''):
    """
    Text dosyasına yazar.
    """
    with open(root + file_name + '.txt', "w", encoding="utf-8") as file:
        file.write(text)
    
    with open(root + file_name + '.txt', "a", encoding="utf-8") as file:
        file.write("\n")
        
def get_text(file_path):
    """
    Text dosyasından text alır
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def split_pdf(file_path, save, init_threshold, termination_threshold):
    """
    Parametre olarak verilen PDF belgesini, verilen sayfalar arasında split eder.
    """
    pdf_reader = PdfReader(file_path)
    num_pages = len(pdf_reader.pages)
    
    for page_num in range(init_threshold, num_pages - termination_threshold):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])

        if save:
            output_file_path = f"{file_path[:-4]}_{page_num + 1}.pdf"
            with open(output_file_path, 'wb') as output_pdf_file:
                pdf_writer.write(output_pdf_file)
            
            print(f"Created: {output_file_path}")


ins_pattern = r'Instruction\d+:\s*(.*?)\s*(?=Response\d+:|$)'
res_pattern = r'Response\d+:\s*(.*?)\s*(?=Instruction\d+:|$)'

instruction_pattern = re.compile(ins_pattern, re.DOTALL)
response_pattern = re.compile(res_pattern, re.DOTALL)

def extract_data(text):
    instructions = instruction_pattern.findall(text)
    responses = response_pattern.findall(text)
    
    dataset = [{"instruction": inst.strip(), "response": resp.strip()} for inst, resp in zip(instructions, responses)]

    return dataset


          

def extract_opsiyon(text):
    matches = pattern_ops.findall(text)
    
    data = []
    
    for match in matches:
        paragraf = match[0].strip()
        soru = match[1].strip()
        siklar = match[2].strip()
        
        entry = {
            "paragraf": paragraf,
            "soru": soru,
            "opsiyonlar": siklar
        }
        
        data.append(entry)
        
    return data
    
def create_JSON_training_dataset(Json_folder_path, output_name, output_path='./', verbose=False):
    """
    JSON belgeleri içeren klasor yolu alarak tum json dosyalarından bir dataset JSON olusturur"""
    dataset = []

    # Traverse all files in the given folder
    for filename in os.listdir(Json_folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(Json_folder_path, filename)
            
            # Read the JSON file
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from file {file_path}: {e}")
                    continue

                # Extract instruction and response
                for item in data:
                    instruction = item.get('instruction', '').strip()
                    response = item.get('response', '').strip()

                    if instruction and response:
                        dataset.append({
                            "input": instruction,
                            "output": response
                        })

    #return dataset
    with open(output_path + output_name, 'w', encoding='utf-8') as out_file:
        
        json.dump(dataset, out_file, ensure_ascii=False, indent=4)

    if verbose:
        print(f"Dataset created and saved to {output_path + output_name}")
        
import random

def JSON_merge(directory_path, output_path):
    """
    Tüm json'ları birleştirir."""
    merged_data = []

    json_files = glob.glob(os.path.join(directory_path, '*.json'))

    for file in json_files:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                merged_data.extend(data)
            else:
                merged_data.append(data)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=4)

    print(f"Merged JSON saved to {output_path}")

