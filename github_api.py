# TODO make requests to github API
import requests
import logging

def get_github_user(username):
    #When dealing with a function that needs to send data a/ indicate errs, return a tuple of (data and err msg)

    #if things work, return (data, None)

    #if things don't work, there's an err,so return (None. error value/msg)

    try:#example err handling. more things could go wrong
        response = requests.get(f'https://api.github.com/users/{username}')
        #404 - username not found
        if response.status_code == 404: #not found
            return None, f'Username {username} not found'#tuple of data, or in this case (None, and an err string)
        #other error
        response.raise_for_status()#500 err from github, sends to except handler 
        #success/happy path
        response_json = response.json()#need to turn response object into reponse.json object
        user_info = extract_user_info(response_json)
        return user_info, None #return a tuple of (data and err msg, or in this case None)
    except Exception as e:
        logging.exception(e)#deals with a general problem, like connection error
        return None, e, 'Error, connecting to GitHub'#if things don't work, there's an error, return (None. error msg)

def extract_user_info(json_response):#pulling out wanted properties
    return {
        'login': json_response.get('login'),
        'name': json_response.get('name'),
        'avatar_url': json_response.get('avatar_url'),
        'home_page': json_response.get('html_url'),
        'public_repos': json_response.get('public_repos')
    }#string before the : are user created names, string in the () need to match the properties in the json response
