import fitz
import os

# Function to extract text from a PDF page
def extract_text_from_page(page, page_number, output_folder):
    # Extract and save the text from the page
    text = page.get_text()
    text_path = os.path.join(output_folder, f"page{page_number}_text.txt")
    with open(text_path, 'w', encoding='utf-8') as text_file:
        text_file.write(text)

# Open the PDF file
pdf_path = 'ViewJournal.pdf'
pdf = fitz.open(pdf_path)

# Create a directory to store the extracted images and text
os.makedirs("images_24", exist_ok=True)
os.makedirs("text_24", exist_ok=True)

# Iterate over each page in the PDF
for page_number, page in enumerate(pdf, start=1):
    # Extract and save the text from the page
    extract_text_from_page(page, page_number, "text_24")

    # Iterate over each image on the page
    for image_index, image in enumerate(page.get_images(), start=1):
        # Get the XREF of the image
        xref = image[0]

        # Get the image data as a Pixmap
        pixmap = fitz.Pixmap(pdf, xref)

        # Save the image as PNG
        image_path = f"images_24/page{page_number}_image{image_index}.png"
        pixmap.save(image_path, "png")

        # Close the Pixmap
        pixmap = None

# Close the PDF file
pdf.close()
