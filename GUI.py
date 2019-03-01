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
    predicted_text= str(get_prediction(textp))
    ttk.Label(mainframe, text="").grid(column=0, row=5)
    result = textp+" "+predicted_text
    text_window = tk.Text(mainframe, width=50, height=5)
    text_window.grid(column=0, row=5)
    text_window.insert(tk.END, result)

def browse():
    """ display the path of selected file """
    curr_directory = os.getcwd()
    file_path = filedialog.askopenfilename(initialdir = curr_directory, title = "Select file",filetypes = (("csv file","*.csv"),("all files","*.*")))
    path.set(file_path)


#root and title
root = Tk()
root.title("predict app")

#main frames
mainframe= ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#variables

path=StringVar()
text= StringVar()
out = StringVar()

#creating intries and labels and buttons
text_label = ttk.Label(mainframe, text="text")
text_entry = ttk.Entry(mainframe, width=50, textvariable=text)
browse_entry = ttk.Entry(mainframe, width=10, textvariable=path)
browse_button = ttk.Button(mainframe, text="Browse", command=browse)
predict_button = ttk.Button(mainframe, text ="predict file", command=predict)
predict_text_button= ttk.Button(mainframe, text ="predict text", command=predict_text)


#geometry setting
text_label.grid(column=1, row=0, sticky=(E,W))
text_entry.grid(column=0, row=0, sticky=(E,W))
browse_entry.grid(column=0, row=1, sticky=(E,W))
browse_button.grid(column=1, row=1, sticky=(E,W))
predict_button.grid(column=0, row=3, sticky=(E))
predict_text_button.grid(column=0, row=3, sticky=(W))

# add padding around all mainframe children 
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()



# old code

#learn = prepare_learner_cpu()

#from model import predict_file22

    
# def predict_file22(path):
#     print("0")
#     df = pd.read_csv(path)
#     review = df.iloc[:,0]
#     print("pred")
#     prediction = [get_prediction(i,learn).tolist() for i in review]
#     df['Predict'] = prediction
#     print("1")
#     store_csv(df,path)
#     print("2")
#     visual_hist(df)
#     #return prediction

# def get_prediction(review):
#     x = learn.predict(review)
#     return np.argmax(x[-1],0)
