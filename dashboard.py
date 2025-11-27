import os, json
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder="templates")
DATA_DIR = os.path.join(os.path.dirname(__file__), "data", "backups")

@app.route("/")
def index():
    files = []
    if os.path.exists(DATA_DIR):
        for fn in os.listdir(DATA_DIR):
            if fn.endswith(".json"):
                path = os.path.join(DATA_DIR, fn)
                try:
                    data = json.load(open(path,"r",encoding="utf-8"))
                except:
                    data = {}
                files.append(data)
    return render_template("index.html", guilds=files)

@app.route("/backup/<fn>")
def backup_file(fn):
    return send_from_directory(DATA_DIR, fn)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
