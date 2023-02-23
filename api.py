import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory, jsonify
from pathlib import Path

app = Flask(__name__)
UPLOAD_PASTA = Path(__file__).parent / "pasta_downloads"
CAMINHO_JSON = Path(__file__).parent / "arquivo.json"
app.config["UPLOAD_PASTA"] = UPLOAD_PASTA


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # Verifica se a solicitacao de postagem tem a parte do arquivo
        if "file" not in request.files:
            flash("Nao tem a parte do arquivo")
            return redirect(request.url)
        file = request.files["file"]

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_PASTA"], filename))
            return redirect(url_for("download_file", name=filename))
    return """
    <!doctype html>
    <html>
    <head>
        <title>Upload File</title>
    </head>
    <body>
        <h1>RUBENS's SUPREMACY, futuro INTER</h1>
        <form method="POST" action="" enctype="multipart/form-data">
        <p><input type="file" name="file"></p>
        <p><input type="submit" value="Submit"></p>
        </form>
    </body>
    </html>
        """


@app.route("/uploads/<name>")
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


if __name__ == "__main__":
    app.run(debug=True)
