# Written by Kristian Muri Knausgård 2023-08-31, partially using GPT-4
#
# Note: Main thread and GUI is partially blocked by the API call, and no feedback is shown while waiting for results.
#
import openai
import pyperclip
import tkinter as tk
from tkinter import Button
import pyautogui  # Mouse pointer position
import time

# Globals
last_clipboard_content = ""
update_pending = True


def rewrite_text(text):
    openai.api_key = "your-openai-api-key-here"

    prompt =   f"You are a merited academic writer using clear language. For the following task, avoid translating," \
               f"and if language is difficult to figure out, assume Norwegian, English, or German." \
               f"Rewrite the text inbetween the lines in a "\
               f"grammatically near perfect and professional and spelling error-free manner:\n"\
               f"------------------\n"\
               f"{text}\n"\
               f"------------------\n"

    message = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=message,
        temperature=0.2,
        max_tokens=100,
        frequency_penalty=0.0
    )

    return response['choices'][0].message.content

def read_clipboard():
    return pyperclip.paste()

def update_clipboard(new_content):
    pyperclip.copy(new_content)

def apply_rewrite(root, canvas, clipboard_content):
    global update_pending
    update_pending = True
    root.destroy()  # Destroy window first
    new_content = rewrite_text(clipboard_content)
    update_clipboard(new_content)


def rewrite_content():
    global last_clipboard_content, update_pending
    clipboard_content = read_clipboard()

    if update_pending:
        update_pending = not update_pending
        last_clipboard_content = clipboard_content
        return

    if clipboard_content != last_clipboard_content:
        print("Displaying buttons.")  # Debug message
        last_clipboard_content = clipboard_content
        x, y = pyautogui.position()
        root = tk.Tk()
        root.overrideredirect(True)
        root.geometry(f"160x30+{x}+{y}")
        root.wm_attributes('-alpha', 0.8)
        root.wm_attributes('-topmost', True)

        canvas = tk.Canvas(root, bg='SystemButtonFace', bd=0, highlightthickness=0, width=160, height=30)
        canvas.pack()

        rewrite_button = Button(canvas, text="Rewrite", command=lambda: root.after(1, apply_rewrite, root, canvas, clipboard_content))
        cancel_button = Button(canvas, text="Cancel", command=root.destroy)
        canvas.create_window(40, 15, anchor='center', window=rewrite_button)
        canvas.create_window(120, 15, anchor='center', window=cancel_button)

        root.after(5000, root.destroy)
        root.mainloop()

if __name__ == "__main__":
    while True:
        rewrite_content()
        time.sleep(0.2)
        
