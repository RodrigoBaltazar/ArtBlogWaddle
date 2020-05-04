from flask import abort, render_template
from estevaodafontoura.models import Posts


def index():
    posts = Posts.query.all()
    return render_template("index.html", posts=posts)


def post(post_id):
    post = Post.query.filter_by(id=post_id).first() or abort( #talvez o Post seja Posts nesta linha bem a esquerda
        404, "post nao encontrado"
    )
    return render_template("post.html", post=post)