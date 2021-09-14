from flask import Flask, request
from  cm import Myclass

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

@app.route('/web',methods=['POST'])
def login():
    data = request.get_json(force=True)
    name  = data.get('name')
    id = data.get('id')
    print(name +" "+str(id))

    #obj = Myclass(name,str(id))
    #obj.new_func()
    return {'status':"successful"}

if __name__ == '__main__':
    app.run()
