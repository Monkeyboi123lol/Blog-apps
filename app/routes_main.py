from flask import Blueprint, render_template, request, redirect, url_for, session,flash
main_bp = Blueprint('main', __name__)
from app.models import User
from app import db

# Main page
@main_bp.route('/')
def index():
    return render_template('index.html')

# signup page
@main_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Here you would typically add code to save the user to the database
        # For example:
        # new_user = User(username=username, email=email, password=password)
        # db.session.add(new_user)
        # db.session.commit()
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash('Username or email already exists. Please choose a different one.', 'error')
            return redirect(('main.signup'))
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('main.login'))
    return render_template('sign-up.html')

# login page
@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user=User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            flash('Logged in successfully!', 'success')
            return redirect(url_for('main.index'))
        flash('Invalid username or password. Please try again.')

        
    return render_template('log-in.html')