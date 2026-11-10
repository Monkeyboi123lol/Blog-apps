from app import db
from datetime import datetime  
from  werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    """
    a special column in a database table that uniquely identifies each row in the table, ensuring no duplicates exist and no null values. It is used as a primary key for the table, allowing for efficient data retrieval and management.

    Main Rules:
    - No duplicates: Each value in the primary key column must be unique across all rows in the table.
    - No null values: The primary key column cannot contain null values, ensuring that every row can be uniquely identified.
    - One per table: Each table can have only one primary key, which can consist of a single column or a combination of multiple columns (composite primary key).

    Purpose:
    - Fast searching
    - Stops mistakes 
    - Connects tables(links tables, creates relationships, and builds structures )
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

    class Content(db.Model):
        __tablename__ = 'contents'

        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(200), nullable=False)
        slug = db.Column(db.String(200), unique=True, nullable=False)
        description = db.Column(db.Text, nullable=False)
        image_url = db.Column(db.String(500), nullable=True)
        status = db.Column(db.String(20), default='Draft')
        created_at = db.Column(db.DateTime, default=datetime.utcnow)
