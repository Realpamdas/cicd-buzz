import os
from flask import Flask, render_template
from buzz import generator

app = Flask(__name__)


@app.route("/")
def generate_buzz():
    page = render_template('home.html')
    page += generator.generate_buzz()
    return page

#def generate_buzz():
#    page = '<html><body background="{{ url(NaturePatterns08.jpg) }}"><h1>'
#    page += generator.generate_buzz()
#    page += '</h1></body></html>'
#    return page


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))