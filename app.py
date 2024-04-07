from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Handle the uploaded file
    # Process and generate the graph
    # For now, just redirecting back to home
    return 'File Uploaded Successfully'

if __name__ == "__main__":
    app.run(debug=True)