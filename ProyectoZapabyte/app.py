from flask import Flask, render_template, request, redirect, render_template

from conexionDBUsuarios import ConexionDBUsuario

app = Flask(__name__)


@app.route('/index')  # Definiendo la ruta raíz
def principal():
    return render_template('index.html')

@app.route('/hombres')
def hombres():
    return render_template('hombres.html')

@app.route('/mujeres')
def mujeres():
    return render_template('mujeres.html')

@app.route('/niños')
def niños():
    return render_template('niños.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/prueba')
def login1():
    return render_template('prueba.html')  

@app.route('/privacety')
def politicas_de_privacidad():
    return render_template('privacety.html')

@app.route('/devoluciones')
def politicas_de_devoluciones():
    return render_template('devoluciones.html')

@app.route('/terminosCompra')
def terminosDeCompra():
    return render_template('terminosCompra.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login2')
def login2():
    return render_template('login2.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')


@app.route('/preguntas')
def pregruntas():
    return render_template('preguntas.html')
@app.route('/zapahombre1')
def zapahombre1():
    return render_template('zapashombres/zapahombre1.html')
@app.route('/zapahombre2')
def zapahombre2():
    return render_template('zapashombres/zapahombre2.html')
@app.route('/zapahombre3')
def zapahombre3():
    return render_template('zapashombres/zapahombre3.html')
@app.route('/zapahombre4')
def zapahombre4():
    return render_template('zapashombres/zapahombre4.html')
@app.route('/zapahombre5')
def zapahombre5():
    return render_template('zapashombres/zapahombre5.html')
@app.route('/zapahombre6')
def zapahombre6():
    return render_template('zapashombres/zapahombre6.html')
@app.route('/zapahombre7')
def zapahombre7():
    return render_template('zapashombres/zapahombre7.html')
@app.route('/zapahombre8')
def zapahombre8():
    return render_template('zapashombres/zapahombre8.html')
@app.route('/zapahombre9')
def zapahombre9():
    return render_template('zapashombres/zapahombre9.html')
@app.route('/zapahombre10')
def zapahombre10():
    return render_template('zapashombres/zapahombre10.html')
@app.route('/zapahombre11')
def zapahombre11():
    return render_template('zapashombres/zapahombre11.html')
@app.route('/zapahombre12')
def zapahombre12():
    return render_template('zapashombres/zapahombre12.html')
@app.route('/zapamujer1')
def zapamujer1():
    return render_template('zapasmujer/zapamujer1.html')
@app.route('/zapamujer2')
def zapamujer2():
    return render_template('zapasmujer/zapamujer2.html')
@app.route('/zapamujer3')
def zapamujer3():
    return render_template('zapasmujer/zapamujer3.html')
@app.route('/zapamujer4')
def zapamujer4():
    return render_template('zapasmujer/zapamujer4.html')
@app.route('/zapamujer5')
def zapamujer5():
    return render_template('zapasmujer/zapamujer5.html')
@app.route('/zapamujer6')
def zapamujer6():
    return render_template('zapasmujer/zapamujer6.html')
@app.route('/zapamujer7')
def zapamujer7():
    return render_template('zapasmujer/zapamujer7.html')
@app.route('/zapamujer8')
def zapamujer8():
    return render_template('zapasmujer/zapamujer8.html')
@app.route('/zapamujer9')
def zapamujer9():
    return render_template('zapasmujer/zapamujer9.html')
@app.route('/zapamujer10')
def zapamujer10():
    return render_template('zapasmujer/zapamujer10.html')
@app.route('/zapamujer11')
def zapamujer11():
    return render_template('zapasmujer/zapamujer11.html')
@app.route('/zapamujer12')
def zapamujer12():
    return render_template('zapasmujer/zapamujer12.html')       
@app.route('/zapanino1')
def zapanino1():
    return render_template('zapasnino/zapanino1.html')
@app.route('/zapanino2')
def zapanino2():
    return render_template('zapasnino/zapanino2.html')
@app.route('/zapanino3')
def zapanino3():
    return render_template('zapasnino/zapanino3.html')
@app.route('/zapanino4')
def zapanino4():
    return render_template('zapasnino/zapanino4.html')
@app.route('/zapanino5')
def zapanino5():
    return render_template('zapasnino/zapanino5.html')
@app.route('/zapanino6')
def zapanino6():
    return render_template('zapasnino/zapanino6.html')
@app.route('/zapanino7')
def zapanino7():
    return render_template('zapasnino/zapanino7.html')
@app.route('/zapanino8')
def zapanino8():
    return render_template('zapasnino/zapanino8.html')
@app.route('/zapanino9')
def zapanino9():
    return render_template('zapasnino/zapanino9.html')
@app.route('/zapanino10')
def zapanino10():
    return render_template('zapasnino/zapanino10.html')
@app.route('/zapanino11')
def zapanino11():
    return render_template('zapasnino/zapanino11.html')
@app.route('/zapanino12')
def zapanino12():
    return render_template('zapasnino/zapanino12.html')


@app.route('/insertar_comentario', methods=['POST'])
def insertar_comentario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']

        conexion_db = ConexionDBUsuario()
        conexion_db.insertar_comentario(nombre, correo, mensaje)

        return redirect('/index')

if __name__ == '__main__':
    app.run(debug=True)



