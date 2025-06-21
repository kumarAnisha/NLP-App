from flask import Flask, render_template,request,session
from db import database
import json
import ner as nf
import language_detection as ld
import sentiment as st
import os

app = Flask(__name__)
dbo=database()

@app.route('/')
def index():
    
    return render_template("login.html")
@app.route('/register')
def register():
    return render_template("register.html")
@app.route('/perform_registration',methods=['POST'])
def perform_registration():
    name=request.form.get('user_name')
    email=request.form.get('user_email')
    password=request.form.get('user_password')
    response=dbo.insert(name,email,password)
    
    return render_template("register.html",message="Email already exists")
    
@app.route('/perform_login',methods=['POST'])
def perform_login():
    email=request.form.get('user_email')
    password=request.form.get('user_password')
    response=dbo.search(email,password)
    if response==0:
        return render_template("login.html",message="wrong email or password")
    else:
         
         return render_template("profile.html")
    
@app.route('/Headline_generation')
def ner_page():
   
        return render_template("ner.html")
        
    
@app.route('/perform_ner',methods=['POST'])
def perform_ner():
   
        text=request.form.get("text")
    

        result =nf.perform_ner_final(text)
    
    
        return render_template("ner.html",result=result)
   
@app.route('/language_detection')
def language_detection():
   
         return render_template("language_detection.html")
    
    
@app.route('/perform_ld',methods=['POST'])
def perform_ld():
 
     text=request.form.get('text')
     result=ld.detect_language(text)
     return render_template('/language_detection.html',result=result)
    
@app.route('/sentiment_analysis')
def sentiment_analysis():
   
        return render_template("sentiment.html")
    
     
@app.route('/perform_sa',methods=['POST'])
def perform_sa():
 
     text=request.form.get('text')
     result=st.detect_sentiment(text)
     return render_template('/sentiment.html',result=result)
   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
