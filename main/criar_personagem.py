from escrever_devagar import escrever_devagar
from exibir_vocaçao import exibir_opcoes_de_vocacao_raca

status_base = {
    "ataque": 2,
    "defesa": 1,
    "vida": 8,
    "esquiva": 1,
    "exp_necessaria": 100
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

def criar_personagem():
    nome = input("✍️ **Nome do personagem:** ")
    personagem = status_base.copy()
    personagem["nome"] = nome
    personagem["rodadas"] = []
    personagem["nivel"] = 1
    personagem["exp"] = 0
    personagem["vida_total"] = personagem["vida"]
    exibir_opcoes_de_vocacao_raca()

    escrever_devagar("📜 **Escolha sua Vocação**: G=Guerreiro, A=Arqueiro, P=Paladino")
    vocação = ""
    while vocação not in vocações:
        vocação = input("Vocação: ").upper()
        if vocação not in vocações:
            escrever_devagar("Vocação inválida! Por favor, escolha uma vocação válida: G=Guerreiro, A=Arqueiro, P=Paladino")

    escrever_devagar("🌍 **Escolha sua Raça**: A=Anão, E=Elfo, H=Humano")
    raça = ""
    while raça not in raças:
        raça = input("Raça: ").upper()
        if raça not in raças:
            escrever_devagar("Raça inválida! Por favor, escolha uma raça válida: A=Anão, E=Elfo, H=Humano")

    
    for atributo, bonus in vocações[vocação].items():
        personagem[atributo] = personagem.get(atributo, 0) + bonus

    
    for atributo, bonus in raças[raça].items():
        personagem[atributo] = personagem.get(atributo, 0) + bonus

    personagem["vida_total"] = personagem["vida"]
    return personagem
def exibir_historico(personagem):
    escrever_devagar("\nHistórico de Rodadas de Batalha:")
    if personagem["rodadas"]:
        for rodada, log in enumerate(personagem["rodadas"], start=1):
            escrever_devagar(f"Rodada {rodada}: {log}")
    else:
        escrever_devagar("Nenhuma batalha registrada ainda.")
    print()