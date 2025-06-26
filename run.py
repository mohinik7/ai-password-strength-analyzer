import pickle

with open('model_enhanced.pkl','rb') as file:
    data = pickle.load(file)
    
print(data)