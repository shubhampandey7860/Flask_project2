from flask import *
from flask_wtf import Form
from wtforms import StringField,SubmitField

app = Flask(__name__)
app.config['SECRET_KEY']='csrf_token'

class NameForm(Form):
    name = StringField()
    submit = SubmitField()
    
@app.route('/flaskwtform',methods=['GET','POST'])
def flaskwtform():
    form = NameForm()
    if request.method=='POST':
        fd = NameForm(request.form)
        if fd.validate():
            return fd.name.data
    return render_template('flaskwtform.html',form=form)    
        
            


if __name__=='__main__':
    app.run(debug=True)
    
