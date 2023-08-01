def verifica_opcao(opcao):
    if opcao < 1 or opcao > 7: # Verifica se a opção está fora do intervalo válido (1 a 7)
        raise ValueError("Escolha uma das opções disponíveis!\n")