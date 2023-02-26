import os
import warnings
from flask import Flask, render_template, request, redirect, session
from speech import transcripe
from summarization import english_summarization, long_summarization, arabic_summarization
warnings.filterwarnings('ignore')

app = Flask(__name__)
app.secret_key = "my_secret_key_@secret"
app.config["UPLOAD_DIR"] = "./static/assets/uploads"


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/get-transcription')
def get_transcription():
    session["transcription"] = transcripe(session["audio_path"]) if "transcription" not in session else session["transcription"]
    return session["transcription"]

@app.route('/get-short-english-summarization')
def get_short_english_summarization():
    transcription = get_transcription()
    session["short_english_summarization"] = english_summarization(transcription) if "short_english_summarization" not in session else session["short_english_summarization"]
    return session["short_english_summarization"]

@app.route('/get-short-arabic-summarization')
def get_short_arabic_summarization():
    short_english_summarization = get_short_english_summarization()
    session["short_arabic_summarization"] = arabic_summarization(short_english_summarization) if "short_arabic_summarization" not in session else session["short_arabic_summarization"] 
    return session["short_arabic_summarization"]

@app.route('/get-long-english-summarization')
def get_long_english_summarization():
    transcription = get_transcription()
    session["long_english_summarization"] = long_summarization(transcription) if "long_english_summarization" not in session else session["long_english_summarization"]
    return session["long_english_summarization"]

@app.route('/get-long-arabic-summarization')
def get_long_arabic_summarization():
    long_english_summarization = get_long_english_summarization()
    session["long_arabic_summarization"] = arabic_summarization(long_english_summarization) if "long_arabic_summarization" not in session else session["long_arabic_summarization"]
    return session["long_arabic_summarization"]

@app.route('/reset-session', methods=["POST"])
def reset_session():
    global file
    file = request.files['file']
    upload_file() # I want to call this function in get_transcription function but it gives me error related to file access. It's not right to call upload file here, becuase this will upload any file I choose in html even if I am not going to transcripe it
    session.pop("transcription", None)
    session.pop("short_english_summarization", None)
    session.pop("short_arabic_summarization", None)
    session.pop("long_english_summarization", None)
    session.pop("long_arabic_summarization", None)
    return ""

def upload_file():
    audio_path = os.path.join(app.config['UPLOAD_DIR'], file.filename)
    file.save(audio_path)    
    session["audio_path"] = audio_path
    
if __name__=="__main__":
    app.run(debug=True,threaded=True)
