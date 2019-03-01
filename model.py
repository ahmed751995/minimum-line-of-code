from fastai import *
from fastai.text import *



def get_prediction(text):
    """ return the prediction value of the text
    text: plain text  """
    pass

def predict_file(data_file):
    """ add Predict column to data_file
    data_file: csv file """
    pass


# def prepare_learner(path ='',bs=48):
#     data_clas = TextClasDataBunch.load(path, 'tmp_clas', bs=bs)
#     learn = text_classifier_learner(data_clas, drop_mult=0.5)
#     learn.load_encoder('fine_tuned_enc')
#     learn.load('third')
#     return learn

# def prepare_learner_cpu(model_path='',name='fine_tuned_enc',path ='',bs=48):
#     model_path = '/home/ahmed/Documents/data/Prototype/models/'
#     data_clas = TextClasDataBunch.load(path, 'tmp_clas', bs=bs)
#     learn = text_classifier_learner(data_clas, drop_mult=0.5)
#     x = torch.load(f'{model_path+name}.pth',map_location='cpu')
#     get_model(learn.model)[0].load_state_dict(x)
#     learn.load('third')
#     return learn

# def get_prediction(review,learn):
#     print("getpred")
#     x = learn.predict(review)
#     print(x)
#     return np.argmax(x[-1],0)

# def predict_file22(path):
#     print("0")
#     df = pd.read_csv(path)
#     review = df.iloc[:,0]
#     prediction = [get_prediction(i,learn).tolist() for i in review]
#     df['predictions'] = prediction
#     print("1")
#     store_csv(df,path)
#     print("2")
#     visual_hist(df)
#     #return prediction

# learn = prepare_learner_cpu()
