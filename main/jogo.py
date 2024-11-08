import os
from random import randint
import time

os.system('clear')

def escrever_devagar(texto, intervalo=0.05):
    for caractere in texto:
        print(caractere, end='', flush=True)
        time.sleep(intervalo)
    print()
def exibir_opcoes_de_vocacao_raca():
   
    escrever_devagar("🛡️ **Opções de Vocação**:")
    escrever_devagar("⚔️ **Guerreiro (G):** +2 Ataque, +1 Defesa, -1 Esquiva")
    escrever_devagar("🏹 **Arqueiro (A):** +2 Ataque, -1 Defesa, +1 Esquiva, -1 Vida")
    escrever_devagar("🛡️ **Paladino (P):** +1 Ataque, +1 Defesa, -1 Esquiva, +1 Vida")

    
    escrever_devagar("\n🌍 **Opções de Raça**:")
    escrever_devagar("🛠️ **Anão (A):** +1 Defesa, +2 Vida")
    escrever_devagar("🌲 **Elfo (E):** +2 Esquiva, +1 Ataque")
    escrever_devagar("👨‍🦰 **Humano (H):** +1 Ataque, +1 Defesa, +1 Esquiva, +1 Vida")
    print("\n")    

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

def exibir_status(personagem):
    print(f"\n🌟 **Status de {personagem['nome']}:**")
    escrever_devagar(f"💖 **Vida**: {personagem['vida']} / {personagem['vida_total']}")
    escrever_devagar(f"⚔️ **Ataque**: {personagem['ataque']}")
    escrever_devagar(f"🛡️ **Defesa**: {personagem['defesa']}")
    escrever_devagar(f"💨 **Esquiva**: {personagem['esquiva']}")
    escrever_devagar(f"🎮 **Nível**: {personagem['nivel']}")
    escrever_devagar(f"✨ **Experiência**: {personagem['exp']}")
    print("\n")

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
            
            acao = input("Ação: ").upper()           
            if acao in ["A", "D", "E", "F", "M"]:
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
    escrever_devagar("\n🗺️ Você está explorando... procurando por tesouros... 🗺️")
    time.sleep(1)
    desafio = randint(1, 20)

    if desafio <= 4:
        escrever_devagar("\n🎉 Você encontrou um baú brilhante! 🎉\n")
        time.sleep(1)
        escrever_devagar("Abrindo o baú...")
        time.sleep(1)

        if randint(1, 10) == 1: 
            escrever_devagar("⚠️ Mas espere... algo está errado... ⚠️")
            time.sleep(1)
            escrever_devagar("\n😈 O baú se transformou em um Mimético! 😈\n")
            combate(personagem, "mimico")
        else:
            if abrir_bau():
                escrever_devagar("\n💖 Você recuperou 50% da sua vida! 💖")
                personagem["vida"] = min(personagem["vida_total"], personagem["vida"] + personagem["vida_total"] // 2)

    elif desafio == 20:
        escrever_devagar("\n🌋 Você encontrou o temível Lorde Demônio! 🌋")
        combate(personagem, "lorde_demonio")

    else:
        tipo_monstro = "goblim" if desafio <= 10 else "ogro" if desafio <= 15 else "dragao"
        escrever_devagar(f"\n⚔️ Você encontrou um {tipo_monstro} pronto para lutar! ⚔️")
        combate(personagem, tipo_monstro)

def abrir_bau():
    tentativas = 3
    escrever_devagar("\n🔑 Tentando abrir o baú... 🔑\n")
    for i in range(tentativas):
        rolagem = randint(1, 20)
        escrever_devagar(f"🔍 Tentativa {i + 1}: Você rolou {rolagem}")
        time.sleep(0.5)
        if rolagem >= 10:
            escrever_devagar("\n🎉 Baú aberto com sucesso! 🎉")
            return True
        else:
            escrever_devagar("\n🔒 O baú não abriu... tentando novamente 🔒\n")
    escrever_devagar("\n💀 Você falhou em abrir o baú. 💀")
    return False


def jogo():
    os.system("clear")
    sair = input("Você deseja entrar na caverna? (S/N): ").upper()
    if sair == 'N':
        return
    personagem = criar_personagem()
    exibir_status(personagem)
    
    while personagem["vida"] > 0:
        escrever_devagar("Escolha sua próxima ação: B=Enfrentar Batalha, H=Ver Histórico de Batalhas, S=Sair do Jogo")
        opcao = input("Ação: ").upper()
        
        if opcao == "B":
            desafio_bau(personagem)
            if personagem["vida"] <= 0:
                escrever_devagar("Você morreu... Fim de jogo.")
                exibir_status(personagem)
                break
        
        elif opcao == "H":
            exibir_historico(personagem)
        
        elif opcao == "S":
            escrever_devagar("Fim de jogo.")
            exibir_status(personagem)
            break
        else:
            escrever_devagar("Opção inválida! Escolha B, H ou S.")

jogo()

