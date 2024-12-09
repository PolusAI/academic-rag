import pymupdf
import fitz

file_path= "/home/jovyan/work/2401/2401.00001v1.pdf" #tester

pdf=fitz.open(file_path) #testing opening with documentation
pdf.metadata

pdf.get_toc() #table of contents 

page_content= pdf.load_page(10).get_text().replace("\t", " ")
print(page_content) #removes \

selected_arxiv = [
    '2401.00796', '2401.00759', '2401.00875', '2401.00296', '2401.00817', '2401.00929',
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
    '2401.00148', '2401.00118', '2401.00571', '2401.00657'
] #same list as doctr

pdf_base_dir = '/home/jovyan/work/2401'#folder it will be looking through

#adds v1.pdf to ids and looks through folder for the pdfs
import os
def find_pdf_path(pdf_base_dir, arxiv_id):
    target_filename = arxiv_id + "v1.pdf"  
    
    for root, dirs, files in os.walk(pdf_base_dir):
        if target_filename in files:
            return os.path.join(root, target_filename)
    
    return None

#pymupdf begins to parse and add to a list 
def analyze_arxiv_pdfs(arxiv_id, pdf_base_dir = '/home/jovyan/work/2401'):
    results = []
    for arxiv_id in arxiv_id:
        # path is found
        pdf_path = find_pdf_path(pdf_base_dir, arxiv_id)
        
        # skips
        if not pdf_path:
            continue
        pdf_file=fitz.open(pdf_path)

        num_pages = pdf_file.page_count
        book_content = []
        for i in range(num_pages):
            page = pdf_file.load_page(i)
            page_text = page.get_text() 
            raw_txt = page_text.replace("\t", " ")
            book_content.append(raw_txt)  
        results.append({arxiv_id: book_content})

    return results

arxiv_contents = analyze_arxiv_pdfs(selected_arxiv, pdf_base_dir)
arxiv_contents

output_folder = '/home/jovyan/work/proj1/pymu_output'
 #goes through each item in list and places on a new folder as atxt file
for content_dict in arxiv_contents:
    for three_selected, results in content_dict.items():  
        extracted_text = "\n".join(results)  

        base_filename = three_selected 
        output_file_path = os.path.join(output_folder, f'{base_filename}.txt')  #defines the file

        with open(output_file_path, 'w') as output_file:
            output_file.write(extracted_text)