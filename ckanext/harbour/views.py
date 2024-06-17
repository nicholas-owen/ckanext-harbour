from flask import Blueprint


harbour = Blueprint(
    "harbour", __name__)


def page():
    return "Hello, harbour!"


harbour.add_url_rule(
    "/harbour/page", view_func=page)


def get_blueprints():
    return [harbour]
