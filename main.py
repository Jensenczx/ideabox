__author__ = 'chenjensen'
import mysql.connector
from dbtest import dbhelper
from  flask import  Flask, render_template,request
app = Flask(__name__)
@app.route('/')
def index():
    helper = dbhelper()
    idealist=helper.getidea()
    return render_template('index.html',idealist=idealist)
@app.route('/<word>')
def bag(word):
    if word == 'ideabag':
        return render_template('ideabag.html')
    else:
        helper = dbhelper()
        ideainfo = helper.getoneidea(word)
        return render_template('content.html',ideainfo=ideainfo)
if __name__ == '__main__':
    app.run()