from flask import Blueprint, jsonify

bp = Blueprint('blueprint', __name__, url_prefix='/filas')

filaGlobal = {'Normal': [0, 0], 'Preferencial': [0, 0]}


@bp.route('/situacao')
def show():
    return filaGlobal


@bp.route('/gerar/normal')
def postFilaNormal():
    list = filaGlobal.get('Normal')

    filaGlobal['Normal'] = [list[0], list[1] + 1]

    return '', 200


@bp.route('/gerar/preferencial')
def postFilaPreferencial():
    list = filaGlobal.get('Preferencial')

    filaGlobal['Preferencial'] = [list[0], list[1] + 1]

    return '', 200


@bp.route('/chamar/normal')
def putFilaNormal():
    list = filaGlobal.get('Normal')

    list_1 = list[0]
    list_2 = list[1]

    if list_1 < list_2:
        filaGlobal['Normal'] = [list_1 + 1, list_2]

        return show(), 200
    else:
        return 'Fila vazia', 500


@bp.route('/chamar/preferencial')
def putFilaPreferencial():
    list = filaGlobal.get('Preferencial')

    list_1 = list[0]
    list_2 = list[1]

    if list_1 < list_2:
        filaGlobal['Preferencial'] = [list_1 + 1, list_2]

        return show(), 200
    else:
        return 'Fila vazia', 500
