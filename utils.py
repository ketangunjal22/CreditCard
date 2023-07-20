from code import *
import pickle
import json
import os
import numpy as np
import pandas as pd

class Insurance:
    def load_model(self):
        with open(r"artifacts\model.pkl",'rb')as f:
            self.model = pickle.load(f)

        with open(r"artifacts\jason_data.json", 'r') as f:
            self.json_data = json.load(f)

    def prediction(self,age,job,marital,education,default,balance,housing,loan,contact,day,month,duration,campaign,pdays,previous,poutcome):
        try:
            self.age = age
            self.job = job
            self.marital = marital
            self.education = education
            self.default=default
            self.balance=balance
            self.housing=housing
            self.loan=loan
            self.contact=contact
            self.day=day
            self.month=month
            self.duration=duration
            self.campaign=campaign
            self.pdays=pdays
            self.previous=previous
            self.poutcome=poutcome


            test = np.zeros(38, dtype = int)
            test[0] = self.age
            test[self.json_data['columns'].index('job_'+ self.job)] = 1
            test[self.json_data['columns'].index('marital_'+ self.marital)] = 1
            test[1] = self.json_data['education'][self.education]
            test[2] = self.json_data['default'][self.default]
            test[3] = self.balance
            test[4] = self.json_data['housing'][self.housing]
            test[5] = self.json_data['loan'][self.loan]
            test[6] = self.json_data['contact'][self.contact]
            test[7] = self.day
            test[self.json_data['columns'].index('month_'+ self.month)] = 1
            test[9] = self.duration
            test[10] = self.campaign
            test[11] = self.pdays
            test[12] = self.previous
            print(test)
            return self.model.predict(test)[0]
        except:
            return 'Error in Prediction!'
    
