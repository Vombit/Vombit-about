"""void
"""
import json
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    """simple code with the ability to change data without restarting
    """
    with open('data/desc.json', encoding='utf-8') as f:
        description = json.load(f)
    with open('data/prjct.json', encoding='utf-8') as f:
        projects = json.load(f)

    supported_languages = ["ru", "en"]
    lang = request.accept_languages.best_match(supported_languages)

    project = projects["base"]
    descr = description["base"]
    if lang == "ru":
        project = projects["ru"]
        descr = description["ru"]

    return render_template('index.html', projects=project, description=descr)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')
