selected_arxiv = ['2401.00796', '2401.00759', '2401.00875', '2401.00296', '2401.00817', '2401.00929',
 '2401.00449', '2401.00871', '2401.00082', '2401.00077', '2401.00326', '2401.00500',
 '2401.00867', '2401.00249', '2401.00258', '2401.00472', '2401.00686', '2401.00010',
 '2401.00503', '2401.00337', '2401.00520', '2401.00770', '2401.00713', '2401.00854',
 '2401.00536', '2401.00650', '2401.00110', '2401.00635', '2401.00105', '2401.00610',
 '2401.00589', '2401.00245', '2401.00648', '2401.00332', '2401.00495', '2401.00070',
 '2401.00752', '2401.00214', '2401.00649', '2401.00484', '2401.00270', '2401.00823',
 '2401.00247', '2401.00887', '2401.00566', '2401.00476', '2401.00411', '2401.00608',
 '2401.00837', '2401.00738', '2401.00814', '2401.00849', '2401.00761', '2401.00069',
 '2401.00743', '2401.00401', '2401.00687', '2401.00451', '2401.00545', '2401.00989',
 '2401.00180', '2401.00712', '2401.00901', '2401.00466', '2401.00498', '2401.00775',
 '2401.00178', '2401.00613', '2401.00590', '2401.00170', '2401.00313', '2401.00822',
 '2401.00107', '2401.00591', '2401.00009', '2401.00288', '2401.00716', '2401.00087',
 '2401.00974', '2401.00906', '2401.00394', '2401.00352', '2401.00431', '2401.00708',
 '2401.00897', '2401.00560', '2401.00852', '2401.00739', '2401.00985', '2401.00133',
 '2401.00549', '2401.00622', '2401.00126', '2401.00747', '2401.00765', '2401.00611',
 '2401.00148', '2401.00118', '2401.00571', '2401.00657']

%matplotlib inline
import os
import doctr
from doctr.io import DocumentFile
from doctr.models import ocr_predictor
os.environ['USE_TORCH']='1'

import matplotlib.pyplot as plt
from doctr.io import DocumentFile
from doctr.models import ocr_predictor

#similar to pymupdf to create file path
def find_pdf_path(pdf_base_dir, arxiv_id):
    target_filename = arxiv_id + "v1.pdf"  
    
    for root, dirs, files in os.walk(pdf_base_dir):
        if target_filename in files:
            return os.path.join(root, target_filename)
    
    return None

model = ocr_predictor(pretrained=True) #based on doctr documentation 

def analyze_arxiv_pdfs(arxiv_id, pdf_base_dir = '/home/jovyan/work/2401'):#func to go through files to retrieve information
    results = []
    
    for arxiv_id in arxiv_id:
        pdf_path = find_pdf_path(pdf_base_dir, arxiv_id)
        
        if not pdf_path:#continues in case an id is not found
            continue
        
        doc = DocumentFile.from_pdf(pdf_path)  
        result = model(doc)  
        exported_result = result.export()  
        results.append((arxiv_id, exported_result))  
    
    return results


results = analyze_arxiv_pdfs(selected_arxiv)#parsing through 100 ids from 2024

analyze_arxiv_pdfs(arxiv_record('2105.05050'))#sample parse
results[-5:]#sample to see if func worked


output_folder = output_base_dir#recalling

for arxiv_id, results in selected_arxiv:
    extracted_text = ""
    base_filename = arxiv_id  
    output_file_path = os.path.join(output_folder, f'{base_filename}.txt')#renames files with given id name 
#pases json files
    for page in results['pages']:
        for block in page['blocks']:
            for line in block['lines']:
                for word in line['words']:
                    extracted_text += word['value'] + " "  
                extracted_text += "\n" 

    with open(output_file_path, 'w') as output_file:#will go through files and turn into txt file of parsed pdfs
        output_file.write(extracted_text)

