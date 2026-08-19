import os
import shutil

print("File Organizer 📂")

folders = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3"],
    "Videos": [".mp4"]
}

for folder in folders:
    if not os.path.exists(folder):
        os.mkdir(folder)

files = os.listdir()

for file in files:
    for folder, extensions in folders.items():
        if file.endswith(tuple(extensions)):
            shutil.move(file, folder)
            print(f"{file} moved to {folder}")

print("Files organized! ✅")