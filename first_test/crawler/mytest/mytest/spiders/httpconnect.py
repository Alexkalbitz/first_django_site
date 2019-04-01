import requests

def send_data(my_json):
    #password for views.py verification
    password = '123456'
    #URL to send data to (called in views.py for Database entry)
    URL = "http://127.0.0.1:8000/crawler/"

    with requests.session() as s:
        s.get(URL)
        csrftoken = s.cookies.get_dict()['csrftoken']
        s.headers['X-CSRFToken'] = csrftoken
        payload={
            "data" : my_json,
            "password" : password,
        }
        s.post(URL, data=payload)
