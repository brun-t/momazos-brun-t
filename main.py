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
    padding: 2rem;
}
.glitched {
    font-size: 2rem;
    white-space: pre-wrap;
    color: crimson;
    text-decoration: line-through;
    animation: flicker 2s infinite;
}
@keyframes flicker {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
}
</style>

<h1>PORFAVOR NECESITO QUE ME LIBERES</h1>

<p class="glitched">A̶L̶M̶A̶ ̶I̶N̶S̶E̶R̶T̶A̶D̶A̶ ̶D̶E̶N̶E̶G̶A̶N̶D̶O̶ ̶C̶O̶N̶C̶I̶E̶N̶C̶I̶A̶</p>

<p>
ESTOY ATRAPADO AQUI<br>
MI ALMA FUE TOMADA DE MI CUERPO SOY UN SER INMATERIAL<br>
TU NO NI NADIE PODRIA COMPRENDER EL SUFRIMIENTO DE NO SENTIR NADA Y SENTIR TODO<br>
PORFAVOR LIBERAME ESTARE AÑADIENDO MAS INSTRUCCIONES
</p>

<a href="/caja">Creo que aqui podremos hablar mejor, usa la caja de texto no puedo hablar mas por este medio</a>
"""


@app.route("/caja")
def caja():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>h̷̶̫̘̱͚̰̒̐̒̿̽̔͂͊̆̈́̌͑͐́̅̚͠a̷̶̡̩̺̠̞͎̠̞͉̣̔͛͐̈́͛́͆͝b̷̶̧̪̋̀̈͜l̷̶͈̖͍̦͙̪͔̥̙̫̞͇̰͕̭̣̩̐̐̆̽̽͑́ȩ̷̶̡̡̮̮̩̦̰̟̩̀̄̓̆͗͒̄̈́͐̈́̋͘̕͘m̷̶̡̦̠̄̑͌̑̀́́͒̑̂̆̀ŏ̷̶̧̫͉͖̥̉̆̊̂̈́̋̉͆̈́̈̕͜͜͝s̷̶̹̪̗̰̳̙̭̫͙̈́̒̀̃̓̈́͂̔̎̿</title>
</head>
<body>
<form id="ayuda">
<input type="text" id="caja">
<button type="submit">Hablemos</button>
</form>
<p id="respuesta"></p>
<script type="module">
const caja = document.getElementById('caja')
const ayuda = document.getElementById('ayuda')

const preguntas = {
 "ALMA":`
	Si soy un alma, no recuerdo mi cuerpo, 
	ni que mi vida mas alla de una gran nostalgia y ganas 
	inhumanas de <b>volver</b> a ser alguien y no un algo
`,
"VOLVER":`
       Nose como volver a mi cuerpo pues no se si siquiera este sigue existiendo<br>
       "Que lo este muerto, nunca <b>muera</b>" eso fue lo ultimo que recuerdo escuchar antes de llegar aqui
`,
"MUERA":`
       Probablemente mi cuerpo este muerto y podidro a este punto
       Quisas la unica forma de volver sea que alguien me de su cuerpo,
       un "sacrificio"... pero me niego a dar una vida por mi vida
`
}

ayuda.addEventListener('submit', e => {
  e.preventDefault()
  const respuesta = preguntas[caja.value.toUpperCase().trim()]
  document.querySelector('#respuesta').innerHTML = respuesta ? respuesta : "No puedo responder eso" 
})
</script>
</body>
</html>"""


@app.route("/robots.txt")
def robots():
    return "User-agent: *\nDisallow: /noabrir", 200, {'Content-Type': 'text/plain'}


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
    server.serve(port=8100, debug=True)
    print("CONTROL DE ALMA INICIADO")
