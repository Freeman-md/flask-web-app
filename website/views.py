from flask import Blueprint # splits up application into multiple files that perform specific actions

views = Blueprint('views', __name__)

@views.route('/') # Decorator
def home(): 
  return '<h1>Test</h1>'