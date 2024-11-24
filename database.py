import sqlite3

def conectar_db():
    conn = sqlite3.connect("user.db")
    return conn

def criar_tabela_personagem():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS personagem (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            vocacao TEXT,
            raca TEXT,
            ataque INTEGER,
            defesa INTEGER,
            vida INTEGER,
            esquiva INTEGER,
            nivel INTEGER,
            exp INTEGER,
            vida_total INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def salvar_personagem(personagem):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO personagem (nome, vocacao, raca, ataque, defesa, vida, esquiva, nivel, exp, vida_total)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        personagem['nome'], personagem.get('vocacao'), personagem.get('raca'),
        personagem['ataque'], personagem['defesa'], personagem['vida'],
        personagem['esquiva'], personagem['nivel'], personagem['exp'], personagem['vida_total']
    ))
    conn.commit()
    conn.close()
    