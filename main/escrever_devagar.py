import time
def escrever_devagar(texto, intervalo=0.05):
    for caractere in texto:
        print(caractere, end='', flush=True)
        time.sleep(intervalo)
    print()