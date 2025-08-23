from flask import Flask, render_template
from livereload import Server

app = Flask(__name__)
app.debug = True  # Required for template changes to reload


@app.route("/")
def hello_world():
    return render_template('index.html')


if __name__ == "__main__":
    server = Server(app.wsgi_app)

    # 👇 Watch templates and static files for changes
    server.watch('templates/*.html')
    server.watch('static/**/*.css')
    server.watch('static/**/*.js')

    # 👇 Start livereload server on http://localhost:5500
    server.serve(port=5500, debug=True)
