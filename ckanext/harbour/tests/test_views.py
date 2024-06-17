"""Tests for views.py."""

import pytest

import ckanext.harbour.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "harbour")
@pytest.mark.usefixtures("with_plugins")
def test_harbour_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("harbour.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, harbour!"
