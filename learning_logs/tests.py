from django.test import TestCase

# Create your tests here.
def add():
    url = 'http://127.0.0.1:8000/tcmanager/add/'
    data = '{"user_id": "1","user_name": "hand", "password": "111111", "status": "1"}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        'Spam': 'Eggs'}
    res = requests.post(url, data=data, headers=headers)
    text = res.text
    print(text)

add()