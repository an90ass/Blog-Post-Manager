from flask import Flask, render_template, flash,request,redirect, url_for
from Databases import add_user_to_db, delete_post_from_db, delete_user_from_db, get_all_users, get_all_posts, get_post, get_user_by_user_name, get_user_info, pw_to_chek_in_db, update_post_in_db, update_user_in_db,add_post
from WebForms import LoginForm, NamerForm, PasswordForm, UserForm ,PostForm
from Models import db, migrate, login_manager
from werkzeug.security import check_password_hash
from datetime import date, datetime
from flask_login import UserMixin,login_user,LoginManager,login_required,logout_user,current_user
app = Flask(__name__)
app.config['SECRET_KEY'] = "hi"
# Old SQLITE DB
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# NEW MYSQL DB
#'mysql:///username:password@localhost/db_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://anass:4923an90as@localhost/flask_users'
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

db.init_app(app)  # Initialize the db with the app
migrate.init_app(app,db)  # Initialize the migrate with the app
login_manager.init_app(app)


@app.route('/')
def index():
    flash('Welcome to our website')
    first_name = 'Anas'
    stuff = 'This is the Home Page'
    return render_template('index.html', first_name=first_name, stuff=stuff)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

# Create custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''  # clear it
        flash("Form submitted successfully")
    return render_template("name.html", name=name, form=form)

@app.route('/users/add', methods=['POST', 'GET'])
def add_user():
    form = UserForm()
    name = None
    if form.validate_on_submit():
        add_user_to_db(form)
        flash('User added successfully')
        name = form.name.data
        # print(name)
    form.name.data = ''
    form.user_name.data = ''
    form.email.data = ''
    form.favorite_color.data = ''
    form.password_hash.data = ''
    our_users = get_all_users()
    return render_template("add_user.html", form=form, name=name, our_users=our_users)


@app.route('/update/<int:id>',methods=['GET','POST'])
@login_required
def update_user(id):
    form = UserForm()
    user_info = get_user_info(id)
    print(user_info)
    if request.method =="POST":
        try:
            update_user_in_db(form,user_info)
            # name = form.name.data =''
            flash("User updated successfully")
            return render_template("update_user.html",
                                    form=form,
                                   user_info=user_info,
                                   id=id)
            # our_users = get_all_users()
            # return render_template("add_user.html", form=form, name=name , our_users=our_users)

        except Exception as e:
            flash("Error ! ")
            return render_template("update_user.html",
                                    form=form,
                                   user_info=user_info,
                                   id=id)
    else:
        return render_template("update_user.html",
                                    form=form,
                                   user_info=user_info,
                                   id=id)
@app.route('/delete/<int:id>')
def delete_user(id):
    name = None
    form = UserForm()
    user_info_to_delete = get_user_info(id)
    try:
        delete_user_from_db(user_info_to_delete)
        flash("User deleted successfully")
        our_users = get_all_users()
        return render_template("add_user.html", form=form, name=name, our_users=our_users)
        
    except Exception as e:
        flash("Erorr during deleting user.. Try again")
        return render_template("add_user.html", form=form, name=name, our_users=our_users)
# Create Password Test Page
@app.route('/test_pw', methods=['GET', 'POST'])
def test_pw():
    email = None
    password = None
    checked_pw = None
    passed = None
    form = PasswordForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password_hash.data
        form.email.data = ''
        form.password_hash.data = ''
        checked_pw = pw_to_chek_in_db(email)
        if checked_pw and check_password_hash(checked_pw.password_hash, password):
            passed = True
        else:
            passed = False
            # flash("No user found with that email address or password is incorrect.")

    return render_template("test_pw.html", email=email, password=password, form=form, checked_pw=checked_pw, passed=passed)

# Json Thing 
@app.route('/date')
def get_current_date():
    date_of_today = {
        "Date":date.today(),
        "Time":datetime.now().time().isoformat()
        }
    favorati_food = {
        "Anas":"Pizza",
        "Ahmet":"Rice"
    }

    response = {
        "date":date_of_today,
        "favorati_food":favorati_food
    }
    return response

# Add Post Page
@app.route('/add-post', methods=['GET', 'POST'])
@login_required
def add_post_route():
    form = PostForm()
    if form.validate_on_submit():
        poster = current_user.id
        add_post(form,poster)
        form.title.data = ''
        form.content.data = ''
        form.author.data = ''
        form.slug.data = ''
        flash("Blog Post Submitted Successfully!")
    return render_template("add_post.html", form=form)

@app.route('/posts')
def posts():
    posts = get_all_posts()
    # print(posts)
    return render_template("posts.html",posts=posts)

@app.route('/post/<int:id>')
def post(id):
    post = get_post(id)
    return render_template("post.html", post=post)

@app.route('/posts/edit/<int:id>',methods=['GET','POST'])
@login_required
def update_post(id):
    form = PostForm()
    post = get_post(id)
    if request.method =="POST":
        try:
            update_post_in_db(form,post)
            flash("Post Updated Successfully")
            return redirect(url_for('post', id=post.id))
        except Exception as e:
            print(e)
    form.title.data = post.title
    form.slug.data = post.slug
    form.content.data = post.content
    return render_template("update_post.html",form=form)
        
@app.route('/posts/delete/<int:id>')
def delete_post(id):
    post = get_post(id)
    try:
        delete_post_from_db(post)
        flash("Post Deleted Successfully")
        posts = get_all_posts()
    # print(posts)
        return render_template("posts.html",posts=posts)
    except Exception as e:
        flash("There was a porblem deleting post !")

# Create login page
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    user_name = form.user_name.data
    if form.validate_on_submit():
        user = get_user_by_user_name(user_name)
        if user:
            #   Chek hash
            if check_password_hash(user.password_hash,form.password.data):
                login_user(user)
                flash('Login Successfully !!')
                return redirect(url_for('dashboard'))
            else:
                flash('Wrong password - Try again !!')
        else:
            flash('That user does not exist - Try again !!')
    return render_template("login.html",form=form)

# Create Dashboard page
@app.route('/dashboard',methods=['GET','POST'])
@login_required
def dashboard():
    form = UserForm()
    id = current_user.id
    user_info = get_user_info(id)
    print(user_info)
    if request.method =="POST":
        try:
            update_user_in_db(form,user_info)
            # name = form.name.data =''
            flash("User updated successfully")
            return render_template("dashboard.html",
                                    form=form,
                                   user_info=user_info)
            # our_users = get_all_users()
            # return render_template("add_user.html", form=form, name=name , our_users=our_users)

        except Exception as e:
            flash("Error ! ")
            return render_template("dashboard.html",
                                    form=form,
                                   user_info=user_info)
    else:
        return render_template("dashboard.html",
                                    form=form,
                                   user_info=user_info)
    return render_template("dashboard.html")
    

# Create Logout page
@app.route('/logout',methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    flash('You Have Been Logged Out - Thanks For Stopping By ..!!')
    return redirect(url_for('login'))







if __name__ == '__main__':
    app.run(debug=True)
