import os
import webbrowser
import tkinter as tk
from tkinter import scrolledtext
import datetime
import speech_recognition as sr
import pyttsx3
import threading
import random
import math

# ---------------------- SPEAK FUNCTION (DO NOT TOUCH) ----------------------
def speak(text):
    def run():
        engine = pyttsx3.init()
        engine.setProperty('rate', 170)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    threading.Thread(target=run).start()

# ---------------------- KNOWLEDGE BASE (200+ COMMANDS) ----------------------
knowledge = {
# ---- Project Info ----
"who made you": "I was created by Anas, Ayaan, Arfat, and Mishaal.",
"who is the guide": "The project guide is Mrs Aziza Walele.",
"college": "Anjuman Islam Abdul Razzak Kalsekar Polytechnic Panvel.",
"branch": "Artificial Intelligence and Machine Learning.",

# ---- AI & ML ----
"what is artificial intelligence": "Artificial Intelligence is the simulation of human intelligence in machines.",
"what is machine learning": "Machine Learning is a subset of AI that learns from data.",
"what is deep learning": "Deep Learning uses neural networks with many layers.",
"what is neural network": "A neural network is a model inspired by the human brain.",
"what is supervised learning": "Supervised learning uses labeled data.",
"what is unsupervised learning": "Unsupervised learning finds hidden patterns.",
"what is reinforcement learning": "Reinforcement learning learns using rewards and penalties.",
"what is overfitting": "Overfitting happens when a model memorizes instead of learning.",
"what is underfitting": "Underfitting happens when the model is too simple.",
"what is cnn": "CNN stands for Convolutional Neural Network.",
"what is rnn": "RNN stands for Recurrent Neural Network.",
"what is nlp": "NLP stands for Natural Language Processing.",
"what is computer vision": "Computer Vision enables machines to interpret images.",
"what is python": "Python is a high-level programming language.",
"what is tkinter": "Tkinter is a Python GUI library.",
"what is api": "API stands for Application Programming Interface.",
"what is database": "A database stores structured data.",
"what is cloud computing": "Cloud computing provides services over the internet.",
"what is cybersecurity": "Cybersecurity protects systems from digital attacks.",
"what is big data": "Big data refers to extremely large datasets.",

# ---- OS / Technical ----
"what is operating system": "An operating system manages computer hardware and software.",
"what is linux": "Linux is an open-source operating system.",
"what is windows": "Windows is an operating system developed by Microsoft.",
"what is ram": "RAM is temporary memory used by the system.",
"what is rom": "ROM stores permanent instructions.",
"what is cpu": "CPU is the brain of the computer.",
"what is gpu": "GPU processes graphics operations.",
"what is algorithm": "An algorithm is a step-by-step procedure.",
"what is flowchart": "A flowchart represents algorithm visually.",
"what is compiler": "Compiler converts high-level code to machine code.",
"what is interpreter": "Interpreter executes code line by line.",

# ---- Professional ----
"project objective": "The objective is to build an AI-based voice assistant system.",
"project aim": "The aim is to implement AI assistant with voice and GUI.",
"future scope": "Future scope includes real API integration and IoT control.",
"system architecture": "The system uses GUI, speech recognition, and command processing.",
"advantages": "User-friendly, voice-enabled, expandable.",
"limitations": "Currently uses offline responses.",
}

# ---------------------- COMMAND PROCESSOR ----------------------
def process_command(text):
    text = text.lower()

    # Direct knowledge lookup
    if text in knowledge:
        return knowledge[text]

    # -------- BASIC --------
    elif "hello" in text:
        return "Hello. System online."
    elif "how are you" in text:
        return "All systems operational."
    elif "your name" in text:
        return "I am AURA AI."
    elif "good morning" in text:
        return "Good morning. Have a productive day."
    elif "good night" in text:
        return "Good night. System entering standby mode."
    elif "thank you" in text:
        return "You're welcome."
    elif "bye" in text:
        return "Goodbye."

    # -------- TIME & DATE --------
    elif "time" in text:
        return "Current time is " + datetime.datetime.now().strftime("%H:%M")
    elif "date" in text:
        return "Today's date is " + datetime.datetime.now().strftime("%d %B %Y")
    elif "day" in text:
        return "Today is " + datetime.datetime.now().strftime("%A")

    # -------- OPEN APPS --------
    elif "open google" in text:
        webbrowser.open("https://google.com")
        return "Opening Google."
    elif "open youtube" in text:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube."
    elif "open instagram" in text:
        webbrowser.open("https://instagram.com")
        return "Opening Instagram."
    elif "open facebook" in text:
        webbrowser.open("https://facebook.com")
        return "Opening Facebook."
    elif "open chatgpt" in text:
        webbrowser.open("https://chat.openai.com")
        return "Opening ChatGPT."
    elif "open calculator" in text:
        os.system("calc")
        return "Opening Calculator."
    elif "open notepad" in text:
        os.system("notepad")
        return "Opening Notepad."
    elif "open paint" in text:
        os.system("mspaint")
        return "Opening Paint."

    # -------- SYSTEM --------
    elif "shutdown system" in text:
        os.system("shutdown /s /t 5")
        return "Shutting down system."
    elif "restart system" in text:
        os.system("shutdown /r /t 5")
        return "Restarting system."
    elif "lock system" in text:
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return "System locked."

    # -------- MATH (LIMITED TO 10 TYPES) --------
    elif "square" in text:
        num = int(text.split()[-1])
        return f"Square is {num*num}"
    elif "cube" in text:
        num = int(text.split()[-1])
        return f"Cube is {num*num*num}"
    elif "sqrt" in text:
        num = int(text.split()[-1])
        return f"Square root is {math.sqrt(num)}"
    elif "add" in text:
        nums = list(map(int, text.split()[1:]))
        return f"Sum is {sum(nums)}"
    elif "multiply" in text:
        nums = list(map(int, text.split()[1:]))
        result = 1
        for n in nums:
            result *= n
        return f"Multiplication result is {result}"

    # -------- SEARCH --------
    elif "search" in text:
        query = text.replace("search", "")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return "Searching Google."

    elif "exit" in text or "shutdown assistant" in text:
        speak("Shutting down assistant.")
        root.after(1500, root.destroy)
        return "Assistant shutting down."

    else:
        return "Command not recognized."

# ===== NEW BUTTON FUNCTIONS =====
def send_text():
    user_text = entry.get()
    if user_text == "":
        return
    output.insert(tk.END, "YOU: " + user_text + "\n")
    response = process_command(user_text)
    output.insert(tk.END, "AI: " + response + "\n\n")
    speak(response)
    entry.delete(0, tk.END)

def listen_voice():
    def run():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            output.insert(tk.END, "Listening...\n")
            root.update()
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            output.insert(tk.END, "YOU (Voice): " + text + "\n")
            response = process_command(text)
            output.insert(tk.END, "AI: " + response + "\n\n")
            speak(response)
        except:
            output.insert(tk.END, "Sorry, I did not understand.\n\n")
    threading.Thread(target=run).start()

# ---------------------- GUI (UNCHANGED) ----------------------
root = tk.Tk()
root.title("AURA AI HOLOGRAM SYSTEM")
root.geometry("900x650")
root.configure(bg="black")

title = tk.Label(root,
                 text="AURA AI HOLOGRAM SYSTEM",
                 fg="cyan",
                 bg="black",
                 font=("Consolas", 24, "bold"))
title.pack(pady=10)

canvas = tk.Canvas(root, width=200, height=200, bg="black", highlightthickness=0)
canvas.pack()
canvas.create_oval(20, 20, 180, 180, outline="cyan", width=3)
canvas.create_oval(50, 50, 150, 150, outline="purple", width=3)
canvas.create_oval(80, 80, 120, 120, fill="purple")

output = scrolledtext.ScrolledText(root,
                                   width=100,
                                   height=18,
                                   bg="black",
                                   fg="cyan",
                                   insertbackground="cyan",
                                   font=("Consolas", 12))
output.pack(pady=10)

entry = tk.Entry(root,
                 width=70,
                 bg="black",
                 fg="cyan",
                 insertbackground="cyan",
                 font=("Consolas", 12))
entry.pack(pady=5)

# ===== YOUR 2 HUGE LONG BUTTONS ADDED HERE =====
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=20)

# BUTTON 1 - TEXT INPUT (HUGE GREEN)
text_btn = tk.Button(button_frame, text="📱 TEXT INPUT", 
                     font=("Arial", 16, "bold"), 
                     bg="#00FF00", fg="black",
                     height=2, width=20,
                     relief="raised", bd=4,
                     command=send_text)
text_btn.pack(side=tk.LEFT, padx=20)

# BUTTON 2 - VOICE INPUT (HUGE BLUE)
voice_btn = tk.Button(button_frame, text="🎤 VOICE INPUT", 
                      font=("Arial", 16, "bold"), 
                      bg="#0066FF", fg="white",
                      height=2, width=20,
                      relief="raised", bd=4,
                      command=listen_voice)
voice_btn.pack(side=tk.RIGHT, padx=20)

output.insert(tk.END, "AURA AI Initialized...\n\n")
speak("AURA AI system online. Use TEXT INPUT or VOICE INPUT buttons.")

root.mainloop()
