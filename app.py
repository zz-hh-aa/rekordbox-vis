import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'xml'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']

    # save file to server
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # process file to generate graph
    html_graph = graph_xml(file_path)

    return html_graph

# function to check for correct file type
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# def graph_xml(file_path):
    # CODE HERE TO PARSE XML, CREATE GRAPH AND GENERATE HTML

if __name__ == "__main__":
    app.run(debug=True)