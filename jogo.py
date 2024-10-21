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
    "esquiva": 1
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
    nome = input("nome: ")
    personagem = status_base.copy()
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
def escrita_status():
    escrever_devagar(f"nome do aventureiro={nome}")
monstros = {
    "goblim": {"ataque": 3, "defesa": 1, "vida": 8, "esquiva": 2},
    "ogro": {"ataque": 4, "defesa": 1, "vida": 12, "esquiva": 4},
    "dragao": {"ataque": 6, "defesa": 2, "vida": 20, "esquiva": 6},
    "lorde_demonio": {"ataque": 10, "defesa": 5, "vida": 45, "esquiva": 8}
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
    
def combate(personagem, tipo_monstro):  
    monstro = monstros[tipo_monstro].copy()
    escrever_devagar(f"Apareceu um {tipo_monstro}!")  
    while monstro["vida"] > 0 and personagem["vida"] > 0:
        if not funcao_de_esquiva(personagem, monstro):
            dano_monstro = monstro["ataque"] - personagem["defesa"]
            personagem["vida"] -= max(dano_monstro, 0)
            escrever_devagar(f"Você sofreu {max(dano_monstro, 0)} de dano. Sua vida agora é {personagem['vida']}.")

        dano_causado = ataque_geral(personagem, monstro)
        monstro["vida"] -= max(dano_causado, 0)

        escrever_devagar(f"Você causou {max(dano_causado, 0)} de dano. Vida do monstro agora é {monstro['vida']}.\n")
        time.sleep(1)

    if personagem["vida"] > 0:
        escrever_devagar("Você venceu o combate!")
    else:
        escrever_devagar("Você foi derrotado...")

def desafio_bau(personagem):
    desafio = randint(1, 20)
    if desafio <= 4:
        escrever_devagar("Você encontrou um baú!")
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
    while personagem["vida"] > 0:
        desafio_bau(personagem)
        if personagem["vida"] <= 0:
            escrever_devagar("Você morreu... Fim de jogo.")
            break
        jogar_novamente = input("Deseja continuar? (S/N): ").upper()
        if jogar_novamente != "S":
            escrever_devagar("Fim de jogo.")
            break

jogo()
