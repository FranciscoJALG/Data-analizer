from flask import Flask, request, jsonify, render_template, url_for
import pandas as pd
import matplotlib.pyplot as plt
import os
import uuid

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 📌 Obtiene la ruta absoluta de Backend
STATIC_DIR = os.path.join(BASE_DIR, "Statics")  # 📌 Ruta correcta de archivos estáticos dentro de Backend
UPLOAD_FOLDER = os.path.join(BASE_DIR, "Uploads")  # 📌 Ruta correcta para las subidas
GRAPH_FOLDER = os.path.join(STATIC_DIR, "Graphs")  # 📌 Guardar gráficos en Backend/Statics/Graphs

app = Flask(__name__, static_folder=STATIC_DIR)  # 📌 Ahora sirve archivos desde Backend/Statics
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(GRAPH_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Guardar el historial de archivos
upload_files = []

@app.route("/")
def index():
    return render_template("index.html", files=upload_files)  # Se pasa el historial al frontend

@app.route("/uploads", methods=["POST"])
def handle_file():
    if "file" not in request.files:
        return jsonify({"error": "No se encontró el archivo"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Nombre de archivo vacío"}), 400

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    # Procesar CSV
    df = pd.read_csv(file_path)
    stats = {
        "Filas": df.shape[0],
        "Columnas": df.shape[1],
        "Columnas_Nombres": df.columns.to_list(),
        "Media": df.mean(numeric_only=True).to_dict()
    }

    numeric_columns = df.select_dtypes(include=["number"]).columns
    if not numeric_columns.empty:
        plt.figure(figsize=(6, 4))
        df[numeric_columns[0]].hist(bins=20)
        graph_filename = f"graph_{uuid.uuid4().hex}.png"
        graph_path = os.path.join(GRAPH_FOLDER, graph_filename)  # 📌 Guardamos en Backend/Statics/Graphs
        plt.savefig(graph_path)
        plt.close()

        # 📌 Generamos la URL correcta para que el navegador pueda ver la imagen
        stats["graph_url"] = url_for('static', filename=f"Graphs/{graph_filename}")

    upload_files.append({"name": file.filename, "stats": stats, "graph_url": stats.get("graph_url", None)})

    return jsonify(stats)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
