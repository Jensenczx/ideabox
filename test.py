__author__ = 'chenjensen'
from  flask import  Flask, render_template,request
app = Flask(__name__)
idealist = []
idea ={}
classlist =[]
@app.route('/')
def index():
    return render_template('index.html',idealist=idealist)
@app.route('/test')
def content():
    id = request.args.get('id', '')
    return render_template('content.html')
@app.route('/:id',methods=['GET','POST'])
def ideabag():
    if request.methond == 'POST':
        return
    else:
        return render_template('ideabag.html')
@app.route('/:id')
def ideaclass():
    return render_template('content.html',)
if __name__ == '__main__':
    app.run()