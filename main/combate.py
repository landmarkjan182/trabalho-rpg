from escrever_devagar import escrever_devagar
from random import randint
from esquiva import funcao_de_esquiva
from status import exibir_status
from ataque import ataque_geral
from nivel import subir_de_nivel
import time
from historico import exibir_historico 

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
def combate(personagem, tipo_monstro):
    monstro = monstros[tipo_monstro].copy()
    escrever_devagar(f"\nApareceu um {tipo_monstro}!\n")  
    defesa_temporaria = personagem["defesa"]  
    
    while monstro["vida"] > 0 and personagem["vida"] > 0:
       
        escrever_devagar(f"\n{('❤️')} Vida do Personagem: {personagem['vida']}  |  {tipo_monstro} Vida: {monstro['vida']} {('💀')}\n")
        
        while True:
            escrever_devagar("\nEscolha sua ação:")
            escrever_devagar("A = Atacar ⚔️")
            escrever_devagar("D = Defender 🛡️")
            escrever_devagar("E = Esquivar 🤸")
            escrever_devagar("F = Fugir 🏃")
            escrever_devagar("M = Ver Atributos do Monstro 🦹")
            escrever_devagar("S = Status personagem 🧒")
            
            acao = input("Ação: ").upper()           
            if acao in ["A", "D", "E", "F", "M","S"]:
                break
            else:
                escrever_devagar("Opção inválida! Tente novamente.\n")
        
        if acao == "F":
            chance_fuga = randint(1, 2)
            if chance_fuga == 1:
                escrever_devagar("\nVocê conseguiu fugir com sucesso! 🏃💨\n")
                personagem["rodadas"].append("Fugiu com sucesso")
                return
            else:
                dano_monstro = monstro["ataque"] - defesa_temporaria
                personagem["vida"] -= max(dano_monstro, 0)
                escrever_devagar(f"\nVocê tentou fugir, mas foi atingido e sofreu {max(dano_monstro, 0)} de dano. {('💥')}\n")
                personagem["rodadas"].append(f"Fuga falhou, sofreu {max(dano_monstro, 0)} de dano")
                continue

        elif acao == "E":
            dado_rolado = randint(1, 20) 
            esquivou = funcao_de_esquiva(personagem, monstro, dado_rolado)
            if esquivou:
                personagem["rodadas"].append("Esquivou com sucesso 🤸")
                escrever_devagar("\nVocê esquivou com sucesso! ✨\n")
                continue
            else:
                escrever_devagar("\nVocê não conseguiu esquivar... 😓\n")
        
        elif acao == "D":
            defesa_temporaria = personagem["defesa"] + 2 
            escrever_devagar("\nVocê se defendeu, aumentando sua defesa temporariamente! 🛡️\n")
            personagem["rodadas"].append("Defendeu 🛡️")
        elif acao == "S":
             exibir_status(personagem)
        elif acao == "M":
            escrever_devagar(f"\nAtributos do {tipo_monstro}:")
            escrever_devagar(f"Ataque: {monstro['ataque']}, Defesa: {monstro['defesa']}, Vida: {monstro['vida']}, Esquiva: {monstro['esquiva']} 🦹\n")
            continue    
        else:
            dano_causado = ataque_geral(personagem, monstro)
            monstro["vida"] -= max(dano_causado, 0)
            personagem["rodadas"].append(f"Atacou e causou {max(dano_causado, 0)} de dano ⚔️")
            escrever_devagar(f"\nVocê causou {max(dano_causado, 0)} de dano. Vida do monstro agora é {monstro['vida']}.\n")
        
       
        if monstro["vida"] > 0:
            dano_monstro = monstro["ataque"] - defesa_temporaria
            personagem["vida"] -= max(dano_monstro, 0)
            escrever_devagar(f"\nVocê sofreu {max(dano_monstro, 0)} de dano. {('💥')} Sua vida agora é {personagem['vida']}.\n")
            personagem["rodadas"].append(f"Sofreu {max(dano_monstro, 0)} de dano")

        time.sleep(1)

   
    if personagem["vida"] > 0:
        escrever_devagar(f"\nVocê venceu o combate contra o {tipo_monstro}! {('🎉')}\n")
        personagem["rodadas"].append(f"Venceu o {tipo_monstro}")
        personagem["exp"] += experiencia_monstro[tipo_monstro]
        escrever_devagar(f"\nVocê ganhou {experiencia_monstro[tipo_monstro]} de experiência! {('⭐')}\n")
        subir_de_nivel(personagem)
    else:
        escrever_devagar(f"\nVocê foi derrotado pelo {tipo_monstro}... {('☠️')}\n")
        personagem["rodadas"].append(f"Derrotado pelo {tipo_monstro}")
    
    ver_historico = input("\nDeseja ver o histórico de batalha? (S/N): ").upper()
    if ver_historico == "S":
        exibir_historico(personagem)