from escrever_devagar import escrever_devagar
def exibir_status(personagem):
    print(f"\n🌟 **Status de {personagem['nome']}:**")
    escrever_devagar(f"💖 **Vida**: {personagem['vida']} / {personagem['vida_total']}")
    escrever_devagar(f"⚔️ **Ataque**: {personagem['ataque']}")
    escrever_devagar(f"🛡️ **Defesa**: {personagem['defesa']}")
    escrever_devagar(f"💨 **Esquiva**: {personagem['esquiva']}")
    escrever_devagar(f"🎮 **Nível**: {personagem['nivel']}")
    escrever_devagar(f"✨ **Experiência**: {personagem['exp']}")
    print("\n")