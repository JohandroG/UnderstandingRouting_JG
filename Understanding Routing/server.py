from os import name
from flask import Flask

app = Flask( __name__ )


@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"

@app.route('/dojo', methods=['GET'])
def dojo():
    return "Dojo!"

@app.route('/say/<name>', methods=['GET'])
def hi(name):
    return f"Hi {name}!" 

@app.route('/repeat/<num>/<word>', methods=['GET'])
def repeat(num,word):
    usedWord = ''
    numbersel = int(num)
    for i in range (1,numbersel+1,1):
        usedWord += f"<h1> {word} <h1/>"
    return usedWord



if __name__ == "__main__":
    app.run( debug = True )



#Base Url: http://127.0.0.1:5000/
