from flask import Flask, request
from pymongo import MongoClient
from passlib.hash import pbkdf2_sha256
import argparse


app = Flask(__name__)
client = MongoClient("mongodb+srv://new-user1:1234@cluster0.cocbi8g.mongodb.net/?retryWrites=true&w=majority")
#create schema
db = client.mylist
# print("TEST2")


@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return "Hello"
    elif request.method == 'POST':
        return "Hi"


@app.route("/register", methods = ['GET', ' POST'])
def register():
    if request.method == 'GET':
        #create schema
        users = db.users
        username = request.args.get('username')
        email = request.args.get('email')
        password = request.args.get('password')
        password_hash = pbkdf2_sha256.hash("password")
        print(username)
        users.insert_one({
        "username" : username,
        "email" : email,
        "password" : password_hash
        })
        return "Hello"
    
    elif request.method == 'POST':
        #create schema
        users = db.users
        username = request.form('username')
        email = request.form('email')
        password = request.form('password')
        password_hash = pbkdf2_sha256.hash("password")
        print(username)
        users.insert_one({
        "username" : username,
        "email" : email,
        "password" : password_hash
        })
        return "Hi"


# 인자값을 받으 수 있는 인스턴스 생성
parser = argparse.ArgumentParser(description = '사용법 테스트입니다.')


if __name__ == '__main__':
    # print("TEST1")
    app.run(debug=True , port=8000)

