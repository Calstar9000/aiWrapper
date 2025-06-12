from apiKey import key
import google.generativeai as genAI
import tkinter

genAI.configure(api_key=key)
model = genAI.GenerativeModel()
chat = model.start_chat(history=[])

def getAIResponce():
    entryBoxInput = entryBox.get()
    entryBox.delete(0, tkinter.END)

    result = chat.send_message(entryBoxInput, stream=True)

    outputBox.config(state='normal')
    outputBox.insert(tkinter.END, f'USER: {entryBoxInput}\n\n')
    outputBox.insert(tkinter.END, f'GEMINI: ')
    # {result.text.strip().replace('*', '')}\n\n
    for i in result:
        outputBox.insert(tkinter.END, (i.text.replace('*', '')))
        print(i.text)
        outputBox.update_idletasks()
        outputBox.see(tkinter.END)
    outputBox.insert(tkinter.END, '\n\n')
    outputBox.config(state='disabled')


root = tkinter.Tk()
root.title("AI Wrapper")
root.geometry('1000x500')

entryBox = tkinter.Entry(root, width=30)
entryBox.pack(pady=10)

submitButton = tkinter.Button(root, text="Submit", command=getAIResponce)
submitButton.pack(pady=5)

frame = tkinter.Frame(root)
frame.pack(fill='both', expand=True, padx=10, pady=10)

# Scrollbar
scrollbar = tkinter.Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

# Text widget for output
outputBox = tkinter.Text(frame, wrap='word', yscrollcommand=scrollbar.set, state='disabled')
outputBox.pack(side='left', fill='both', expand=True)

# Connect scrollbar
scrollbar.config(command=outputBox.yview)

root.mainloop()
