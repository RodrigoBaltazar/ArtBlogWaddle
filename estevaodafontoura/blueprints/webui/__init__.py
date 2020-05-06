from flask import Blueprint

#from .views import index, post
from .views import index

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)
# bp.add_url_rule(
#     "/post/<post_id>", view_func=post endpoint="postview"
# )


def init_app(app):
    app.register_blueprint(bp)