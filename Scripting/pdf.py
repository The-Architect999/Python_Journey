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
# write using specific methods required onlly later
merger = pypdf.PdfWriter()
stamp = pypdf.PdfReader(r".\pdfs\wtr.pdf").pages[0]
for pdf in inputs:
    merger.append(pdf)
    #need to check merge files documentation - seens to be changed.
    #pyPDF2 - pypdf
for page in merger.pages:
    page.merge_page(stamp)
merger.write(r".\pdfs\combined.pdf")
print("all pages watermarked suscessfully!")



#to withch to using pathlib later
# from pathlib import Path

# base_folder = Path.cwd()
# file_folder = base_folder / 'pdf'
