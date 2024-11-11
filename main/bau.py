from escrever_devagar import escrever_devagar
import time
from random import randint
from combate import combate
from abrir_bau import abrir_bau
from criar_personagem import criar_personagem
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