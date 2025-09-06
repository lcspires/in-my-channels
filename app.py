import sqlite3
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

DB_FILE = "videos.db"

# --- Função para buscar vídeos no SQLite usando FTS ---
def buscar_videos(termo):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    # Pesquisa full-text (case-insensitive)
    query = "SELECT canal, titulo FROM videos WHERE videos MATCH ?"
    c.execute(query, (termo,))
    resultados = c.fetchall()
    conn.close()
    return [{"canal": canal, "titulo": titulo} for canal, titulo in resultados]

# --- Rota principal (home) ---
@app.route("/")
def home():
    return render_template("index.html")

# --- Rota de busca ---
@app.route("/search")
def search():
    termo = request.args.get("q", "").strip()
    if not termo:
        return jsonify({"results": []})

    resultados = buscar_videos(termo)
    if not resultados:
        return jsonify({"results": [], "message": "Nenhum vídeo encontrado"})
    
    return jsonify({"results": resultados})

# --- Rodar app ---
if __name__ == "__main__":
    app.run(debug=True)
