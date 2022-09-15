import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

filaGlobal = {'Normal': [0, 0], 'Preferencial': [0, 0]}

@app.route('/situacao/')
def situacao():
    return filaGlobal

@app.route('/gerar/normal')
def postFilaNormal():
    list = filaGlobal.get('Normal')

    filaGlobal['Normal'] = [list[0], list[1] + 1]

    return '', 200


@app.route('/gerar/preferencial')
def postFilaPreferencial():
    list = filaGlobal.get('Preferencial')

    filaGlobal['Preferencial'] = [list[0], list[1] + 1]

    return '', 200


@app.route('/chamar/normal')
def putFilaNormal():
    list = filaGlobal.get('Normal')

    list_1 = list[0]
    list_2 = list[1]

    if list_1 < list_2:
        filaGlobal['Normal'] = [list_1 + 1, list_2]

        return situacao(), 200
    else:
        return 'Fila vazia', 500


@app.route('/chamar/preferencial')
def putFilaPreferencial():
    list = filaGlobal.get('Preferencial')

    list_1 = list[0]
    list_2 = list[1]

    if list_1 < list_2:
        filaGlobal['Preferencial'] = [list_1 + 1, list_2]

        return situacao(), 200
    else:
        return 'Fila vazia', 500

app.run()