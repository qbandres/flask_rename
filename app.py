from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        archivos = request.files.getlist('archivos')
        nuevo_nombre_base = request.form['nuevo_nombre_base']

        if archivos and nuevo_nombre_base:
            carpeta_destino = os.getcwd()
            for i, archivo in enumerate(archivos):
                nombre, extension = os.path.splitext(archivo.filename)
                nuevo_nombre = f"{nuevo_nombre_base}_{i+1}{extension}"
                nuevo_path = os.path.join(carpeta_destino, nuevo_nombre)
                archivo.save(nuevo_path)
            return "Archivos renombrados exitosamente"

    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
