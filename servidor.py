from distutils.log import debug
from flask import Flask, request, jsonify, render_template


# Generar el servidor (Back-end)

servidorWeb = Flask(__name__)

# Anotación


@servidorWeb.route("/test", methods=['GET'])
def formulario():
    return render_template('pagina.html')


if __name__ == '__main__':
    servidorWeb.run(debug=False, host='0.0.0.0', port='8080')
