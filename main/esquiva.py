from escrever_devagar import escrever_devagar
from random import randint
def funcao_de_esquiva(personagem, monstro, dado_rolado):
    if "esquiva" not in personagem:
        escrever_devagar("Erro: Atributo 'esquiva' não encontrado no personagem.")
        return False
    if "ataque" not in monstro:
        escrever_devagar("Erro: Atributo 'ataque' não encontrado no monstro.")
        return False

    resultado_esquiva_jogador = dado_rolado + personagem["esquiva"] 
    resultado_esquiva_monstro = randint(1, 20) + monstro["esquiva"]
    
    escrever_devagar(f"Rolando os dados do jogador: {dado_rolado} + {personagem['esquiva']} = {resultado_esquiva_jogador}")
    escrever_devagar(f"Rolando os dados do monstro para esquiva: {resultado_esquiva_monstro}")

   
    if resultado_esquiva_jogador > resultado_esquiva_monstro:
        escrever_devagar("Você esquivou do ataque do monstro!")
        return True
    else:
        escrever_devagar("Você não conseguiu esquivar e foi atingido!")
        return False
    