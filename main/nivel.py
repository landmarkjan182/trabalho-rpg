from escrever_devagar import escrever_devagar
def subir_de_nivel(personagem):
  
    while personagem["exp"] >= personagem["exp_necessaria"]:
        personagem["exp"] -= personagem["exp_necessaria"]
        personagem["nivel"] += 1
        escrever_devagar(f"Você subiu para o nível {personagem['nivel']}!")
              
        for atributo in ["ataque", "defesa", "vida_total", "esquiva"]:
            aumento = personagem[atributo] // 2  
            personagem[atributo] += aumento
            escrever_devagar(f"{atributo.capitalize()} aumentado para {personagem[atributo]}.")
     
        personagem["exp_necessaria"] = int(personagem["exp_necessaria"] * 1.4)  
        escrever_devagar(f"Experiência necessária para o próximo nível: {personagem['exp_necessaria']}.")