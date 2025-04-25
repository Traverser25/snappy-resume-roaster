# Snappy Resume Roaster

[Visit Snappy Resume Roaster](https://roastmyresume.pythonanywhere.com/)  

Welcome to **Snappy Resume Roaster**! A minimal and efficient tool to roast your resume using OpenAI's API with a touch of humor.

## What is Snappy Resume Roaster?

This is a small and simple project that allows you to upload your resume, and our AI will roast it with funny and witty responses. Whether you're looking for a lighthearted take on your resume or just want to see what our AI thinks, you're in the right place!

## Features

- **Minimal and simple design**: Focused on functionality without unnecessary fluff.
- **AI-powered roasting**: Using OpenAI's API, the project roasts resumes with humor.
- **Fast and responsive**: Light on resources while still providing a delightful experience.



## Future Prospects

While the current version is simple,  Here are a few enhancements that we plan to incorporate:

- **Robust Logging**: We'll be adding comprehensive logging to help with debugging and provide better insights into the app's behavior.
- **Rate Limiting**: In future releases, we will include rate limiting to ensure the API usage is controlled and avoid exceeding limits.
- **Rate Management**: To optimize performance, we’ll introduce a more advanced rate management system.
- **Clearly Defined and Pertinent Models**: We will refine the AI model used for resume roasting, ensuring it is more clearly defined and pertinent to the context of resume evaluation.
- **OpenAI Filtering**: We will implement OpenAI filtering techniques to enhance the quality and relevance of the AI responses, ensuring that the roast stays fun and appropriate!
- **Celery & Redis**: We will introduce **Celery** for asynchronous task management and **Redis** as the message broker. This will help us handle background tasks like resume processing more efficiently and scale the application.
## Getting Started

To get started with **Snappy Resume Roaster**, follow these steps:

### 1. Clone this repository

```bash
git clone https://github.com/Traverser25/snappy-resume-roaster.git

# Create a virtual environment (if not already done)
python -m venv roastenv

# Activate the environment
# On Windows
.\roastenv\Scripts\activate
# On macOS/Linux
source roastenv/bin/activate

pip install -r requirements.txt

setup your openai api  key

run app.py

visit  localhost:5000  , upload your resume and feel the roast


