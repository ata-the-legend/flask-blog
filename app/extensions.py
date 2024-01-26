from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security, current_user
from flask_admin import Admin, AdminIndexView, form
from flask_admin.contrib.sqla import ModelView


db = SQLAlchemy()
migrate = Migrate()
security = Security()
admin = Admin()

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        print(current_user.roles)
        return current_user.has_role('admin')

class MyModelView(ModelView):

    column_display_pk = True 
    column_hide_backrefs = False

    def is_accessible(self):
        return current_user.has_role('admin')
    
    def inaccessible_callback(self, name, **kwargs):
        return super().inaccessible_callback(name, **kwargs)

class PostModelView(MyModelView):
    form_columns = ('title', 'content', 'user_id',)

class UserModelView(MyModelView):
    form_columns = ('username', 'email', 'roles', 'active')