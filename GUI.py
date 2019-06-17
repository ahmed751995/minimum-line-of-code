from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
from PIL import ImageTk, Image
import os
from model import *
from graph import *

def predict(*args):
    """ display statistics of the csv file"""
    try:
        data_file = path.get()
        predict_file(data_file)
        data = read_csv(data_file)
        plot_hist(data)
        plot_pie(data)
    except FileNotFoundError:
        pass


def predict_text(*args):
    """displayed the prediction of the text in text window """

    textp = text.get()
    predicted_text= get_prediction(textp)
    if predicted_text.tolist()[0] == 1: result = "Positive"
    else: result = "Negative"
    ttk.Label(root, text="").grid(column=0, row=5)
    text_window = tk.Text(root, width=50, height=5)
    text_window.grid(column=0, row=5, columnspan =2)
    text_window.insert(tk.END, result)
    text_window.config(font=('Arial', 30, 'bold'))

def browse():
    """ display the path of selected file """

    curr_directory = os.getcwd()
    file_path = filedialog.askopenfilename(initialdir = curr_directory, title = "Select file",filetypes = (("csv file","*.csv"),("all files","*.*")))
    path.set(file_path)


# Window initialization
root = tk.Tk()
root.config(bg='#252529')
#root.geometry("400x300")
root.title("Rewiew Classifier")
label_font = ('Arial',20, 'bold')
path= StringVar()
text = StringVar()
out=StringVar()


#text
text_entry = Entry(root, width=50,textvariable=text)
text_entry.grid(row=0, column=0)

text_label = Label(root, text='text')
text_label.config(font=label_font, fg='#ccc', bg='#252529')
text_label.config(height=1, width=20)
text_label.grid(row=0, column=1)
# browse_label.config(padx=20)

#Browse
browse_entry = Entry(root, width=50,textvariable=path)
browse_entry.grid(row=1, column=0)

browse_button = Button(root, text="Browse", command=browse)
browse_button.grid(row=1, column=1)
browse_button.config(padx=0)
browse_button.config(width=15)
browse_button.config(bg='#b90415',fg='#ccc')


#predict Buttons
predict_text_button = Button(root, text="Predict Text ", command=predict_text)
predict_text_button.grid(row=2, column=0)
predict_text_button.config(padx=100)
predict_text_button.config(width=5, height=2)
predict_text_button.config(font=label_font, fg='#ccc', bg='#b90415')

predict_file_button = Button(root, text="Predict File ", command=predict)
predict_file_button.grid(row=2, column=1)
predict_file_button.config(padx=100)
predict_file_button.config(width=5, height=2)
predict_file_button.config(font=label_font, fg='#ccc', bg='#b90415')




for child in root.winfo_children(): child.grid_configure(padx=5, pady=5)
root.mainloop()
