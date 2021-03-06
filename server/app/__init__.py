from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app=Flask(__name__,static_folder='/home/shri/tangle/client/dist',static_url_path='/home/shri/tangle/client/dist',template_folder='../../client')
app.config['STATIC_FOLDER']='/home/shri/tangle/client/images'
app.config.from_pyfile('/home/shri/tangle/config.py')
login_manager = LoginManager(app)
login_manager.init_app(app)
# URI for database
app.config['SQLALCHEMY_DATABASE_URI']='mysql://user:backspace2;@localhost/tangle'
# SQLAlchemy object intiation
db=SQLAlchemy(app)
db.init_app(app)
db.create_all()
migrate = Migrate(app, db)
from app import models
from .models import User
# login Blueprint
from .login import login as login_blueprint
app.register_blueprint(login_blueprint)
# signin Blueprint
from .signin import signin as signin_blueprint
app.register_blueprint(signin_blueprint)
#route to '/'
@app.route('/',methods=['GET','POST'])
def data():
    
    return render_template('home.html')

# route to signin
