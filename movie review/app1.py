# -*- coding: utf-8 -*-
from flask import Flask, request, render_template

import re
import requests
import json

app = Flask(__name__)

def check(output):
    url = "https://japerk-text-processing.p.rapidapi.com/sentiment/"
    payload = {"text": output}
    print (payload)
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-key': "cacdd5537cmsh3a068dea4423103p117046jsn9c12a735a265",
        'x-rapidapi-host': "japerk-text-processing.p.rapidapi.com"    
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    value = response.text
    output = json.loads(value)
    return response.json()

@ app.route('/')
def summarizer():
    return render_template('summarizer.html')

@app.route('/summarize', methods = ['POST'])
def summarize():
    output = request.form['output']
    output = re.sub("[^a-zA-Z.,]"," ",output)
    print(output)
    essay = check(output)
    print(type(essay['label']))
    if essay['label'] == "pos":
        output="Positive review"
    elif essay['label'] == "neg":
        output="Negative review"
    else:
        output = "Neutral Review"
        
    return render_template('summary.html',essay=essay, prediction_text='{}'.format(output))
    
if __name__ == "__main__":
    app.run(debug = True)
    
    
    
    
    
    