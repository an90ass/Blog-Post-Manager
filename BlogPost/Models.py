from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,login_user,LoginManager,login_required,logout_user,current_user

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view='login'
@login_manager.user_loader
def load_user(user_id):
     return Users.query.get(int(user_id))

class Users(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    favorite_color = db.Column(db.String(120))
    about_author =  db.Column(db.Text(500),nullable=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    profile_pic = db.Column(db.Text(500), nullable=True)

    # Do some password stuff!
    password_hash = db.Column(db.String(512))
    # User Can have many posts
    posts = db.relationship('Posts',backref='poster', cascade="all, delete-orphan")

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute!')
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    # Creat A String 
    def __repr__(self):
        return '<name %r>' % self.user_name
    
# Create Blog Post model 
class Posts(db.Model):
        id = db.Column(db.Integer,primary_key = True)
        title = db.Column(db.String(255))
        content = db.Column(db.Text)
        # author = db.Column(db.String(255))
        date_posted = db.Column(db.DateTime, default=datetime.utcnow)  # Corrected typo here
        slug = db.Column(db.String(255))
        # Foreign Key to link Users (refer to the primary key of the user)
        poster_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    

