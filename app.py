from flask import Flask ,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,EmailField
from wtforms.validators import InputRequired,Length,ValidationError
app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY']='keykey'
db=SQLAlchemy(app)
class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username_or_email=db.Column(db.String(35),nullable=False)
    password=db.Column(db.String(128),nullable=False)
class RegisterFrom(FlaskForm):
    first_name = StringField(validators=[InputRequired(),Length(min=5,max=25)],render_kw={"placeholder":"first_name"})
    last_name = StringField(validators=[InputRequired(),Length(min=5,max=25)],render_kw={"placeholder":"last_name"})
    username_name = StringField(validators=[InputRequired(),Length(min=5,max=25)],render_kw={"placeholder":"username_name"})
    Password=PasswordField(validators=[InputRequired(),Length(min=6,max=20)], render_kw={"placeholder": "password"})
    submit=SubmitField("Register")
    def validate_username(self,username):
        existing_user_username=user.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError("change username in other name")
class login(FlaskForm): 
    username_name = StringField(validators=[InputRequired(),Length(min=5,max=25)],render_kw={"placeholder":"username_name"})
    Password=PasswordField(validators=[InputRequired(),Length(min=6,max=20)], render_kw={"placeholder": "password"})
    submit=SubmitField("login")
@app.route("/")
def home():
    return render_template('home.html')
@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm
    return render_template('login.html',form=form)   
@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
     new_user=User(username_or_email=form.username_name.data,password=form.password.data)
     db.session.add(new_user)
     db.session.commit()
     return redirect(url_for('login'))
    return render_template('register.html',form=form)
@app.route("/about")
def about():
    return render_template("about.html")
if __name__=="__main__":
        app.run(debug=True)