from flask import Flask, render_template, request, redirect, url_for, session, flash
from random import randint
import sqlite3


app = Flask(__name__)
app.secret_key = '111'
DATABASE = 'user.db'


monstros = {
    "goblim": {"ataque": 3, "defesa": 1, "vida": 8, "esquiva": 2},
    "ogro": {"ataque": 4, "defesa": 1, "vida": 12, "esquiva": 4},
    "dragao": {"ataque": 6, "defesa": 2, "vida": 20, "esquiva": 6},
    "lorde_demonio": {"ataque": 10, "defesa": 5, "vida": 45, "esquiva": 8},
    "mimico": {"ataque": 4, "defesa": 1, "vida": 12, "esquiva": 4}
}

experiencia_monstro = {
    "goblim": 50,
    "ogro": 100,
    "dragao": 200,
    "lorde_demonio": 500,
    "mimico": 100
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
def subir_de_nivel(personagem):
  
    while personagem["exp"] >= personagem["exp_necessaria"]:
        personagem["exp"] -= personagem["exp_necessaria"]
        personagem["nivel"] += 1
        print(f"Você subiu para o nível {personagem['nivel']}!")
              
        for atributo in ["ataque", "defesa", "vida_total", "esquiva"]:
            aumento = personagem[atributo] // 2  
            personagem[atributo] += aumento
            print(f"{atributo.capitalize()} aumentado para {personagem[atributo]}.")
     
        personagem["exp_necessaria"] = int(personagem["exp_necessaria"] * 1.4)  
        print(f"Experiência necessária para o próximo nível: {personagem['exp_necessaria']}.")
def abrir_bau():
    tentativas = 3
    print("\n🔑 Tentando abrir o baú... 🔑\n")
    for i in range(tentativas):
        rolagem = randint(1, 20)
        print(f"🔍 Tentativa {i + 1}: Você rolou {rolagem}")
       
        if rolagem >= 10:
            print("\n🎉 Baú aberto com sucesso! 🎉")
            return True
        else:
            print("\n🔒 O baú não abriu... tentando novamente 🔒\n")
    print("\n💀 Você falhou em abrir o baú. 💀")
    return False
def desafio_bau(personagem):
    print("\n🗺️ Você está explorando... procurando por tesouros... 🗺️")
    desafio = randint(1, 20)

    if desafio <= 4:
        print("\n🎉 Você encontrou um baú brilhante! 🎉\n")
        print("Abrindo o baú...")

        if randint(1, 10) == 1: 
            print("⚠️ Mas espere... algo está errado... ⚠️")
            print("\n😈 O baú se transformou em um Mimético! 😈\n")
            combate(personagem, "mimico")
        else:
            if abrir_bau():
                print("\n💖 Você recuperou 50% da sua vida! 💖")
                personagem["vida"] = min(personagem["vida_total"], personagem["vida"] + personagem["vida_total"] // 2)

    elif desafio == 20:
        print("\n🌋 Você encontrou o temível Lorde Demônio! 🌋")
        combate(personagem, "lorde_demonio")

    else:
        tipo_monstro = "goblim" if desafio <= 10 else "ogro" if desafio <= 15 else "dragao"
        print(f"\n⚔️ Você encontrou um {tipo_monstro} pronto para lutar! ⚔️")
        combate(personagem, tipo_monstro)

     

def ataque_geral(personagem, monstro):
    dado20_personagem = randint(1, 20)  
    resultado_ataque = dado20_personagem + personagem["ataque"]  
    personagem["dado_ataque"] = dado20_personagem 

    print(f"Rolando os dados do ataque = {dado20_personagem} + {personagem['ataque']} = {resultado_ataque}")

    if dado20_personagem == 20:
        print("Acerto Crítico!")
        return (personagem["ataque"] * 2) - monstro["defesa"]
    
   
    if print(monstro, personagem):
        return 0
    
    if resultado_ataque >= monstro["defesa"]:
        print("Você atacou o monstro!!")
        return personagem["ataque"] - monstro["defesa"]
    else:
        print("O ataque falhou!")
        return 0

def funcao_de_esquiva(personagem, monstro, dado_rolado):
    if "esquiva" not in personagem:
        print("Erro: Atributo 'esquiva' não encontrado no personagem.")
        return False
    if "ataque" not in monstro:
        print("Erro: Atributo 'ataque' não encontrado no monstro.")
        return False

    resultado_esquiva_jogador = dado_rolado + personagem["esquiva"] 
    resultado_esquiva_monstro = randint(1, 20) + monstro["esquiva"]
    
    print(f"Rolando os dados do jogador: {dado_rolado} + {personagem['esquiva']} = {resultado_esquiva_jogador}")
    print(f"Rolando os dados do monstro para esquiva: {resultado_esquiva_monstro}")

   
    if resultado_esquiva_jogador > resultado_esquiva_monstro:
        print("Você esquivou do ataque do monstro!")
        return True
    else:
        print("Você não conseguiu esquivar e foi atingido!")
        return False
    
def combate(personagem, tipo_monstro):
    monstro = monstros[tipo_monstro].copy()  
    print(f"\nApareceu um {tipo_monstro}!\n")  
    defesa_temporaria = personagem["defesa"]  
    
    while monstro["vida"] > 0 and personagem["vida"] > 0:
        print(f"\n{('❤️')} Vida do Personagem: {personagem['vida']}  |  {tipo_monstro} Vida: {monstro['vida']} {('💀')}\n")
        
        while True:
            print("\nEscolha sua ação:")
            print("A = Atacar ⚔️")
            print("D = Defender 🛡️")
            print("E = Esquivar 🤸")
            print("F = Fugir 🏃")
            print("M = Ver Atributos do Monstro 🦹")
          
            acao = input("Ação: ").upper()           
            if acao in ["A", "D", "E", "F", "M"]:
                break
            else:
                print("Opção inválida! Tente novamente.\n")
        
        if acao == "F":
            chance_fuga = randint(1, 2)
            if chance_fuga == 1:
                print("\nVocê conseguiu fugir com sucesso! 🏃💨\n")
                personagem["rodadas"].append("Fugiu com sucesso")
                return
            else:
                dano_monstro = monstro["ataque"] - defesa_temporaria
                personagem["vida"] -= max(dano_monstro, 0)
                print(f"\nVocê tentou fugir, mas foi atingido e sofreu {max(dano_monstro, 0)} de dano. {('💥')}\n")
                personagem["rodadas"].append(f"Fuga falhou, sofreu {max(dano_monstro, 0)} de dano")
                continue

        elif acao == "E":
            dado_rolado = randint(1, 20) 
            esquivou = funcao_de_esquiva(personagem, monstro, dado_rolado)
            if esquivou:
                personagem["rodadas"].append("Esquivou com sucesso 🤸")
                print("\nVocê esquivou com sucesso! ✨\n")
                continue
            else:
                print("\nVocê não conseguiu esquivar... 😓\n")
        
        elif acao == "D":
            defesa_temporaria = personagem["defesa"] + 2 
            print("\nVocê se defendeu, aumentando sua defesa temporariamente! 🛡️\n")
            personagem["rodadas"].append("Defendeu 🛡️")
       
        elif acao == "M":
            print(f"\nAtributos do {tipo_monstro}:")
            print(f"Ataque: {monstro['ataque']}, Defesa: {monstro['defesa']}, Vida: {monstro['vida']}, Esquiva: {monstro['esquiva']} 🦹\n")
            continue    
        else:
            dano_causado = ataque_geral(personagem, monstro)
            monstro["vida"] -= max(dano_causado, 0)
            personagem["rodadas"].append(f"Atacou e causou {max(dano_causado, 0)} de dano ⚔️")
            print(f"\nVocê causou {max(dano_causado, 0)} de dano. Vida do monstro agora é {monstro['vida']}.\n")
        
        if monstro["vida"] > 0:
            dano_monstro = monstro["ataque"] - defesa_temporaria
            personagem["vida"] -= max(dano_monstro, 0)
            print(f"\nVocê sofreu {max(dano_monstro, 0)} de dano. {('💥')} Sua vida agora é {personagem['vida']}.\n")
            personagem["rodadas"].append(f"Sofreu {max(dano_monstro, 0)} de dano")

    if personagem["vida"] > 0:
        print(f"\nVocê venceu o combate contra o {tipo_monstro}! {('🎉')}\n")
        personagem["rodadas"].append(f"Venceu o {tipo_monstro}")
        personagem["exp"] += experiencia_monstro[tipo_monstro]
        print(f"\nVocê ganhou {experiencia_monstro[tipo_monstro]} de experiência! {('⭐')}\n")
        subir_de_nivel(personagem)

     

def salvar_personagem_db(personagem):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    
    cursor.execute('DELETE FROM personagem')
    
    

    cursor.execute(
        '''
        INSERT INTO personagem (nome, raca, vocacao, ataque, defesa, vida, esquiva, nivel, exp, vida_total)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (
            personagem["nome"], personagem["raca"], personagem["vocacao"],
            personagem["ataque"], personagem["defesa"], personagem["vida"],
            personagem["esquiva"], personagem["nivel"], personagem["exp"], personagem["vida_total"]
        )
    )
    
    conn.commit()
    conn.close()


@app.route('/inicio', methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        opcao = request.form['opcao']
        if opcao == 'novo':
            return redirect(url_for('criar_nome'))
        elif opcao == 'carregar':
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM personagem LIMIT 1') 
            personagem = cursor.fetchone()
            conn.close()
            if personagem:
             
                session['nome'] = personagem[1]
                session['raca'] = personagem[2]
                session['vocacao'] = personagem[3]
                return redirect(url_for('painel_controle'))
            else:
                flash('Nenhum personagem salvo encontrado!', 'error')
                return redirect(url_for('inicio'))
    return render_template('inicio.html')


@app.route('/criar_nome', methods=['GET', 'POST'])
def criar_nome():
    if request.method == 'POST':
        session['nome'] = request.form['nome']
        return redirect(url_for('criar_raca'))
    return render_template('criar_nome.html')


@app.route('/criar_raca', methods=['GET', 'POST'])
def criar_raca():
    racas = {'A': 'Anão', 'E': 'Elfo', 'H': 'Humano'}
    if request.method == 'POST':
        session['raca'] = request.form['raca']
        return redirect(url_for('criar_vocacao'))
    return render_template('criar_raca.html', racas=racas)


@app.route('/criar_vocacao', methods=['GET', 'POST'])
def criar_vocacao():
    vocacoes = {'G': 'Guerreiro', 'A': 'Arqueiro', 'P': 'Paladino'}
    if request.method == 'POST':
        session['vocacao'] = request.form['vocacao']

       
        atributos_base = {"ataque": 2, "defesa": 1, "vida": 8, "esquiva": 1}

       
        raca = session['raca']
        if raca in raças:
            for atributo, valor in raças[raca].items():
                atributos_base[atributo] += valor

       
        vocacao = session['vocacao']
        if vocacao in vocações:
            for atributo, valor in vocações[vocacao].items():
                atributos_base[atributo] += valor

        
        personagem = {
            "nome": session['nome'],
            "raca": raca,
            "vocacao": vocacao,
            "ataque": atributos_base["ataque"],
            "defesa": atributos_base["defesa"],
            "vida": atributos_base["vida"],
            "esquiva": atributos_base["esquiva"],
            "nivel": 1,
            "exp": 0,
            "vida_total": atributos_base["vida"],
            "rodadas": []
        }

       
        salvar_personagem_db(personagem)
        flash('Personagem criado com sucesso!', 'success')
        return redirect(url_for('painel_controle'))
    return render_template('criar_vocacao.html', vocacoes=vocacoes)


@app.route('/painel_controle')
def painel_controle():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM personagem LIMIT 1') 
    cursor.execute('SELECT * FROM personagem')
    personagem = cursor.fetchone()
    conn.close()
    return render_template('painel_controle.html', personagem=personagem)


@app.route('/historico')
def historico():
    personagem = {
        "nome": session.get('nome', 'Desconhecido'),
        "raca": session.get('raca', 'Indefinida'),
        "vocacao": session.get('vocacao', 'Indefinida'),
        "ataque": 2,
        "defesa": 1,
        "vida": 8,
        "esquiva": 1,
        "nivel": 1,
        "exp": 0,
        "vida_total": 8,
        "rodadas": ["Vitória contra monstro", "Derrota para monstro"]
    }
    return render_template('historico.html', personagem=personagem)


@app.route('/caverna', methods=['GET', 'POST'])
def caverna():
    personagem = session.get('personagem', {})
    if request.method == 'POST':
       desafio_bau()  
       return render_template('resultado_combate.html', personagem=personagem)  
    
    return render_template('caverna.html', personagem=personagem)

        
   
        



@app.route('/sair')
def sair():
    session.clear()
    return redirect(url_for('index'))


@app.route('/')
def index():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM personagem')
    personagens = cursor.fetchall()
    conn.close()
    return render_template('index.html', personagens=personagens)


if __name__ == '__main__':
    app.run(debug=True)
