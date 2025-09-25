def cadastroCarro():
    modelo = input("Qual o modelo do seu carro: ")
    cor = input("Qual a cor do seu carro: ")
    AnoCarro = int(input("Qual o ano do seu carro: "))

    print("\n --- FICHA DE CADASTRO --- \n")

    print("Modelo: ", modelo)
    print("Cor: ", cor)
    if AnoCarro > 2020:
        print("Seu carro não é antigo")
    else:
        print("Seu carro é antigo (Está desatualizado)")

cadastroCarro()