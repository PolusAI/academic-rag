import sys
import os
#from dotenv import load_dotenv

# bring in our LLAMA_CLOUD_API_KEY
from dotenv import load_dotenv

load_dotenv()


# bring in deps
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader

# set up parser
parser = LlamaParse(
    result_type="markdown"  # "markdown" and "text" are available
)
file_extractor = {".pdf": parser}

#get input and output directories, set up reader
output_dir = 'parsed_data'
input_dir = '../data'
reader = SimpleDirectoryReader(input_dir = input_dir, file_extractor=file_extractor)

#iterate through as we parse and create a file. 
all_docs = []
i = 1 #index based on document order
for docs in reader.iter_data():
    output_file = os.path.join(output_dir, f"parsed_document_{i}.md")
    j = 0
    with open(output_file, "a") as file:
        for doc in docs:
            if j == 0:
                #attempts to parse out abstract individually-- problem is inconsistent addressing between papers.
                abstract_file = os.path.join(output_dir, f"parsed_abstract_{i}.md")
                with open(abstract_file, "w") as f:
                    f.write(doc.text)
            all_docs.append(doc)
            file.write(doc.text + "\n\n")
            j = j + 1
    
    i = i + 1


