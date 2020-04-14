import json
import requests
from faker import Faker
import random

with open('config.txt') as file:
    config = json.load(file)

number_of_users = config.get('number_of_users')
max_posts_per_user = config.get('max_posts_per_user')
max_likes_per_user = config.get('max_likes_per_user')

reg_url = 'http://localhost/api/v1/rest-auth/registration/'
post_url = 'http://localhost/api/v1/post/'
like_url = 'http://localhost/api/v1/like/'
users = []
fake = Faker()

for i in range(number_of_users):
    while True:
        email = fake.email()
        password = fake.password()
        name = fake.first_name()
        payload = {
            "username": name,
            "email": email,
            "password1": password,
            "password2": password
        }
        request = requests.post(reg_url, json=payload)
        if request.status_code==201:
            token = request.json().get('token')
            pk = request.json().get('user').get('pk')
            user = {'email': email, 'name': name, 'password': password, 'token': token}
            users.append({'pk': pk, 'email': email, 'name': name, 'password': password, 'token': token})
            break

for user in users:
    post_num = random.randint(0, max_posts_per_user)
    token = user.get('token')
    headers = {'Authorization': 'JWT {}'.format(token)}
    for _ in range(post_num):
        title = fake.word()
        body = fake.text()
        payload = {
            "title": title,
            "body": body,
        }
        request = requests.post(post_url, json=payload, headers=headers)

posts = requests.get(post_url).json()
for user in users:
    like_num = random.randint(0, max_likes_per_user)
    token = user.get('token')
    headers = {'Authorization': 'JWT {}'.format(token)}
    for _ in range(like_num):
        post = random.choice(posts).get('id')
        like = random.choice([True, False])
        payload = {
            "post": post,
            "like": like,
        }
        request = requests.post(like_url, json=payload, headers=headers)
