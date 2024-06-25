# Databases.py

from flask import   flash,request
from Models import Users, db,Posts
from werkzeug.security import generate_password_hash,check_password_hash
from werkzeug.utils import secure_filename
import uuid as uuid
import os
# UPLOAD_FOLDER = 'static/images/'

def add_user_to_db(form):
    try:
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            # Hash password
            hashed_psw = generate_password_hash(form.password_hash.data)
            user = Users(
                name = form.name.data,
                user_name=form.user_name.data,
                email=form.email.data,
                favorite_color=form.favorite_color.data,
                password_hash=hashed_psw
            )
            db.session.add(user)
            db.session.commit()
        else:
            flash("User with this email already exists.")
    except Exception as e:
        print(f"Error adding user to database: {e}")
    
def get_all_users():
    return Users.query.order_by(Users.date_added).all()

def get_user_info(id):
    user_info = Users.query.get_or_404(id) 
    return user_info

def update_user_in_db(form,user_info,app):
    user_info.user_name = form.user_name.data
    user_info.name = form.name.data
    user_info.email = form.email.data
    user_info.favorite_color = form.favorite_color.data
    user_info.about_author = form.about_author.data
    user_info.profile_pic = request.files['profile_pic']

    # Grab Image Name
    pic_filename = secure_filename(user_info.profile_pic.filename)
    # Set uuid
    uniqe_pic_name = str(uuid.uuid1()) + "_" + pic_filename
        # Save that image 
    saver =  request.files['profile_pic']
    # change it to a string to save to db
    user_info.profile_pic = uniqe_pic_name
    try:
        saver.save(os.path.join(app.config['UPLOAD_FOLDER'],uniqe_pic_name))
        db.session.commit()
    except Exception as e:
        print(e)
def delete_user_from_db(user_info_to_delete):
    db.session.delete(user_info_to_delete)
    db.session.commit()    

def pw_to_chek_in_db(email):
    user = Users.query.filter_by(email=email).first()
    return user

def add_post(form,poster):
     post = Posts(title = form.title.data,content=form.content.data,poster_id=poster,slug =form.slug.data)
     try:
        # Add post data to the DataBase
        db.session.add(post)
        db.session.commit()
     except Exception as e:
         print(e)
def get_all_posts():
    posts = Posts.query.order_by(Posts.date_posted)
    return posts
def get_post(id):
    try:
         post = Posts.query.get_or_404(id)
    except Exception as e:
          print(e)
    return post

def update_post_in_db(form,post):
    post.title = form.title.data
    post.slug = form.slug.data
    post.content = form.content.data
    # Update db
    db.session.add(post)
    db.session.commit()
def delete_post_from_db(post):
    try:
        db.session.delete(post)
        db.session.commit()
    except Exception as e:
        flash("There was a porblem deleting post !")

def get_user_by_user_name(user_name):
    return Users.query.filter_by(user_name=user_name).first()
    
def all_posts():
    return Posts.query
def searched_posts(posts, search):
    filtered_posts = posts.filter(
        (Posts.title.like('%' + search + '%')) | 
        (Posts.content.like('%' + search + '%')) | 
        (Users.user_name.like('%' + search + '%'))
    ).join(Users).order_by(Posts.title).all()
    return filtered_posts



    


        
            