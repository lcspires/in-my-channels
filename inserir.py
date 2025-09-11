import sqlite3

# Arquivo de banco e .txt com novos vídeos
DB_FILE = "videos.db"
TXT_FILE = "videos.txt"

# Conecta/cria banco SQLite
conn = sqlite3.connect(DB_FILE)
c = conn.cursor()

# --- Cria tabela FTS5 se não existir ---
c.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS videos USING fts5(
    canal,
    titulo,
    UNIQUE(canal, titulo)
)
""")

# --- Lê arquivo de vídeos ---
with open(TXT_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

# --- Insere novos vídeos ---
inseridos = 0
for line in lines:
    parts = line.strip().split(";", 1)
    if len(parts) == 2:
        canal, titulo = parts
        try:
            c.execute("INSERT OR IGNORE INTO videos (canal, titulo) VALUES (?, ?)", (canal, titulo))
            inseridos += c.rowcount  # rowcount = 1 se inseriu, 0 se ignorou
        except Exception as e:
            print(f"❌ Erro ao inserir {canal} - {titulo}: {e}")

conn.commit()
print(f"✅ {inseridos} novos vídeos inseridos no banco {DB_FILE} (de {len(lines)} linhas lidas)")

# --- Função de busca para teste rápido ---
def buscar_videos(termo):
    termo = termo.replace("'", "''")  # escape simples para FTS
    query = "SELECT canal, titulo FROM videos WHERE videos MATCH ?"
    c.execute(query, (termo,))
    return c.fetchall()

# --- Teste rápido de busca ---
if __name__ == "__main__":
    termo = input("Digite o termo a buscar nos títulos: ").strip()
    resultados = buscar_videos(termo)
    print(f"\nResultados encontrados: {len(resultados)}\n")
    for canal, titulo in resultados[:50]:  # mostra apenas os 50 primeiros
        print(f"{canal} - {titulo}")

conn.close()
