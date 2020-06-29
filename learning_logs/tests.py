from django.test import TestCase
import requests
# Create your tests here.
def add():
    url = 'http://127.0.0.1:8000/hd/'
    data = '{"user_id": "2","user_name": "hgd", "password": "111111", "status": "1"}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        'Spam': 'Eggs'}
    res = requests.post(url, data=data, headers=headers)

add()