from flask import Flask, request, render_template_string, redirect, url_for, flash
import os
import shutil
import time
from urllib.request import urlretrieve

# Import your automation functions from the existing script
from file_automation import download_pdfs, rename_files, clean_folder, bulk_rename_images

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flashing messages

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


from flask import render_template

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/download_pdfs", methods=["POST"])
def web_download_pdfs():
    urls = request.form['urls'].strip().splitlines()
    prefix = request.form.get('prefix', 'Report_')
    try:
        download_pdfs(urls, 'downloads', prefix)
        flash("PDFs downloaded successfully.")
    except Exception as e:
        flash(f"Error: {e}")
    return redirect(url_for('index'))

@app.route("/rename_files", methods=["POST"])
def web_rename_files():
    directory = request.form['directory']
    prefix = request.form['prefix']
    extension = request.form['extension']
    try:
        rename_files(directory, prefix, extension)
        flash("Files renamed successfully.")
    except Exception as e:
        flash(f"Error: {e}")
    return redirect(url_for('index'))

@app.route("/clean_folder", methods=["POST"])
def web_clean_folder():
    source_dir = request.form['source_dir']
    target_dir = request.form['target_dir']
    extensions = [e.strip() for e in request.form['extensions'].split(',')]
    try:
        clean_folder(source_dir, target_dir, extensions)
        flash("Folder cleaned successfully.")
    except Exception as e:
        flash(f"Error: {e}")
    return redirect(url_for('index'))

@app.route("/bulk_rename_images", methods=["POST"])
def web_bulk_rename_images():
    directory = request.form['directory']
    extensions = tuple(e.strip() for e in request.form['extensions'].split(','))
    try:
        bulk_rename_images(directory, extensions)
        flash("Images renamed successfully.")
    except Exception as e:
        flash(f"Error: {e}")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
