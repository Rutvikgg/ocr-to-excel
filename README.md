# OCR to Excel using Tesseract

## THE Team -
### [Rutvik P. Gondekar](https://github.com/Rutvikgg)   
### [Kamal D. Agrahari](https://github.com/kamalagrahari03) 
### [Akash A. Nahak](https://github.com/ak2484) 
### [Prabha S. Gawde](https://github.com/Prabha85) 

---

This project aims to automate the process of extracting text from images or scanned documents using Tesseract OCR and then organizing the extracted information into an Excel spreadsheet.

## Installation

1. Install Tesseract OCR: Follow the installation instructions for your operating system on the official [Tesseract GitHub repository](https://github.com/tesseract-ocr/tesseract).

2. Install Python dependencies:
   ```bash
   pip install pytesseract
   pip install openpyxl
   ```

## Usage

1. Place your images or scanned documents in the `input_images` directory.

2. Run the OCR script:
   ```bash
   python ocr_to_excel.py
   ```

3. The script will process the images, extract text using Tesseract OCR, and create an Excel file (`output_data.xlsx`) in the `output_excel` directory.

## Configuration

- Adjust Tesseract OCR settings or language options in the script (`ocr_to_excel.py`) based on your specific requirements.


## Contributing

Feel free to contribute by submitting bug reports, feature requests, or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

---
