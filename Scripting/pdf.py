import pypdf
#to withch to using pathlib later
import sys

inputs = sys.argv[1:] #starts at arg 1 but gets a list of all given

# with open(r'.\pdfs\dummy.pdf', 'rb') as file:
#     reader = pypdf.PdfReader(file)
#     print(reader.get_num_pages())
#     page = reader.get_page(0)
#     page.rotate(90)
#     writer = pypdf.PdfWriter()
#     writer.add_page(page)
#     with open(r'.\pdfs\tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)

import sys

inputs = sys.argv[1:] #starts at arg 1 but gets a list of all given

def pdf_combiner(pdfs):
    merger = pypdf
    for pdf in pdfs:
        print(pdf)
        #need to check merge files documentation - seens to be changed.

pdf_combiner(inputs)



#to withch to using pathlib later
# from pathlib import Path

# base_folder = Path.cwd()
# file_folder = base_folder / 'pdf'
