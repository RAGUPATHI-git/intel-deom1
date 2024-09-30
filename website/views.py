from flask import Blueprint,render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')


@views.route('/landing-page')
def landing_page():
    return render_template('landing_page.html')


@views.route('/selection')
def selection():
    return render_template('third_page.html')