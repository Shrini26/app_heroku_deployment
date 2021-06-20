from flask import Flask

app1=Flask(__name__)

@app1.route('/',methods=['GET'])
def index():
    return "<h1> this is a flask application </h1>"

if __name__=="__main__":
    app1.run()