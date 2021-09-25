from flask import Blueprint, render_template
# Blueprint splits up application into multiple files that perform specific actions
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/') # Decorator
@login_required
def home(): 
  return render_template('home.html', user=current_user)