

from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
import re

  
app = Flask(__name__)
  
app.secret_key = 'naresh'



@app.route('/')

def homer():
    return render_template('home.html')


@app.route('/login',methods =['GET', 'POST'])
def login():
    
    return render_template('login.html', msg = msg)

        

   
@app.route('/register', methods =['GET', 'POST'])
def registet():
    
    return render_template('register.html', msg = msg)




    
if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8080)