"""
https://flask.palletsprojects.com/en/2.0.x/quickstart/
En modo debug, el servidor se actualiza al cambiar el archivo,
sin necesidad de reiniciar app
> $env:FLASK_ENV = "development"
> flask run

Flask templates:
https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates

favicon:
https://flask.palletsprojects.com/en/1.1.x/patterns/favicon/
"""

from flask import Flask, render_template

app = Flask(__name__)

"""
esto hace que cada vez q se busque la ruta home,
se ejecute este codigo
"""

# responder al request de una direccion, enviando texto.
# en las herramientas del navegador podemos ver que en un momento, se genera
# automaticamente un archivo .html, y este texto se pone en el body del archivo
@app.route("/")
def hello_world():
    return "<p>Hello, asd!</p>"


@app.route("/pag1")
def pag1():
    return "prueba pagina 1"


@app.route("/pag1/dentro")
def pagInterna():
    return "prueba pagina interna"

# responder al request enviando un archivo .html
# para esta funcion, los hhtml deben estar dentro de una carpeta "templates"
@app.route("/temp")
def temp():
    return render_template("index.html")

# responder al request enviando un archivo estatico (CSS o JS)
# para esta funcion, los hhtml deben estar dentro de una carpeta "static"


# variables, ver el link para ver los distintos reglamentos
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
@app.route("/<username>")
def helloUser(username="default_user"):
    return render_template("index.html", name=username)
