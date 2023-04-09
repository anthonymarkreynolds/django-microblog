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

In this project, I learned about various Django concepts, including:

- How to use the built-in authentication and authorization functionality to secure parts of the app
- How to use Django's form classes to handle user input and validation
- URL routing using `urls.py`
- Views and generic views
- Templates and template tags
- Bootstrap 5 Intergration
- Models and database interactions
- `__init__.py` and package management
- `reverse` and `reverse_lazy`
- Caching using Django's cache framework

### Third-Party Libraries

- How to use third-party libraries like `markdown` to add functionality to the app
- How to install and manage dependencies using `pip` and `requirements.txt`

Through this project, I gained a better understanding of how Django handles requests, renders responses, and interacts with databases. I also learned how to implement caching in a Django application, which can significantly improve the application's performance.

Overall, this project was a great opportunity to learn and practice Django concepts and develop a functional microblog application.

## License

This app is licensed under the MIT License. See `LICENSE` for more information.
