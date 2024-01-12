#This code runs in downloads folder and storea new folders as images , pdf , and words if they are not already created , then stores every type file within the coresponding folder
#This code iss written by znl_arad


import os
import shutil

def organize_downloads_folder():
    # Downloads folder
    downloads_folder = os.path.expanduser("~/Downloads")

    # Set up the paths for the destination folders
    pdf_folder = os.path.join(downloads_folder, "pdf")
    words_folder = os.path.join(downloads_folder, "words")
    images_folder = os.path.join(downloads_folder, "images")

    # Creating the folders if they don't exist
    for folder in [pdf_folder, words_folder, images_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # List all files in the Downloads folder
    files = os.listdir(downloads_folder)

    for file in files:#looks at every file lke line by line in text
        file_path = os.path.join(downloads_folder, file)

        # Check if the file is a PDF
        if file.lower().endswith(".pdf"):
            shutil.move(file_path, os.path.join(pdf_folder, file))

        # Check if the file is a Word document
        elif file.lower().endswith((".doc", ".docx")):
            shutil.move(file_path, os.path.join(words_folder, file))

        # Check if the file is an image
        elif file.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
            shutil.move(file_path, os.path.join(images_folder, file))

if __name__ == "__main__":
    organize_downloads_folder()
    print("]The folder is now  organized.")