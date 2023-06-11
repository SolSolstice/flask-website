# 1st - store the standard root for users to land on 

from flask import Blueprint
from flask import render_template

views = Blueprint('views', __name__) 


@views.route('/')
def home():
    return render_template("home.html")

@views.route('/yahtzee/')
def yahtzee():
    return render_template("yahtzee.html",boolean=True)