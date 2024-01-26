# flask-blog

This is a simple Flask project that implements a blog application with user registration, login, logout, and CRUD operations for blog posts. The project utilizes various Flask extensions such as Flask-Security and Flask-Admin to handle user authentication, authorization, and administrative tasks.

## Features

- User Registration: Users can create an account by providing their email address and password.
- User Login and Logout: Registered users can log in to access their account and log out when they are done.
- User Roles and Permissions: Users are assigned roles that determine their permissions within the application. The available roles are:
  - Admin: Users with the admin role have elevated privileges. They can edit normal users' posts and access the admin panel created by Flask-Admin.
  - Normal User: Users with the normal user role can create, read, update, and delete their own blog posts.
- CRUD Operations on Posts: Registered users can create new blog posts, view existing posts, update their own posts, and delete their own posts.

## Installation

To run the Flask blog project, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/ata-the-legend/flask-blog.git
2. Change into the project directory:

   ```
   cd flask-blog
3. Create a virtual environment (optional but recommended):

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install the project dependencies:
    ```
    pip install -r requirements.txt
5. Set up the database:
    ```
    flask db migrate
    flask db upgrade
6. Create an admin user with the management command:
    ```
    flask users create-admin USERNAME EMAIL PASSWORD
    ```
    This command will prompt you to enter an email address and password for the admin user.

7. Start the development server:
    ```
    python3 run.py
    ```
    The Flask development server will be accessible at http://localhost:5000.

## Usage

Open your web browser and navigate to http://localhost:5000.

Register a new user account by clicking on the "Register" link.

Log in with your registered email address and password.

Once logged in, you can:
- Create a new blog post by clicking on the "New Post" link.
- View your all posts on home page.
- Update or delete your posts by clicking on the respective   links on the post page.

If you have an admin role, you can:
- Edit normal users' posts by navigating to their post page and clicking on the "update" link.
- Access the admin panel by navigating to http://localhost:5000/admin. Use your admin credentials to log in.
- Create new roles by navigating to the admin panel, selecting the "Roles" section, and clicking on the "Create Role" button.

## Contributing

If you would like to contribute to this Flask blog project, please follow these steps:

- Fork the repository on GitHub.
- Clone your forked repository to your local machine.
- Create a new branch for your changes.
- Make your modifications and commit them.
- Push your changes to your forked repository.
- Submit a pull request to the original repository.

## License

This project is licensed under the MIT license.
## Acknowledgements

Flask: https://flask.palletsprojects.com/
Flask-Security: https://flask-security-too.readthedocs.io/
Flask-Admin: https://flask-admin.readthedocs.io/

