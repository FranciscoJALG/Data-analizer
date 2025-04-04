from  flask import Flask, request, jsonify, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os 
import uuid

app = Flask(__name__, static_folder="Statics")
UPLOAD_FOLDER = "Uploads"
GRAPH_FOLDER = "Statics/Graphs"
os.makedirs(UPLOAD_FOLDER, exist_ok = True)
os.makedirs(GRAPH_FOLDER,exist_ok = True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

#Guardar el historial de archivos
upload_files = []

@app.route("/")
def index():
    return render_template("index.html", files=upload_files) #Se pasa el historial al frontend

@app.route("/uploads", methods=["POST"])
def handle_file():
    if "file" not in request.files:
        return jsonify({"error:" "No se encontro el archivo"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error:" "Nombre de archivo vacio"}), 400
    
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    #Procesar CSV
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
        graph_path = os.path.join(GRAPH_FOLDER,graph_filename)
        plt.savefig(graph_path)
        plt.close()
        stats["graph_url"] = graph_path

    upload_files.append({"name": file.filename, "stats": stats, "graph_url": stats.get("graph_url", None)})

    return jsonify(stats)

if __name__ == "__main__":
    app.run(debug=True)

