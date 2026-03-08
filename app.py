from flask import Flask, render_template, request, redirect, url_for
from models import create_player, list_players, get_player, update_player, delete_player
from db import init_db

app = Flask(__name__)

# initialize database when module is imported (older Flask versions may not have
# before_first_request decorator)
init_db()

@app.route("/")
def index():
    players = list_players()
    return render_template("list.html", players=players)

@app.route("/player/new", methods=["GET", "POST"])
def new_player():
    if request.method == "POST":
        create_player(
            request.form["name"],
            level=int(request.form["level"]),
            score=int(request.form["score"]),
        )
        return redirect(url_for("index"))
    return render_template("form.html", player=None)

@app.route("/player/<int:pid>/edit", methods=["GET", "POST"])
def edit_player(pid):
    player = get_player(pid)
    if not player:
        return "Not found", 404
    if request.method == "POST":
        update_player(
            pid,
            name=request.form["name"],
            level=int(request.form["level"]),
            score=int(request.form["score"]),
        )
        return redirect(url_for("index"))
    return render_template("form.html", player=player)

@app.route("/player/<int:pid>/delete", methods=["POST"])
def remove_player(pid):
    delete_player(pid)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
