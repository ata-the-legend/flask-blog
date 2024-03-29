from flask import Flask
from flask_security import SQLAlchemyUserDatastore

from app.extensions import db, migrate, security, admin, MyAdminIndexView, MyModelView, PostModelView, UserModelView
from app.users.routes import blueprint as users_blueprint
from app.posts.routes import blueprint as posts_blueprint
from app.users import manage as users_manage #to commands be registerd

def register_blueprints(app):
    app.register_blueprint(users_blueprint)
    app.register_blueprint(posts_blueprint)

def add_view_to_admin_panel(admin):
    admin.add_view(UserModelView(User, db.session))
    admin.add_view(MyModelView(Role, db.session))
    admin.add_view(PostModelView(Post, db.session))

app = Flask(__name__)
register_blueprints(app)
app.config.from_object('settings.DevConfig')

db.init_app(app)

from app.users.models import User, Role # to privent circular_imports for migrate use
from app.posts.models import Post
migrate.init_app(app, db, render_as_batch=True)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security.init_app(app, user_datastore)

admin.init_app(app, index_view=MyAdminIndexView())
add_view_to_admin_panel(admin)