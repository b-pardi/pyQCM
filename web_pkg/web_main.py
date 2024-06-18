from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Ensure the file is safe to open
def allowed_file(filename):
    ext = filename.rsplit('.', 1)[1].lower()
    valid_exts = {'csv', 'xls', 'xlsx', 'xlsm', 'txt', 'qsd'}
    if '.' in filename and ext in valid_exts:
        return True
    else:
        return False


@app.route('/')
def index():
    return render_template("index.html")

'''@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # Here you would typically save the file and process it
            filename = secure_filename(file.filename)
            # file.save(os.path.join('/path/to/the/uploads', filename))
            # Process the file...
            # ...
            # Then you can redirect to another page or process the data
            # For simplicity, we'll just render the same page with a message
            return 'File successfully uploaded and being processed'
    return render_template('upload.html')'''

if __name__ == '__main__':
    app.run(debug=True)
