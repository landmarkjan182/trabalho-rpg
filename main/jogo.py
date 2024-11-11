import os
from escrever_devagar import escrever_devagar
from status import exibir_status
from historico import exibir_historico 
from criar_personagem import criar_personagem
from bau import desafio_bau

os.system('clear')

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