from utils import Insurance
import json
from flask import Flask, jsonify, render_template, url_for, request

app = Flask(__name__)

@app.route('/testing')
def welcome():
    return 'Hello World!!'

@app.route('/predict', methods = ["GET"])
def get_prediction():
    try:
        age = int(request.args.get('age'))
        job = object(request.args.get('job'))
        marital = object(request.args.get('marital'))
        education = object(request.args.get('education'))
        default = object(request.args.get('default'))
        balance = int(request.args.get('balance'))
        housing = object(request.args.get('housing'))
        loan = object(request.args.get('loan'))
        contact = object(request.args.get('contact'))
        day = int(request.args.get('day'))
        month = object(request.args.get('month'))
        duration  = int(request.args.get('duration'))
        campaign = int(request.args.get('campaign'))
        pdays = int(request.args.get('pdays'))
        previous = int(request.args.get('previous'))
        poutcome = object(request.args.get('poutcome'))

        obj = Insurance()
        answer = obj.prediction([age, job,marital,education,default,balance,housing,loan,contact,day,month,duration,campaign,pdays,previous,poutcome].to_numpy())
        return answer
    
    except Exception as e:
        # Handle the exception
        return str(e)
    

if __name__ == '__main__':
    app.run()