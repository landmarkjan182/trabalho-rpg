import os
from random import randint
import time

os.system('clear')

def escrever_devagar(texto, intervalo=0.05):
    for caractere in texto:
        print(caractere, end='', flush=True)
        time.sleep(intervalo)
    print()

status_base = {
    "ataque": 2,
    "defesa": 1,
    "vida": 8,
    "esquiva": 1,
    "exp_necessaria": 100
}

vocações = {
    "Guerreiro": {"ataque": 2, "defesa": 1, "esquiva": -1},
    "Arqueiro": {"ataque": 2, "defesa": -1, "esquiva": 1, "vida": -1},
    "Paladino": {"ataque": 1, "defesa": 1, "esquiva": -1, "vida": 1}
}

raças = {
    "Anão": {"defesa": 1, "vida": 2},
    "Elfo": {"esquiva": 2, "ataque": 1},
    "Humano": {"ataque": 1, "defesa": 1, "esquiva": 1, "vida": 1}
}


def criar_personagem():
    nome = input("Nome do personagem: ")
    personagem = status_base.copy()
    personagem["nome"] = nome
    personagem["rodadas"] = [] 
    escrever_devagar("Escolha sua Vocação: Guerreiro, Arqueiro, Paladino")
    vocação = input("Vocação: ").capitalize()
    escrever_devagar("Escolha sua Raça: Anão, Elfo, Humano")
    raça = input("Raça: ").capitalize()

    if vocação in vocações:
        for atributo, bonus in vocações[vocação].items():
            personagem[atributo] = personagem.get(atributo, 0) + bonus

    if raça in raças:
        for atributo, bonus in raças[raça].items():
            personagem[atributo] = personagem.get(atributo, 0) + bonus

    return personagem

monstros = {
    "goblim": {"ataque": 3, "defesa": 1, "vida": 8, "esquiva": 2},
    "ogro": {"ataque": 4, "defesa": 1, "vida": 12, "esquiva": 4},
    "dragao": {"ataque": 6, "defesa": 2, "vida": 20, "esquiva": 6},
    "lorde_demonio": {"ataque": 10, "defesa": 5, "vida": 45, "esquiva": 8},
    "mimico": {"ataque": 4, "defesa": 1, "vida": 12, "esquiva": 3}
}
experiencia_monstro = {
    "goblim": 50,
    "ogro": 100,
    "dragao": 200,
    "lorde_demonio": 500,
    "mimico": 100
}
def funcao_de_esquiva(personagem, monstro):
    dado20 = randint(1, 20)
    resultado_esquiva = dado20 + personagem["esquiva"]
    escrever_devagar(f"Rolando os dados= {dado20} + {personagem['esquiva']} = {resultado_esquiva}")

    if resultado_esquiva >= monstro["ataque"]:
        escrever_devagar("Você esquivou do ataque!")
        return True
    else:
        escrever_devagar("VOCÊ FOI ATINGIDO!!")
        return False
    
def ataque_geral(personagem, monstro):
    dado20 = randint(1, 20)
    resultado_ataque = dado20 + personagem["ataque"]
    escrever_devagar(f"Rolando os dados do ataque = {dado20} + {personagem['ataque']} = {resultado_ataque}")

    if dado20 == 20:
        escrever_devagar("Acerto Crítico!")
        return (personagem["ataque"] * 2) - monstro["defesa"]
    
    if resultado_ataque >= monstro["defesa"]:
        escrever_devagar("Você atacou o monstro!!")
        return personagem["ataque"] - monstro["defesa"]
    else:
        escrever_devagar("O ataque falhou!")
        return 0
def exibir_status(personagem):
    escrever_devagar(f"\nStatus do Personagem: {personagem['nome']}")
    escrever_devagar(f"Ataque: {personagem['ataque']}, Defesa: {personagem['defesa']}, Vida: {personagem['vida']}, Esquiva: {personagem['esquiva']}")
    escrever_devagar(f"Nível: {personagem['nivel']}, EXP: {personagem['exp']}/{personagem['exp_necessaria']}")
    escrever_devagar(f"Faltam {personagem['exp_necessaria'] - personagem['exp']} EXP para o próximo nível.")
    escrever_devagar("Histórico de Rodadas de Batalha:")
    for rodada, log in enumerate(personagem["rodadas"], start=1):
        escrever_devagar(f"Rodada {rodada}: {log}")
    print()

def combate(personagem, tipo_monstro):
    monstro = monstros[tipo_monstro].copy()
    escrever_devagar(f"Apareceu um {tipo_monstro}!")  
    while monstro["vida"] > 0 and personagem["vida"] > 0:
        escrever_devagar("Escolha sua ação: Atacar, Defender, Esquivar, Fugir")
        acao = input("Ação: ").capitalize()

        if acao == "Fugir":
            chance_fuga = randint(1, 2)
            if chance_fuga == 1:
                escrever_devagar("Você conseguiu fugir com sucesso!")
                personagem["rodadas"].append("Fugiu com sucesso")
                return
            else:
                dano_monstro = monstro["ataque"] - personagem["defesa"]
                personagem["vida"] -= max(dano_monstro, 0)
                escrever_devagar(f"Você tentou fugir, mas foi atingido e sofreu {max(dano_monstro, 0)} de dano.")
                personagem["rodadas"].append(f"Fuga falhou, sofreu {max(dano_monstro, 0)} de dano")
                continue

        elif acao == "Esquivar":
            esquivou = funcao_de_esquiva(personagem, monstro)
            if esquivou:
                personagem["rodadas"].append("Esquivou com sucesso")
                continue
        
        elif acao == "Defender":
            defesa_temporaria = personagem["defesa"] + 2
            escrever_devagar("Você se defendeu, aumentando sua defesa temporariamente!")
            personagem["rodadas"].append("Defendeu")
        else:
            defesa_temporaria = personagem["defesa"]
            dano_causado = ataque_geral(personagem, monstro)
            monstro["vida"] -= max(dano_causado, 0)
            personagem["rodadas"].append(f"Atacou e causou {max(dano_causado, 0)} de dano")
            escrever_devagar(f"Você causou {max(dano_causado, 0)} de dano. Vida do monstro agora é {monstro['vida']}.\n")
        
        if monstro["vida"] > 0:
            dano_monstro = monstro["ataque"] - defesa_temporaria
            personagem["vida"] -= max(dano_monstro, 0)
            escrever_devagar(f"Você sofreu {max(dano_monstro, 0)} de dano. Sua vida agora é {personagem['vida']}.")
            personagem["rodadas"].append(f"Sofreu {max(dano_monstro, 0)} de dano")

        time.sleep(1)

    if personagem["vida"] > 0:
        escrever_devagar("Você venceu o combate!")
        personagem["rodadas"].append(f"Venceu o {tipo_monstro}")
        subir_de_nivel(personagem)
    else:
        escrever_devagar("Você foi derrotado...")
        personagem["rodadas"].append("Derrotado pelo monstro")
def subir_de_nivel(personagem):
  
    while personagem["exp"] >= personagem["exp_necessaria"]:
        personagem["exp"] -= personagem["exp_necessaria"]
        personagem["nivel"] += 1
        escrever_devagar(f"Você subiu para o nível {personagem['nivel']}!")
              
        for atributo in ["ataque", "defesa", "vida", "esquiva"]:
            aumento = personagem[atributo] // 2  
            personagem[atributo] += aumento
            escrever_devagar(f"{atributo.capitalize()} aumentado para {personagem[atributo]}.")
     
        personagem["exp_necessaria"] = int(personagem["exp_necessaria"] * 1.4)  
        escrever_devagar(f"Experiência necessária para o próximo nível: {personagem['exp_necessaria']}.")

def desafio_bau(personagem):
    desafio = randint(1, 20)
    if desafio <= 20:
        escrever_devagar("Você encontrou um baú!")
        if randint(1, 10) == 1: 
            escrever_devagar("Mas espere... o baú era um Mimético!")
            combate(personagem, "mimico")
        if abrir_bau():
            escrever_devagar("Você recuperou 50% da sua vida!")
            personagem["vida"] = min(status_base["vida"], personagem["vida"] + status_base["vida"] // 2)
    if desafio == 20:
          combate(personagem, "lorde_demonio")

    else:
        tipo_monstro = "goblim" if desafio <= 10 else "ogro" if desafio <= 15 else "dragao"
        combate(personagem, tipo_monstro)

def abrir_bau():
    tentativas = 3
    for i in range(tentativas):
        rolagem = randint(1, 20)
        escrever_devagar(f"Tentativa {i + 1}: Rolou {rolagem}")
        if rolagem >= 10:
            escrever_devagar("Baú aberto com sucesso!")
            return True
    escrever_devagar("Você falhou em abrir o baú.")
    return False

def jogo():
    os.system("clear")
    personagem = criar_personagem()
    exibir_status(personagem)
    while personagem["vida"] > 0:
        desafio_bau(personagem)
        if personagem["vida"] <= 0:
            escrever_devagar("Você morreu... Fim de jogo.")
            exibir_status(personagem) 
            break
        jogar_novamente = input("Deseja continuar? (S/N): ").upper()
        if jogar_novamente != "S":
            escrever_devagar("Fim de jogo.")
            exibir_status(personagem) 
            break


jogo()
