import click
from flask.cli import with_appcontext
from flask_security import hash_password, cli

from app.extensions import db, security
from .models import Role


def create_admin_role():
    admin = Role.query.filter(Role.name=='admi').first()
    if not admin:
        admin = Role(name='admi', description='This is a admin user')
        db.session.add(admin)
        db.session.commit()



@cli.users.command("create-admin", )
@click.argument("username")
@click.argument("email")
@click.argument("password")
@with_appcontext
def create_admin_user(username: str, email: str, password: str):
    """Create a admin user by passing the username, email and password"""
    create_admin_role()
    user_email = security.datastore.find_user(email=email)
    user_username = security.datastore.find_user(username=username)
    if user_email or user_username:
        raise click.exceptions.ClickException(message='This email or username has been registerd')
    security.datastore.create_user(
                email=email,
                username=username,
                password=hash_password(password),
                roles=['admin']
            )
    db.session.commit()
    click.echo(f"Admin {username} created")