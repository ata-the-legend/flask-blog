from flask import Flask

from app.users.routes import blueprint as users_blueprint
from app.posts.routes import blueprint as posts_blueprint

def register_blueprints(app):
    app.register_blueprint(users_blueprint)
    app.register_blueprint(posts_blueprint)

app = Flask(__name__)
register_blueprints(app)
app.config.from_object('settings.DevConfig')
