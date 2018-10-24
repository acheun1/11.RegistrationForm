#Assignment: Registration Form
#2018 10 06
#Cheung Anthony

# Create a simple registration page with the following fields:

# email
# first_name
# last_name
# password
# confirm_password
# Here are the validations you must include:

# All fields are required and must not be blank
# First and Last Name cannot contain any numbers
# Password should be more than 8 characters
# Email should be a valid email
# Password and Password Confirmation should match
# When the form is submitted, make sure the user submits appropriate information. If the user did not submit appropriate information, return the error(s) above the form that asks the user to correct the information. 

from flask import Flask, render_template, redirect, request, session,flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key='as43df46asd3f4as4'

#our index route will handle the form
@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

#route to handle form submission that calls HTTP allowed for this route
@app.route('/submitted', methods=['POST'])
def submitted():
    q0_str=str(request.form['q0'])
    q1_str=str(request.form['q1'])
    q2_str=str(request.form['q2'])
    q3_str=str(request.form['q3'])
    q3_len=len(request.form['q3'])
    q4_str=str(request.form['q4'])
    if q3_str.islower():
        cap=1
    else:
        cap=0
    if str.isalpha(request.form['q3']):  
        num=1
    else:
        num=0
    cnt=cap+num
    if not q0_str.strip():
        flash("Please provide email to complete registration",'email')
    elif q0_str.strip() and not EMAIL_REGEX.match(request.form['q0']):
        flash("Please provide a valid email to complete registration",'email')
    if not q1_str.strip():
        flash("Please provide your First Name to complete registration",'first')
    if not q2_str.strip():
        flash("Please provide your Last Name to complete registration",'last')
    if not q3_str.strip():
        flash("Please provide a password to complete registration",'password_01')
    elif not q3_str.strip() and q3_len<8:
        flash("The password must be 8 characters to complete registration",'password_01')
    elif q3_str.strip() and cnt>0:        
        flash("Please provide a password that has at least 1 uppercase letter and 1 numeric value to complete registration",'password_01')
    if not q4_str.strip() :
        flash("Please provide a confirmation password to complete registration",'password_02')
    if q3_str.strip() and q4_str.strip() and q3_str != q4_str:
        flash("Password and confirmation password do not match. Please to complete registration",'password_01')

    if '_flashes' in session.keys():
        return redirect("/")

    else:
        print(q3_str.islower())
        print(str.isalpha(request.form['q3']))
        print(cnt)
        return render_template('submitted.html')

if __name__=="__main__":
    app.run(debug=True)

