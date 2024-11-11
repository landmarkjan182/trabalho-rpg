from escrever_devagar import escrever_devagar
def exibir_historico(personagem):
    escrever_devagar("\nHistórico de Rodadas de Batalha:")
    if personagem["rodadas"]:
        for rodada, log in enumerate(personagem["rodadas"], start=1):
            escrever_devagar(f"Rodada {rodada}: {log}")
    else:
        escrever_devagar("Nenhuma batalha registrada ainda.")
    print()