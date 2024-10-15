import img2pdf
import os
from typing import Final

BASE_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR: Final[str] = os.path.join(BASE_DIR, 'images')
OUTPUT_DIF: Final[str] = os.path.join(BASE_DIR, 'output')


def prepare_images_to_process() -> list[str]:
    if not os.path.isdir(IMAGES_DIR):
        print(f'Folder: {IMAGES_DIR} not found!')
        return []

    image_paths: list[str] = list()
    for filename in os.listdir(IMAGES_DIR):
        if filename.endswith(('png', 'jpg', 'jpeg')):
            image_path = os.path.join(IMAGES_DIR, filename)
            image_paths.append(image_path)
        else:
            print(f"File '{filename}' has wrong extension!- I'm skipping it")
    return image_paths


def check_output_file_exist(file_path: str) -> bool:
    return os.path.isfile(file_path)


def create_new_file_path(old_file_path: str) -> str:
    old_file_path = old_file_path[:-4] + '{}' + old_file_path[-4:]
    counter: int = 0
    is_exist: bool = True
    new_file_path: str = ''
    while is_exist:
        new_file_path = old_file_path.format(counter)
        is_exist = os.path.isfile(new_file_path)
        counter += 1
    return new_file_path


def write_img_to_pdf(image_files: list[str], pdf_name: str = 'output.pdf') -> None:
    pdf: bytes = img2pdf.convert(image_files)

    if not os.path.isdir(OUTPUT_DIF):
        os.makedirs(OUTPUT_DIF)

    output_pdf_path: str = os.path.join(OUTPUT_DIF, pdf_name)
    if check_output_file_exist(output_pdf_path):
        output_pdf_path = create_new_file_path(output_pdf_path)

    with open(output_pdf_path, 'wb') as file:
        file.write(pdf)
    output_pdf_name = output_pdf_path.split('\\')[-1]
    print(f'Result pdf file save as "{output_pdf_name}".')


def main() -> None:
    print('Welcome in IMAGE TO PDF CONVERTER!')

    images_to_process: list[str] = prepare_images_to_process()
    if len(images_to_process) == 0:
        print("No images in the folder!")
        return
    print(f'Number of images to process: {len(images_to_process)}.')

    print('Converting images to pdf ... ')
    write_img_to_pdf(images_to_process)


if __name__ == '__main__':
    main()
