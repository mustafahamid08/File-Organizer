import os
import shutil

SOURCE_FOLDER = input("Enter the folder path to organize: ")

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Presentations": [".ppt", ".pptx"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Programs": [".py", ".exe", ".js", ".html", ".css"]
}


def organize_files():
    if not os.path.exists(SOURCE_FOLDER):
        print("Folder not found.")
        return

    for file_name in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file_name)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_name)[1].lower()

            category_found = False

            for category, extensions in FILE_CATEGORIES.items():
                if file_extension in extensions:
                    category_folder = os.path.join(SOURCE_FOLDER, category)

                    if not os.path.exists(category_folder):
                        os.makedirs(category_folder)

                    destination = os.path.join(category_folder, file_name)

                    shutil.move(file_path, destination)

                    print(f"Moved: {file_name} → {category}")
                    category_found = True
                    break

            if not category_found:
                other_folder = os.path.join(SOURCE_FOLDER, "Others")

                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)

                destination = os.path.join(other_folder, file_name)

                shutil.move(file_path, destination)

                print(f"Moved: {file_name} → Others")

    print("\nFiles organized successfully!")


organize_files()