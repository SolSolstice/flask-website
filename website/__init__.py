# set up flask application 

from flask import Flask


# used to initialize flask 
def create_app():
    app = Flask(__name__) #name is the name of the file.. 
    app.config['SECRET_KEY'] = 'Last Chance to Evacuate Planet Earth'

    from .views import views
    from .aboutMe import aboutMe
    from .projects import projects
    from .yahtzee import yahtzee 
    

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(aboutMe, url_prefix='/')
    app.register_blueprint(projects, url_prefix='/')
    app.register_blueprint(yahtzee, url_prefix='/')


    
    return app





