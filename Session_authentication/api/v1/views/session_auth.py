#!/usr/bin/env python3
""" Task 7 - new Flask View """

from api.v1.views import app_views
from api.v1.auth.session_auth import SessionAuth
from api.v1.auth.auth import Auth
from models.user import User
from flask import Flask, jsonify, request, abort
import os

auth = None
auth_type = os.getenv("AUTH_TYPE")

if auth_type == "session_auth":
    auth = SessionAuth()
else:
    auth = Auth()


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def login() -> str:
    """ Task 7 """
    email = request.form.get("email")
    password = request.form.get("password")

    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": email})

    if user == []:
        return jsonify({"error": "no user found for this email"}), 404
    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth

    session_id = auth.create_session(user[0].id)
    user_info = jsonify(user[0].to_json())
    user_info.set_cookie(os.getenv("SESSION_NAME"), session_id)

    return user_info


@app_views.route(
        "/auth_session/logout", methods=["DELETE"], strict_slashes=False)
def logout():
    """ Task 8 - Logout """
    from api.v1.app import auth
    if auth.destroy_session(request) is False:
        abort(404)

    return jsonify({}), 200
