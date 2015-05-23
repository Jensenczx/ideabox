__author__ = 'chenjensen'
from  flask import  Flask, render_template,request
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def regist():
    if request.method == 'POST':
        return '<h>register success</h>'
    else:
        return render_template('index.html')
if __name__ == '__main__':
    app.run()