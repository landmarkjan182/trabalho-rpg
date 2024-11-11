from escrever_devagar import escrever_devagar
from random import randint
def ataque_geral(personagem, monstro):
    dado20_personagem = randint(1, 20)  
    resultado_ataque = dado20_personagem + personagem["ataque"]  
    personagem["dado_ataque"] = dado20_personagem 

    escrever_devagar(f"Rolando os dados do ataque = {dado20_personagem} + {personagem['ataque']} = {resultado_ataque}")

    if dado20_personagem == 20:
        escrever_devagar("Acerto Crítico!")
        return (personagem["ataque"] * 2) - monstro["defesa"]
    
   
    if esquiva_do_monstro(monstro, personagem):
        return 0
    
    if resultado_ataque >= monstro["defesa"]:
        escrever_devagar("Você atacou o monstro!!")
        return personagem["ataque"] - monstro["defesa"]
    else:
        escrever_devagar("O ataque falhou!")
        return 0

def esquiva_do_monstro(monstro, personagem):
    dado20_monstro = randint(1, 20) 
    resultado_esquiva = dado20_monstro + monstro["esquiva"] 
 
    dado20_personagem = personagem.get("dado_ataque", 0) 
    
    escrever_devagar(f"O monstro tenta esquivar: {dado20_monstro} + {monstro['esquiva']} = {resultado_esquiva}")
    
    if resultado_esquiva > dado20_personagem + personagem["ataque"]:
        escrever_devagar("O monstro esquivou do seu ataque!")
        return True 
    else:
        escrever_devagar("O monstro falhou em esquivar!")
        return False  