import os
import shutil
import time
from urllib.request import urlretrieve
import pyautogui  # Optional, for GUI automation

# Function to download PDF files from a list of URLs
def download_pdfs(url_list, download_dir, prefix="Report_"):
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    for idx, url in enumerate(url_list, 1):
        filename = f"{prefix}{idx}.pdf"
        filepath = os.path.join(download_dir, filename)
        try:
            urlretrieve(url, filepath)
            print(f"Downloaded: {filepath}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")

# Function to rename files in a directory with a custom prefix and numbering
def rename_files(directory, prefix, extension):
    files = [f for f in os.listdir(directory) if f.lower().endswith(extension.lower())]
    for idx, filename in enumerate(files, 1):
        old_path = os.path.join(directory, filename)
        new_filename = f"{prefix}{idx}{extension}"
        new_path = os.path.join(directory, new_filename)
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} -> {new_path}")

# Function to clean a folder by moving files of a certain type to a target directory
def clean_folder(source_dir, target_dir, extensions):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    for filename in os.listdir(source_dir):
        if any(filename.lower().endswith(ext.lower()) for ext in extensions):
            src_path = os.path.join(source_dir, filename)
            dst_path = os.path.join(target_dir, filename)
            shutil.move(src_path, dst_path)
            print(f"Moved: {src_path} -> {dst_path}")

# Function to bulk-rename image files by appending a timestamp
def bulk_rename_images(directory, extensions=(".jpg", ".png")):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    for filename in os.listdir(directory):
        if any(filename.lower().endswith(ext) for ext in extensions):
            name, ext = os.path.splitext(filename)
            new_filename = f"{name}_{timestamp}{ext}"
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed: {old_path} -> {new_path}")

# Optional: Use pyautogui to open a folder (Windows example)
def open_folder_with_gui(path):
    os.startfile(path)
    time.sleep(1)
    # Example: Move mouse and click (customize as needed)
    # pyautogui.moveTo(100, 100)
    # pyautogui.click()

# Example usage (customize as needed)
if __name__ == "__main__":
    # Example URLs for PDF download
    pdf_urls = [
        # "https://example.com/file1.pdf",
        # "https://example.com/file2.pdf",
    ]
    download_dir = "downloads"
    image_dir = "images"
    target_dir = "organized_images"

    # download_pdfs(pdf_urls, download_dir)
    # rename_files(download_dir, "Report_", ".pdf")
    # clean_folder(image_dir, target_dir, [".jpg", ".png"])
    # bulk_rename_images(target_dir)
    # open_folder_with_gui(target_dir)

# Customize the function calls above as needed for your workflow.
