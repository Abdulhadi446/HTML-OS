from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Define a path for storing uploaded files
UPLOAD_FOLDER = os.path.join(app.root_path, 'static/uploads')  # Make sure to store files in the static folder
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Update templates rendering paths, just ensure that templates are in the templates folder
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/paint')
def paint():
    return render_template('Paint.html')

@app.route('/mainIndex')
def mainIndex():
    return render_template('mainIndex.html')

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.route('/Video')
def Video():
    return render_template('Video.html')

@app.route('/VS_Code')
def VS_Code():
    return render_template('VS_Code.html')

@app.route('/notepad')
def Notepad():
    return render_template('Notepad.html')

@app.route('/Cmd')
def Cmd():
    return render_template('Cmd.html')

@app.route('/python_runner')
def python_runner():
    return render_template('python_runner.html')

@app.route('/create-file', methods=['POST'])
def create_file():
    # Get the Python code input from the form data
    user_python_code = request.form.get('python_code', '')

    # Handle empty code submission
    if not user_python_code:
        return render_template('python_runner.html', error="No code provided.")

    # Ensure the Python code is wrapped in <py-script> tag
    file_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Code Runner</title>
    <link rel="stylesheet" href="https://pyscript.net/releases/2024.10.2/core.css" type="text/css" media="all" />
    <script type="module" src="https://pyscript.net/releases/2024.10.2/core.js"></script>
</head>
<body>
    <a href="/python_runner">Click to edit</a>
    <py-script>
    {user_python_code}
    </py-script>
</body>
</html>
    """
    
    # Define the file path in the static/uploads folder
    file_name = 'python_file.html'
    file_path = os.path.join(UPLOAD_FOLDER, file_name)
    
    # Create and write to the file
    with open(file_path, 'w') as file:
        file.write(file_content)
    
    return render_template('python_file.html')

@app.route('/create-filehtml', methods=['POST'])
def create_filehtml():
    # Get the HTML code input from the form data
    user_html_code = request.form.get('HTML_code', '')

    # Handle empty code submission
    if not user_html_code:
        return render_template('python_runner.html', error="No code provided.")

    # Write the HTML code directly into a file
    file_content = f"{user_html_code}"
    
    # Define the file path in the static/uploads folder
    file_name = 'python_file.html'
    file_path = os.path.join(UPLOAD_FOLDER, file_name)
    
    # Create and write to the file
    with open(file_path, 'w') as file:
        file.write(file_content)
    
    return render_template('python_file.html')

@app.route('/python_file')
def python_file():
    return render_template('python_file.html')

@app.route('/htmlrunner')
def htmlrunner():
    return render_template('htmlrunner.html')

if __name__ == '__main__':
    # When running on PythonAnywhere, don't use debug mode
    app.run(debug=False, host='0.0.0.0')