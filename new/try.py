from tkinter import *
import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
from googletrans import Translator , LANGUAGES
import tkinter.font as font

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator Created by MOHD HARIS")

        self.target_languages = list(LANGUAGES.values())  # Add or modify target languages as needed
        self.root.geometry('900x600')
        self.root.resizable(0,1)
        self.root.config(bg = '#F7DC6F')

        self.create_widgets()
        Label(self.root, text = "LANGUAGE TRANSLATOR", font = "arial 20 bold", bg='#F7DC6F').pack(pady=20)

    def create_widgets(self):
        
        # Text Input
        self.label_text = ttk.Label(self.root, text="Enter Text:", font=('Times',17),background='#F7DC6F')
        self.label_text.grid(row=0, column=0, padx=10, pady=10)
        self.label_text.place(x=180,y=95)

        self.text_input = ttk.Entry(self.root, width=40)
        self.text_input.grid(row=0, column=1, padx=10, pady=10)
        self.text_input.place(x=300,y=100)

        myFont = font.Font(weight="bold")

        # Voice Recognition Button
        self.voice_button = tk.Button(self.root, text="Voice Recognition", command=self.start_voice_recognition , width=20,font=('Times',8))
        self.voice_button['font']=myFont
        self.voice_button.grid(row=0, column=2, padx=10, pady=10, sticky='NSEW')
        self.voice_button.place(x=600,y=90)

        # Target Language Dropdown
        self.label_language = ttk.Label(self.root, text="Select Target Language:" , font=('Times',17),background="#F7DC6F")
        self.label_language.grid(row=1, column=0, padx=10, pady=10)
        self.label_language.place(x=160,y=180)

        self.selected_language = tk.StringVar()
        self.language_dropdown = ttk.Combobox(self.root, values=self.target_languages, textvariable=self.selected_language , font=('TImes',15))
        self.language_dropdown.grid(row=1, column=1, padx=10, pady=10)
        self.language_dropdown.set("english")
        self.language_dropdown.place(x=400,y=180)

        # Translate Button
        self.translate_button = tk.Button(self.root, text="Translate", command=self.translate_text , width=20 )
        self.translate_button['font']=myFont
        self.translate_button.grid(row=2, column=1, padx=10, pady=10 )
        self.translate_button.place(x=360,y=250)

        # Translated Output
        self.label_result = ttk.Label(self.root, text="Translated Text:" , font=('Times',17),background="#F7DC6F")
        self.label_result.grid(row=3, column=0, padx=10, pady=10)
        self.label_result.place(x=60, y=350)

        self.text_output = tk.Text(self.root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady= 5, width =60)
        self.text_output.grid(row=3, column=1, padx=10, pady=10)
        self.text_output.place(x = 240 , y = 350)

    def start_voice_recognition(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something:")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)

            try:
                text = recognizer.recognize_google(audio)
                print("You said:", text)
                self.text_input.delete(0, tk.END)
                self.text_input.insert(0, text)
            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print(f"Google API request failed: {e}")

    def translate_text(self):
        text_to_translate = self.text_input.get()
        target_language = self.selected_language.get()
        translation = self.translate_text_api(text_to_translate, target_language)

        self.text_output.delete(1.0, tk.END)
        self.text_output.insert(tk.END, translation)

    def translate_text_api(self, text, target_language='en'):
        translator = Translator()
        translation = translator.translate(text, dest=target_language)
        return translation.text

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()
