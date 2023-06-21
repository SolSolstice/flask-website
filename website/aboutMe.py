
from flask import Blueprint
from flask import render_template

aboutMe = Blueprint('aboutMe', __name__) 


@aboutMe.route('/aboutMe/')
def home():
    return render_template("aboutMe.html")