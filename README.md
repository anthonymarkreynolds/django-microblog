# Django Microblog

This is a sample microblog app built with Django, designed to help me learn more about the framework and its features.

## Features

The project includes the following features:

- [x] accounts: This app would handle user authentication and registration, as well as user profiles and settings.
- [x] posts: This app would handle creating and displaying posts, as well as commenting and liking posts.
    - [x] Markdown support for post and comment text
- notifications: This app would handle sending notifications to users when they receive new followers, comments, or likes.
- search: This app would handle searching for posts and users within the microblog.
- hashtags: This app would handle parsing hashtags in posts and allowing users to search for posts by hashtag.
- api: This app would provide an API for other developers to build apps that interact with the microblog.

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
- How to add authentication and authorization to views using Django's `login_required` decorator and `UserPassesTestMixin`.
- How to handle user-specific data with mixins like `LoginRequiredMixin` and `UserPassesTestMixin`.
- How to use Django's form classes to handle user input and validation
- URL routing using `urls.py`
- How to use Django's built-in class-based views such as `ListView`, `DetailView`, `CreateView`, `UpdateView`, and `DeleteView`.
- How to use Django's template tags such as `{% url %}`, `{% csrf_token %}`, and `{% if %}`.
- How to create and use Django forms to handle user input.
- How to create custom template filters
- How to use Bootstrap 5 to style Django templates.
- Models and database interactions
- How to organize code in Django apps and use `__init__.py` files to make code more modular.
- How to use Django's `reverse` and `reverse_lazy` functions to generate URLs dynamically.
- How to use caching to speed up website performance.

### Third-Party Libraries

- How to use third-party libraries like `markdown` to add functionality to the app
- How to install and manage dependencies using `pip` and `requirements.txt`

Through this project, I gained a better understanding of how Django handles requests, renders responses, and interacts with databases. I also learned how to implement caching in a Django application, which can significantly improve the application's performance.

Overall, this project was a great opportunity to learn and practice Django concepts and develop a functional microblog application.

## License

This app is licensed under the MIT License. See `LICENSE` for more information.
