
# Image to PDF Converter

This project contains a Python script that converts images from a folder into a single PDF file. The script supports images in formats such as PNG, JPG, and JPEG and stores the resulting PDF in an output folder. The project uses the `img2pdf` library for the conversion.

## Project Structure

```
pyAutomationHub/
│
├── img_to_pdf/
│   ├── images/                    # Folder containing the images to be converted
│   ├── output/                    # Folder where the resulting PDF will be saved
│   └── image_to_pdf_converter.py  # Script that converts images to PDF

```

## Requirements

The project requires the following Python libraries:

- `img2pdf`
- `os` (standard Python library)
- `pathlib` (standard Python library)

You can install the required library using pip:

```bash
pip install img2pdf
```

## How to Run the Script

1. **Place images in the `images/` folder**:
   - Make sure to use only supported formats (PNG, JPG, JPEG).

2. **Run the script**:
   - You can run the script using the following command:

   ```bash
   python img_to_pdf/image_to_pdf_converter.py
   ```

3. **Check the output**:
   - The resulting PDF file will be saved in the `output/` folder. If a file with the same name already exists, a new file with a counter (e.g., `output0.pdf`, `output1.pdf`) will be created.

## Features

- Converts multiple images into a single PDF file.
- Automatically skips files with unsupported extensions.
- If the output PDF already exists, the script will generate a new file with a unique name to avoid overwriting.

## Example

1. Place your image files (e.g., `image1.jpg`, `image2.png`) into the `images/` folder.

2. Run the script:

   ```bash
   python img_to_pdf/image_to_pdf_converter.py
   ```

3. The resulting PDF file will be saved in the `output/` folder as `output.pdf` or with an incremented name if it already exists.
