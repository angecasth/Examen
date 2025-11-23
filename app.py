from flask import Flask, render_template, request

app = Flask(__name__)

PRECIO_TARRO = 9000 


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None

    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        edad = request.form.get("edad", "").strip()
        tarros = request.form.get("tarros", "").strip()

        if not nombre or not edad or not tarros:
            resultado = {"error": "Todos los campos son obligatorios."}
        else:
            try:
                edad = int(edad)
                tarros = int(tarros)

                total_sin_desc = tarros * PRECIO_TARRO

                if 18 <= edad <= 30:
                    descuento = 0.15
                elif edad > 30:
                    descuento = 0.25
                else:
                    descuento = 0.0

                monto_descuento = total_sin_desc * descuento
                total_pagar = total_sin_desc - monto_descuento

                resultado = {
                    "nombre": nombre,
                    "edad": edad,
                    "tarros": tarros,
                    "total_sin_desc": total_sin_desc,
                    "descuento_porcentaje": int(descuento * 100),
                    "total_pagar": total_pagar,
                }
            except ValueError:
                resultado = {
                    "error": "Debes ingresar valores numéricos válidos en Edad y Tarros."
                }

    return render_template("ejercicio1.html", resultado=resultado)


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None

    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip().lower()
        clave = request.form.get("clave", "").strip()

        if usuario == "juan" and clave == "admin":
            mensaje = "Bienvenido administrador juan"
        elif usuario == "pepe" and clave == "user":
            mensaje = "Bienvenido usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template("ejercicio2.html", mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)
