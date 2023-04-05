# PDFtoAudiobook
The program is a PDF to Audiobook converter. It takes a PDF file as input, extracts the text from each page of the PDF, converts the text to speech, and outputs an audiobook file in MP3 format. The program offers two options for text-to-speech conversion: either using the Google Text-to-Speech (gTTS) library or the VoiceRSS API.

The program's graphical user interface (GUI) is implemented using the tkinter library. The GUI consists of a window with several buttons and labels. The user can upload a PDF file using the "Upload PDF" button, and the program displays the path of the selected file. The user can then click on the "Convert to text" button to extract the text from each page of the PDF. Once the text has been extracted, the user can click on the "Convert to Speech" button to convert the text to speech.

The program uses the PyPDF2 library to extract the text from the PDF file. The extracted text is stored in a list, with each element of the list representing the text of a single page of the PDF. The program then uses either the gTTS library or the VoiceRSS API to convert the text to speech. If the user chooses the gTTS option, the program saves the audiobook file to the user's specified location using the filedialog library. If the user chooses the VoiceRSS option, the program generates a download link for each page of the PDF and displays the links in the GUI.

Overall, the program provides a simple and user-friendly way to convert PDF files to audiobooks, which can be useful for people who prefer to listen to books rather than reading them.
