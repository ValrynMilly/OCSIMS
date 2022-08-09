from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
#from project import users_db, Hatfield_db, Dordon_db, Andover_db, Erith_db, Purfleet_db, Avonmouth_db, Bicester_db, create_app, models    
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/db.sqlite'
    app.config['SQLALCHEMY_BINDS'] = {'Users_db' : 'sqlite:///databases/Users_db.sqlite',
    'Hatfield_db' : 'sqlite:///databases/Hatfield_db.sqlite',
    'Dordon_db' : 'sqlite:///databases/Dordon_db.sqlite',
    'Andover_db' : 'sqlite:///databases/Andover_db.sqlite',
    'Erith_db' : 'sqlite:///databases/Erith_db.sqlite',
    'Purfleet_db' : 'sqlite:///databases/Purfleet_db.sqlite',
    'Avonmouth_db' : 'sqlite:///databases/Avonmouth_db.sqlite',
    'Bicester_db' : 'sqlite:///databases/Bicester_db.sqlite'}
    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models.user_models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    return app