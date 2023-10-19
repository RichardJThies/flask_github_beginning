"""Base of the program, sets up the flask web application and the program"""
from flask import Flask, render_template, request  # NOT the same as requests 
from github_api import get_github_user# call just the one function needed

app = Flask(__name__)

@app.route('/')#/ is the homepage/base directory. Often omitted by browser when on homepage
def homepage():
    return render_template('index.html')#route handler function/view functions always need to return something

@app.route('/get_user')#route handler function/view function. A view is a webpage. Dob't forget the / before get_user
def get_user_info():#flask is unpacking query parameters in url and coverting them into a dictionary
    """get user info from GitHub api, display on new page"""
    print(f'form data is {request.args}')#request is a built in variable from flask, not requests libray. Stores data about the request made by the browser to the server
    #every request made to server, server should always respond. No matter how bad/crash causing/weird/unexpected, the server should respond
    username = request.args.get('username')#classic style, won't error if username data is not provided, instead returns None. Use request.args.get() to read data for each input/field if needed
    # username = request.args('username')#more common style, but does error if no username data is provided
    user_info, error_message = get_github_user(username)#user_info will be dictionary because json data. Request the data from
    if error_message:#sending the error string returned from github_api to new page
        return render_template('error.html', error=error_message)
    else:
        return render_template('github.html',  user_info=user_info)#adding keyword arguments to template. "github_username" is the label/name of the data 

if __name__ == '__main__':
    app.run()