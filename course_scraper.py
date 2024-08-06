import requests
from bs4 import BeautifulSoup
import PyPDF2
from io import BytesIO

#Install the required Python libraries with:
# pip install requests beautifulsoup4 PyPDF2

# Function to download and parse the PDF
def get_classes_from_pdf(pdf_url):
    response = requests.get(pdf_url)
    pdf_file = BytesIO(response.content)
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    num_pages = pdf_reader.numPages
    classes = set()
    
    for page_num in range(num_pages):
        page = pdf_reader.getPage(page_num)
        text = page.extract_text()
        if text:
            lines = text.split('\n')
            for line in lines:
                # You might need to adjust the parsing based on the PDF's text format
                if line.strip():  # simple check to avoid empty lines
                    classes.add(line.strip())
    
    return classes

# Function to check if a class exists on the website
def check_class_on_website(class_name, search_url):
    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Here, you would need to inspect the website structure to find the correct way to search for classes
    # This is a placeholder and needs proper implementation based on the actual website structure
    text = soup.get_text()
    return class_name in text

# URL of the PDF containing the class list
pdf_url = 'https://www.terry.uga.edu/wp-content/uploads/Upper-level-classes-without-prerequisites.pdf'

# URL of the website to search for classes
search_url = 'https://sis-ssb-prod.uga.edu/PROD/bwckschd.p_disp_dyn_sched'

# Get the list of classes from the PDF
classes = get_classes_from_pdf(pdf_url)

# Check each class on the website
for class_name in classes:
    exists = check_class_on_website(class_name, search_url)
    if exists:
        print(f'Class "{class_name}" exists on the website.')
    else:
        print(f'Class "{class_name}" does not exist on the website.')