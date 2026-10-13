from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models import db
admin_bp = Blueprint('admin', __name__)

ADMIN_USER = 'admin'
ADMIN_PASS = 'admin'

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == ADMIN_USER and password == ADMIN_PASS:
            session['logged_in'] = True
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid credentials', 'error')
        if session.get('logged_in'):
            return redirect(url_for('admin.dashboard'))

    return render_template('admin_login.html')

@admin_bp.route('/')
def dashboard():
    if not session.get('logged_in'):
        flash('Please log in to access the admin dashboard', 'error')
        return redirect(url_for('admin.login'))
    return render_template('Admin.html')