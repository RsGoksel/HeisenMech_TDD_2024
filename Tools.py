import pytesseract
from PyPDF2 import PdfReader, PdfWriter
from pdf2image import convert_from_path
import numpy as np
import cv2
import re
import json
import os
import glob

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

pattern = re.compile(r"Soru özeti_\d+: (.*?)\nParagraf_\d+: (.*?)\nSoru_\d+: (.*?)(?=\n\Soru özeti_\d+|$)", re.DOTALL)

def extract_paragraf(text):
    
    matches = pattern.findall(text)
    
    data = []
    
    for match in matches:
        
        soru_ozeti = match[0].strip()
        paragraf = match[1].strip()
        soru = match[2].strip()
        
        entry = {
            "soru_ozeti": soru_ozeti,
            "paragraf": paragraf,
            "soru": soru
        }
        
        # Add the dictionary to the list
        data.append(entry)
        
    return data

pattern_ops = re.compile(r"Paragraf_\d+: (.*?)\nSoru_\d+: (.*?)\nŞıklar_\d+: (.*?)(?=\n\S|$)", re.DOTALL)
             

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

alternates = [
    " bu kelimeleri kullanarak bir paragraf sorusu yaz: ",
    " bu kelimeler ile bir paragraf sorusu sor",
    " bunlar ile bir paragraf sorusu sor",
    " konularından bir paragraf sorusu yaz",
    " bu kelimelerden bir paragraf sorusu sor",
    " bu kelimeleri kullanarak Türkçe paragraf sorusu sor",
    " bir paragraf sorusu yaz",
    " : bu ifadeler ile bir paragraf sorusu oluştur",
    " bu anahtar kelimeler ile bir paragraf sorusu yaz",
    " : bu anahtar sözcükleri kullanarak bir paragraf sorusu oluştur",
    " bu kelimelerden yola çıkarak bir paragraf sorusu sor",
    " : bu kelimeleri kullanarak bir paragraf yaz ve bir soru sor",
    " bu kelimelerden bir paragraf oluştur ve soruyu ekle",
    " : bu kelimeleri kullanarak kapsamlı bir paragraf sorusu yaz",
    " bu terimleri kullanarak bir paragraf sorusu oluştur",
    " : verilen kelimelerle bir paragraf sorusu hazırla",
    " bu sözcükleri kullanarak bir paragraf sorusu yaz",
    " : bu ifadelerden bir paragraf sorusu oluştur",
    " bu terimlerle bir paragraf sorusu hazırla",
    " bu anahtar sözcüklerle bir paragraf sorusu yaz",
]

import random

def create_Paragraf_JSON_training_dataset(Json_folder_path, output_path, verbose=False):
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
                    instruction = item.get('soru_ozeti', '').strip()
                    input = item.get('paragraf', '').strip()
                    output = item.get('soru', '').strip()
                
                    if instruction and input and output:
                        
                        dataset.append({
                            #"input": instruction,  
                            'instruction': instruction + random.choice(alternates),
                            "output": "Paragraf: " + input + 'Soru: ' + output
                            
                        })
                    else:
                        instruction = item.get('Soru özeti', '').strip()
                        input = item.get('Paragraf', '').strip()
                        output = item.get('Soru', '').strip()
                        dataset.append({
                            #"input": instruction,  
                            'instruction': instruction + random.choice(alternates),
                            "output": "Paragraf: " + input + 'Soru: ' + output
                            
                        })
    
    with open(output_path, 'w', encoding='utf-8') as out_file:
        
        json.dump(dataset, out_file, ensure_ascii=False, indent=4)

    if verbose:
        print(f"Dataset created and saved to {output_path}")

alternate_options = [
    " bu paragraf ve soruyu ele alarak 5 adet opsiyon yaz. ",
    " verilen paragraftan ve sorusundan yola çıkarak 5 adet opsiyon yaz.",
    " aşağıdaki paragraf ve soruya dayanarak 5 seçenek oluştur.",
    " bu paragrafı ve soruyu kullanarak 5 farklı opsiyon yaz.",
    " verilen paragraf ve soruya göre 5 seçenek oluştur.",
    " aşağıdaki paragraftan ve sorudan 5 opsiyon üret.",
    " bu paragraf ve soru için 5 farklı seçenek yaz.",
    " verilen paragraf ve soru çerçevesinde 5 alternatif opsiyon yaz.",
    " bu paragraf ve sorudan hareketle 5 seçenek yaz.",
    " aşağıdaki paragraf ve soruya dayanarak 5 farklı seçenek oluştur.",
    " bu metin ve soruyu kullanarak 5 adet seçenek yaz.",
    " paragrafı ve soruyu kullanarak 5 farklı opsiyon üret.",
    " aşağıdaki paragraf ve soru için 5 alternatif seçenek oluştur.",
    " verilen metin ve sorudan 5 farklı seçenek yaz.",
    " bu paragraf ve sorudan yola çıkarak 5 farklı opsiyon oluştur.",
    " verilen paragraf ve soruyu kullanarak 5 adet opsiyon üret.",
    " bu paragraf ve soruya dayanarak 5 adet seçenek oluştur.",
    " aşağıdaki metin ve soru üzerinden 5 farklı opsiyon yaz.",
    " bu paragraf ve sorudan yola çıkarak 5 farklı seçenek oluştur.",
    " verilen paragraf ve soruyu kullanarak 5 alternatif opsiyon yaz."
]

def create_opsiyon_JSON_training_dataset(Json_folder_path, output_path, verbose=False):
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
                # paragraf   #soru   #opsiyonlar
                
                for item in data:
                    instruction = item.get('paragraf', '').strip() + item.get('soru', '').strip()  
                    
                    output = item.get('opsiyonlar', '').strip()
                
                    if instruction and input and output:
                        
                        dataset.append({
                            'instruction': instruction + random.choice(alternate_options),
                            "output": "Şıklar: " + output
                            
                        })
                    
    
    with open(output_path, 'w', encoding='utf-8') as out_file:
        
        json.dump(dataset, out_file, ensure_ascii=False, indent=4)

    if verbose:
        print(f"Dataset created and saved to {output_path}")


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


def text_to_json(file_path):
    """
    Text dolu paragraf folder'ını alır ve hepsini json yapar.
    """
    
    pattern = re.compile(r'Soru özeti_(\d+): (.*?)\nParagraf_\1: (.*?)\nSoru_\1: (.*?)\n', re.DOTALL)
    
    # Function to convert text to JSON
    def convert_text_to_json(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    
        matches = pattern.findall(content)
    
        data = []
        for match in matches:
            data.append({
                'Soru özeti': match[1],
                'Paragraf': match[2],
                'Soru': match[3]
            })
    
        json_path = file_path.replace('.txt', '.json')
        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
    
    # Traverse through the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            convert_text_to_json(file_path)
    
    print('Conversion completed.')
