import random
from random import randint
nome_jogador = ()
def caverna():
    r1 = input("Voce quer entrar na caverna? (Sim, Nao): ").strip().lower()
    if r1 == "sim":
        print("Voce entrou na caverna!")
        ale = random.randint(1, 2)
        
        if ale == 1:
            print("Uau voce encontrou um bau!")
            ale1 = random.randint(1, 100)
            
            if ale1 <= 10:
                #Mateus coloque as estatisticas do mimico
                print("Voce encontrou um mimico!!!")
            elif ale1 > 10 and ale1 <= 60:
                print("Parabens! Voce encontrou uma pocao")
            elif ale1 > 60:
                ("Voce nao encontrou nada kk")
        elif ale == 2:
            #brilha mateus kk
            print("Voce encontrou um monstro!")
    elif r1 == "Nao":
        print(f"Ok {nome_jogador} volte mais tarde")        