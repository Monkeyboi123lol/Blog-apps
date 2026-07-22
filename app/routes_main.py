from flask import Blueprint, render_template, request, redirect, url_for, session,flash
main_bp = Blueprint('main', __name__)

# Main page
@main_bp.route('/')
def index():
    return render_template('index.html')

# signup page
@main_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('sign-up.html')

# login page
@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('log-in.html')