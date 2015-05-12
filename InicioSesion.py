#from IDtwitter import * #Modulo con los tokens de twitter.
import twitter
import io
import json
from flask import request
from flask import Flask, render_template
#from flask.ext.googlemaps import GoogleMaps
#from flask.ext.googlemaps import Map

app = Flask(__name__)
#GoogleMaps(app)

from crypt import crypt

@app.route("/vermyhojadecalculo", methods=['POST'])
def vermyhojadecalculo():
    #aca iria el codigo que redireccionaria iniciando session y mostrando el google hoja de calculo.
    return render_template('tareas.html')

@app.route("/vermygooglecalendar", methods=['POST'])
def vermygooglecalendar():
    #aca iria el codigo que redireccionaria iniciando session y mostrando el google calendar.
    return render_template('tareas.html')


@app.route("/vermytwitter", methods=['POST'])
def vermytwitter():
    #aca iria el codigo que redireccionaria iniciando session en twitter.
    return render_template('tareas.html')

@app.route("/publicarnotasexamen", methods=['POST'])
def publicarnotasexamen():
    #aca iria el codigo de hacedr twitt y mostrar el enlace de la hora de calculo de google.
    return render_template('notasexamen.html')

@app.route("/publicarfechaexamen", methods=['POST'])
def publicarfechaexamen():
    #aca iria el codigo para hacer el twitt y postearlo y agregar a google calendar
    return render_template('fechaexamen.html')

@app.route("/agregarnotaalumno", methods=['POST'])
def agregarnotaalumno():
    #aca iria el codigo de meter linea en hoja de calculo de google
    return render_template('notasexamen.html')

@app.route("/formulariofechaexamen", methods=['POST'])
def formulariofechaexamen():
    return render_template('fechaexamen.html')

@app.route("/formularionotasexamen", methods=['POST'])
def formularionotasexamen():
    return render_template('notasexamen.html')

@app.route("/tareas", methods=['POST'])
def tareas():
    return render_template('tareas.html')

@app.route("/salir", methods=['Post'])
def salir():
    htpuser = ''
    htpasswd = ''
    authdU = crypt('wrongpw',htpuser)==htpuser
    authdP = crypt('wrongpw',htpasswd)==htpasswd
    return render_template('index.html')

@app.route("/buscar", methods=['POST'])
def buscar():
    user = request.form['text']
    termino = pw = request.form['passwd'] 
    htpuser = 'Jywn1PBEdYjkg'
    htpasswd = 'Jywn1PBEdYjkg'
    authU = crypt(pw,htpasswd)==htpasswd
    authP = crypt(user,htpuser)==htpuser
    print authU, authP
    if (authU == True) and (authP == True):        
        return render_template('tareas.html')
    else:        
        return render_template('index.html')

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False)