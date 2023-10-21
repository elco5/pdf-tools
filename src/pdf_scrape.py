import PyPDF2
import os
print("running..")
pdf_directory = r'C:\Users\ecountrywood\dev\tools\pdf_tools\data\pdf_inputs'  # Replace with the path to your directory of PDF files
output_directory = r'C:\Users\ecountrywood\dev\tools\pdf_tools\data\raw_outputs'  # Replace with the path to the directory where you want to save text files

# Iterate over all PDF files in the specified directory
for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        pdf_file_path = os.path.join(pdf_directory, filename)
        # print("processing:  ", pdf_file_path)
        output_text_file = os.path.splitext(filename)[0] + '.txt'  # Create a corresponding text file

        # Specify the full path for the output text file
        output_text_file_path = os.path.join(output_directory, output_text_file)

        # Open the PDF file
        pdf_file = open(pdf_file_path, 'rb')

        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # # Get the number of pages in the PDF (should be 1 for a single-page PDF)
        # num_pages = pdf_reader.getNumPages()

        # Extract text from the single page
        page = pdf_reader.pages[0]
        page_text = page.extract_text()

        # Close the PDF file
        pdf_file.close()

        # Save the extracted text to the specified output directory
        with open(output_text_file_path, 'w', encoding='utf-8') as text_file:
            text_file.write(page_text)

        print(f'Text from {filename} has been saved to {output_text_file_path}')
