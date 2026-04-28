from flask import Flask, render_template

from controllers.app_controller import get_transmissions_schedule

app = Flask(__name__)


@app.route("/")
def hello_world():
    schedule = get_transmissions_schedule()
    print(schedule)
    return render_template("index.html")
