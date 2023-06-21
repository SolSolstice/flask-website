from flask import Blueprint
from flask import render_template
from flask import request 

yahtzee = Blueprint('yahtzee', __name__) 


@yahtzee.route('/yahtzee/',methods=['GET','POST'])  # GET request -> retrieving info.. POST request -> updating/creating something // going to url -> GET request.. clicking submit -> POST request
def ytz():
    data = request.form
    print(data)
    return render_template("yahtzee.html",boolean=True)

