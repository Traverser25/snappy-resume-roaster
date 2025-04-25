from flask import Flask, request, redirect, url_for, flash, render_template
from werkzeug.utils import secure_filename
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
import fitz  # PyMuPDF
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "default_secret")

# Rate limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["5 per minute"]
)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # Limit to 10 MB

RESUME_KEYWORDS = ['experience', 'education', 'skills', 'projects', 'summary', 'profile', 'internship', 'objective']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def seems_like_resume(text):
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in RESUME_KEYWORDS)

def get_chatgpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a humorous and blunt assistant that roasts resumes in a sarcastic like carryminati, very bluntly with humour. Use simple language and reference multiple Indian contexts and cultural elements to enhance the humor, also use Hindi words occasionally, plus infer the received resume data properly, taunt, mock, degrade."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Sorry, something went wrong with the AI."

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
@limiter.limit("5 per minute")
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        text = ""
        try:
            pdf_document = fitz.open(filepath)
            for page in pdf_document:
                text += page.get_text()
        except Exception as e:
            print(f"An error occurred while reading the PDF: {e}")
            flash("Unable to read PDF file.")
            return redirect(url_for('index'))

        if not seems_like_resume(text):
            flash("This doesn't look like a resume. Please upload a proper resume.")
            return redirect(url_for('index'))

        ai_response = get_chatgpt_response(text)
        return render_template('index.html', ai_response=ai_response)

    else:
        flash('Invalid file format. Please upload a PDF resume.')
        return redirect(request.url)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
