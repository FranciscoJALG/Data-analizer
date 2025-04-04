# Data-analizer
📊 Analizador de Datos CSV

Este es un proyecto basado en Flask que permite analizar archivos CSV subidos por los usuarios, generando estadísticas y gráficos de las columnas numéricas. La aplicación está desplegada en Render.

🚀 Características

📂 Subida de archivos CSV.

📊 Análisis de datos: número de filas, columnas, nombres de columnas y media de los valores numéricos.

📈 Generación de gráficos para columnas numéricas.

🖥️ Interfaz sencilla con Bootstrap.

📸 Capturas de Pantalla

![image](https://github.com/user-attachments/assets/a6860546-c2cf-4c77-ae30-57bcd2df291f)
![image](https://github.com/user-attachments/assets/c24bad17-c81d-43c0-bd36-77f1f99960ea)
![image](https://github.com/user-attachments/assets/6dbda5de-aa9d-42ea-9d15-528ee911b6c6)


🛠️ Tecnologías Utilizadas

Backend: Flask, Pandas, Matplotlib

Frontend: HTML, Bootstrap, JavaScript

Despliegue: Render

📂 Estructura del Proyecto
📁 Backend/
│── app.py                # Código principal de la aplicación Flask
│── requirements.txt      # Dependencias del proyecto
│── 📁 Templates/
│   └── index.html        # Interfaz de usuario
│── 📁 Statics/
│   └── Graphs/           # Carpeta para guardar gráficos generados
│── 📁 Uploads/           # Carpeta para archivos subidos
│── render.yaml           # Configuración para despliegue en Render
└── README.md             # Documentación del proyecto

🛠️ Instalación y Ejecución Local

Clonar el repositorio:
git clone https://github.com/FranciscoJALG/Data-analizer.git
cd Data-analizer/Backend

Crear un entorno virtual (opcional pero recomendado):
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

Instalar las dependencias:
pip install -r requirements.txt

Ejecutar la aplicación:
python app.py

Abrir en el navegador:
http://127.0.0.1:5000

🚀 Despliegue en Render

Subir el código a un repositorio en GitHub.

Crear un nuevo servicio en Render y conectar el repositorio.

Configurar la variable de entorno PORT=10000.

Render instalará automáticamente las dependencias y ejecutará la aplicación.

📝 Autor

FranciscoJALG - GitHub

📄 Licencia
Este proyecto está bajo la licencia MIT. Puedes ver más detalles en el archivo LICENSE.
