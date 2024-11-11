from escrever_devagar import escrever_devagar
from random import randint
import time
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