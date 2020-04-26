from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from .pusher import pusher_client


main = Blueprint("main", __name__)


@main.route("/")
def index():
    pusher_client.trigger("my-channel", "my-event", {"message": "hello world"})
    return render_template("index.html")


@main.route("/profile")
@login_required
def profile():
    return render_template("profile.html", name=current_user.name)
