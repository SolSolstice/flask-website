# set up flask application 

from flask import Flask


# used to initialize flask 
def create_app():
    app = Flask(__name__) #name is the name of the file.. 
    app.config['SECRET_KEY'] = 'Last Chance to Evacuate Planet Earth'

    from .views import views
    from .auth import auth 

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    
    return app





