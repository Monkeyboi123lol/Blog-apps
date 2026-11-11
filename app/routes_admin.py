from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models import db
from app.models import Content    
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
    all_contents = Content.query.order_by(Content.created_at.desc())
    return render_template('Admin.html', contents=all_contents)

@admin_bp.route('/create', methods=['POST'])
def create():
    if not session.get('logged_in'):
        flash('Please log in to access the admin dashboard', 'error')
        return redirect(url_for('admin.login'))
    new_item = Content(
        title = request.form.get('title'),
        slug = request.form.get('slug').strip().replace(' ', '-'),
        description = request.form.get('description'),
        image_url = request.form.get('image_url'),
        status = request.form.get('status')
    )
    db.session.add(new_item)
    db.session.commit()
    flash('Content created successfully!', 'success')
    return redirect(url_for('admin.dashboard'))
@admin_bp.route('/update-status/<int:item_id>/<string:new_status>')
def update_status(item_id, new_status):
    if not session.get('logged_in'):
        flash('Please log in to access the admin dashboard', 'error')
        return redirect(url_for('admin.login'))
    item = Content.query.get_or_404(item_id)
    item.status = new_status
    db.session.commit()
    flash(f'Status updated to {new_status} for item {item.title}', 'success')
    return redirect(url_for('admin.dashboard'))
@admin_bp.route('/delete/<int:item_id>')
def delete(item_id):
    if not session.get('logged_in'):
        flash('Please log in to access the admin dashboard', 'error')
        return redirect(url_for('admin.login'))
    item = Content.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash(f'Item {item.title} deleted successfully!', 'success')
    return redirect(url_for('admin.dashboard'))