from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models import db
admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('admin_login.html')