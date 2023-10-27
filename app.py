from flask import Flask
import argparse

app = Flask(__name__)

# print("TEST2")

parser = argparse.ArgumentParser()
parser.add_argument("-he", "--hello", dest="hello", action="store")   
args = parser.parse_args()

@app.route('/', methods=['GET', 'POST'])
def main():
    if args.hello == '1':
        return 'Hello World'
    else:
        return 'Hangilecho "# web_server" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/gogiri/web_server.git
git push -u origin main World'

if __name__ == '__main__':
    print('TEST1')
    app.run(port=8000)

