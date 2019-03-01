import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



    
def read_csv(path):
    """ read csv file and return it as pandas data frame"""
    
    return pd.read_csv(path)

def store_csv(data_frame, path):
    """ takes pandas data frame and save it in path"""
    
    data_frame.to_csv(path)
              
    
def plot_hist(data_frame, column="Predict"):
    """display histogram based on column values
    data_frame: pandas data frame
    column: column name  """
    
    hist_plot = data_frame[column].hist()
    hist_plot.set_title('Histogram')
    hist_plot.set_xlabel('Reviews Classes')
    hist_plot.set_ylabel('Prediction Count')
    plt.show()

def plot_pie(data_frame, column="Predict"):
    """display pie chart based on column values
    data_frame: pandas data frame
    column: column name  """
    
    X=pd.value_counts(data_frame[column])
    to_list = list([str(X.index[i]) for i in range(2)])
    seq = ''.join(to_list)
    plt.pie(X,labels=seq,labeldistance=0.5, shadow=True)
    plt.show()

