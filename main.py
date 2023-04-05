import webbrowser
from tkinter import *
from tkinter import filedialog as fd
from PyPDF2 import PdfReader
from gtts import gTTS
import requests
import urllib.request

# API Constants---------------------------------------------------------------------
API = "ba1189a75cda43149bb513556ce1b838"
ENDPOINT = "https://api.voicerss.org/"
LANG = "en-us"
AUDIO = "MP3"
URLS = []
y_cord = 60

# Tkinter initialization--------------------------------------------------------
display = Tk()
display.title("PDF to Audiobook")
display.state("zoomed")


# Choose a pdf file to start----------------------------------------------------
text_per_page_in_file = []
filepath = None


def select_file():
    global filepath, text_per_page_in_file, y_cord
    y_cord = 60
    text_per_page_in_file = []
    filetypes = (('pdf', '.pdf'),)
    filename = fd.askopenfilename(title='Open a file',initialdir='/', filetypes=filetypes)
    filepath = filename
    uploadlabel.config(text=filepath)
    pdflabel.config(text="Press to scan pdf text")
    text_convert.config(state="active")


# Text Extraction using PDF Reader Python Library------------------------------
def extractext(filename):
    reader = PdfReader(filename)
    number_of_pages = len(reader.pages)
    for x in range(0, number_of_pages):
        page = reader.pages[x]
        text = page.extract_text()
        text_per_page_in_file.append(text)
    pdflabel.config(bg="#0F9D58", text="Ready for Speech conversion")
    speechlabel.config(text="Text to speech, ready")
    speech_convert.config(state="active")


# ------------------------------------------------------------------------------
def open_link(url):
    webbrowser.open(url)


# Text to Speech----------------------------------------------------------------
# using HTTP request and API
def apispeech(text_list):
    ix = 0
    global URLS, y_cord
    results = Canvas()
    results.place(x=60, y=220)
    for text in text_list:
        params = {"key": API, "src": text, "hl": LANG, "c": AUDIO}
        response = requests.get(url=ENDPOINT, params=params)
        URLS.append(response.url)
    for link in URLS:
        Label(results, text=f"Page {URLS.index(link)+1}").place(x=0, y=y_cord)
        Button(results, text="Download Audio", command=lambda url=link: open_link(url)).place(x=130, y=y_cord)
        ix +=1
        y_cord += 40


# using Google text to speech library
def speech(text_list):
    savepath = fd.asksaveasfilename()
    for page in text_list:
        tts = gTTS(page)
        tts.save(f'{savepath}.mp3')
# ------------------------------------------------------------------------------

# GUI---------------------------------------------------------------------------
Label(text="pdf to mp3 Converter", fg="#0F9D58", font=("Trebuchet MS", 40)).place(x=60, y=20)

select = Button(text="Upload PDF", command=select_file)
select.place(x=60, y=100)

uploadlabel = Label(background="#4285F4", width=60, fg="white")
uploadlabel.place(x=150, y=102.5)

text_convert = Button(text="Convert to text", command=lambda: extractext(filename=filepath), state="disabled")
text_convert.place(x=60, y=140)

pdflabel = Label(background="#F4B400", width=59, fg="white")
pdflabel.place(x=155, y=142.5)

# using gtts library
# speech_convert = Button(text="Convert to Speech", command=lambda: speech(text_list=text_per_page_in_file), state="disabled")

# using voice RRS APR
speech_convert = Button(text="Convert to Speech", command=lambda: apispeech(text_list=text_per_page_in_file), state="disabled")
speech_convert.place(x=60, y=180)

speechlabel = Label(background="#DB4437", width=56, fg="white")
speechlabel.place(x=175, y=182.5)

display.mainloop()
# -------------------------------------------------------------------------------
