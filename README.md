# Class Availability Checker
By using this script, you can efficiently verify class availability on a school's scheduling website based on a list of classes extracted from a PDF document that lists upper level course electives.

## Overview:
The task involves two main steps:
1. Download and Parse the PDF: Extract class names from the provided PDF file. Although extracting data from a PDF isn’t scraping, it is crucial for preparing the data for the next step.
2. Scrape the UGA Scheduling Website: Check if the extracted classes are listed on the UGA scheduling website. This involves sending HTTP requests to the website, parsing the HTML response, and searching for the class names.

## Key Components:
HTTP Requests: Use the requests library to fetch the PDF file and the scheduling webpage.
Text Extraction: Utilize PyPDF2 (or pdfplumber) to extract class names from the PDF.
HTML Parsing: Employ BeautifulSoup to navigate and search the HTML content of the scheduling website.

## Tools and Libraries:
requests: To handle HTTP requests and retrieve data from the web.
BeautifulSoup: For parsing HTML and extracting relevant information.
PyPDF2 or pdfplumber: To extract text from PDF files.
Selenium (Optional): For handling complex web interactions involving JavaScript or dynamic content.

## Usage:
This script allows you to automate the process of checking class availability, saving you time and ensuring you have the most up-to-date information directly from the source.
