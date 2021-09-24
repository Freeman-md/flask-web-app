from flask import Blueprint, render_template
# Blueprint splits up application into multiple files that perform specific actions

views = Blueprint('views', __name__)

@views.route('/') # Decorator
def home(): 
  return render_template('home.html')