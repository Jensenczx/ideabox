__author__ = 'chenjensen'
import mysql.connector
from  flask import  Flask, render_template,request
from DatabseUtile import DatabaseOperateUtil

app = Flask(__name__)

@app.route('/')
def index():
    operater = DatabaseOperateUtil('root','','IdeaBox','true')
    idealist = operater.getideas()
    return render_template('index.html',idealist=idealist)

@app.route('/idea/<int:idea_code>')
def ideaInfo():
    pass

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')