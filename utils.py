import numpy as np
import json
import pickle

class wineprediction():
    
    def __init__(self,data):
        self.data= data
        print(self.data)
        
    def __loading(self):
        
        """ This is fuction of wine_prediction model """
        
        with open('artifacts/project_data.json','r') as file:
            self.project_data = json.load(file)

        with open('artifacts/scale.pkl','rb') as file:
            self.scaler = pickle.load(file)

        with open('artifacts/model.pkl','rb') as file:  
            self.model = pickle.load(file)
            
            
    def get_wine_quality_prediction(self):
              
        self.__loading()  
        
        fixed_acidity = self.data['html_fixed_acidity']
        volatile_acidity = self.data['html_volatile_acidity']
        citric_acid = self.data['html_citric_acid']
        residual_sugar = self.data['html_residual_sugar']
        chlorides = self.data['html_chlorides']
        free_sulfur_dioxide = self.data['html_free_sulfur_dioxide']
        total_sulfur_dioxide = self.data['html_total_sulfur_dioxide']
        density = self.data['html_density']
        pH = self.data['html_pH']
        sulphates = self.data['html_sulphates']
        alcohol = self.data['html_alcohol']
        
        user_data = np.zeros(len(self.project_data['column_name']))
        user_data[0] = fixed_acidity
        user_data[1] = volatile_acidity 
        user_data[2] = citric_acid 
        user_data[3] = residual_sugar 
        user_data[4] = chlorides 
        user_data[5] = free_sulfur_dioxide 
        user_data[6] = total_sulfur_dioxide 
        user_data[7] = density
        user_data[8] = pH 
        user_data[9] = sulphates 
        user_data[10] = alcohol 
        
        input_data = np.asarray(user_data)
        input_data_reshaped = input_data.reshape(1,-1)
        
        return self.model.predict(input_data_reshaped)[0]
        
    
        