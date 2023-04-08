# Django Microblog

This is a sample microblog app built with Django, designed to help me learn more about the framework and its features.

## Features

The app includes the following features:

- User authentication and authorization
- Posting and displaying short messages
- Commenting and liking posts
- Markdown support for post and comment text

## Requirements

To run this app, you will need:

- Python 3.10 or later
- Other dependencies listed in `requirements.txt`

## Installation

To install the app, follow these steps:

1. Clone the repository: `git clone https://github.com/yourusername/django-microblog.git`
2. Create a virtual environment: `python -m venv env`
3. Activate the virtual environment: `source env/bin/activate` (or `env\Scripts\activate` on Windows)
4. Install the dependencies: `pip install -r requirements.txt`
5. Set up the database: `python manage.py migrate`
6. Create a superuser: `python manage.py createsuperuser`
7. Run the development server: `python manage.py runserver`

You should now be able to access the app at `http://localhost:8000/`.

## Summary of What I've Learned So Far

### Django Basics

- How to create a new Django project and app
- How to define models and use the ORM to interact with the database
- How to create views and templates to display content to users
- How to use URL routing to map requests to specific views
- How to use the built-in authentication and authorization functionality to secure parts of the app
- How to use Django's form classes to handle user input and validation
- How to use Django's generic views to simplify the development process

### Third-Party Libraries

- How to use third-party libraries like `django-markdownx` to add functionality to the app
- How to install and manage dependencies using `pip` and `requirements.txt`

### Git and Version Control

- How to use Git for version control and collaboration
- How to create and manage branches, commit changes, and push to a remote repository
- How to use Git's merge and pull request functionality to merge changes into the main branch

This is just a high-level summary of what I've learned so far. I've also gained a lot of practical experience working with Django and building a real-world app. I've learned how to break down a project into smaller tasks, how to research and solve problems, and how to work iteratively to improve and refine the app over time.


## License

This app is licensed under the MIT License. See `LICENSE` for more information.
