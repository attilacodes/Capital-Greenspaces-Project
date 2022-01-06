from flask import Blueprint, render_template

views = Blueprint('views', __name__)

team = Blueprint('team', __name__)

@views.route('/')
def home():
    return render_template('homepage_ARQI2.html')
    
@team.route('/aboutus')
def aboutus():
    return render_template('about_us.html')
