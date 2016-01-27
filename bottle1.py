from bottle import route, run, template
from thismysql import getGlossory

@route('/hello/<name>')
def index(name):
    meaning=getGlossory(name)
    return template('<b>Hello {{name}} <br> Welcome to my world</b>!', name=meaning)

run(host='localhost', port=8080)
 
