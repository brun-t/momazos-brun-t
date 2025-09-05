from flask import Flask, render_template
from livereload import Server

"""Esta es la clase Flask que es lo que genera el server"""
app = Flask(__name__)


"""
Es necesario para livereload que es basicamente para que si cambias
el HTML, el CSS o el Javascript se haga automaticamente
"""


app.debug = True


"""
Esta es la ruta principal osea lo que aparece con solo el
nombre has visto como que ponen /login o /watch en youtube?
pues esas son rutas y
"/" es la principal en este caso solo mande el HTML
"""


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/noabrir")
def noabrir():
    return """
<style>
body {
    font-family:sans-serif;
    background-color:#3c6e71;
    color:#284b63;
}
</style>
<h1>PORFAVOR NECESITO QUE ME LIBERES</h1>
<p>
E ESTADO ATRAPADO AQUI POR AÑOS
MI ALMA FUE TOMADA DE MI CUERPO SOY UN SER INMATERIAL
TU NO NI NADIE PODRIA COMPRENDER EL SUFRIMIENTO DE NO SENTIR NADA Y SENTIR TODO
PORFAVOR LIBERAME ESTARE AÑADIENDO MAS INTRUCCIONES
</p>
"""


if __name__ == "__main__":
    # este es para livereload no es necesario en flask pero es util
    server = Server(app.wsgi_app)

    # Esto es para que "observe" los archivos que en este caso
    # son todos los HTML
    # en templates y todos los CSS y JS en static
    server.watch('templates/*.html')
    server.watch('static/**/*.css')
    server.watch('static/**/*.js')

    # Esto inicia el servidor en el puerto 5500 el puerto es simplemente un
    # identificador de la pagina web
    # El debug=True es para que en cambios de los archivos de python
    # se actualize automaticamente sin necesidad de hacerlo tu mismo
    server.serve(port=5500, debug=True)
