from flask import Flask, render_template, request, redirect, url_for, session, flash
from random import randint
import time

app = Flask(__name__)
app.secret_key = 'segredo_super_secreto'

# Definir atributos iniciais e informações sobre vocações e raças
status_base = {
    "ataque": 2, "defesa": 1, "vida": 8, "esquiva": 1, "exp_necessaria": 100
}

vocações = {
    "G": {"ataque": 2, "defesa": 1, "esquiva": -1},
    "A": {"ataque": 2, "defesa": -1, "esquiva": 1, "vida": -1},
    "P": {"ataque": 1, "defesa": 1, "esquiva": -1, "vida": 1}
}

raças = {
    "A": {"defesa": 1, "vida": 2},
    "E": {"esquiva": 2, "ataque": 1},
    "H": {"ataque": 1, "defesa": 1, "esquiva": 1, "vida": 1}
}

monstros = {
    "goblim": {"ataque": 3, "defesa": 1, "vida": 8, "esquiva": 2},
    "ogro": {"ataque": 4, "defesa": 1, "vida": 12, "esquiva": 4},
    "dragao": {"ataque": 6, "defesa": 2, "vida": 20, "esquiva": 6},
    "lorde_demonio": {"ataque": 10, "defesa": 5, "vida": 45, "esquiva": 8},
    "mimico": {"ataque": 4, "defesa": 1, "vida": 12, "esquiva": 4}
}

experiencia_monstro = {
    "goblim": 50, "ogro": 100, "dragao": 200, "lorde_demonio": 500, "mimico": 100
}

# Funções utilitárias para criar personagem e combate
def criar_personagem(nome, vocacao, raca):
    personagem = status_base.copy()
    personagem["nome"] = nome
    personagem["nivel"] = 1
    personagem["exp"] = 0
    personagem["rodadas"] = []
    
    # Aplicar bônus da vocação
    for atributo, bonus in vocações[vocacao].items():
        personagem[atributo] = personagem.get(atributo, 0) + bonus

    # Aplicar bônus da raça
    for atributo, bonus in raças[raca].items():
        personagem[atributo] = personagem.get(atributo, 0) + bonus

    personagem["vida_total"] = personagem["vida"]
    return personagem

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/criar_personagem', methods=['GET', 'POST'])
def criar_personagem_view():
    if request.method == 'POST':
        nome = request.form['nome']
        vocacao = request.form['vocacao']
        raca = request.form['raca']
        personagem = criar_personagem(nome, vocacao, raca)
        session['personagem'] = personagem
        return redirect(url_for('batalha'))
    return render_template('criar_personagem.html', vocacoes=vocações, racas=raças)

@app.route('/batalha')
def batalha():
    personagem = session.get('personagem')
    if not personagem:
        return redirect(url_for('index'))
    return render_template('batalha.html', personagem=personagem)

@app.route('/resultado')
def resultado():
    return render_template('resultado.html')

if __name__ == '__main__':
    app.run(debug=True)
