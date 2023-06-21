
from flask import Blueprint
from flask import render_template

projects = Blueprint('projects', __name__) 


@projects.route('/projects/')
def home():
    return render_template("projects.html")