
def EscolaCoodenacao():
    cadPessoa = int(input("Quem você quer cadastrar:" \
    "\n Aluno - 1;" \
    "\n Professor - 2" \
    "\n Ninguem - qualquer número." \
    "\n Qual será a sua opção: "))

    if cadPessoa == 1:
        print("--- Cadastro Aluno ---")
        nome = input("Qual o nome do aluno: ")
        email = input("E-mail do aluno: ")
        cpf = input("CPF do aluno: ")

        print("--- Cadastro Realizado ---")

        print("Nome: ", nome, "" \
        "\nE-mail: ", email, "" \
        "\nCPF: ", cpf)

        print("--------------------------------------")

    elif cadPessoa == 2:
        print("--- Cadastro Professor ---")
        nome = input("Qual o nome do professor: ")
        email = input("E-mail do professor: ")
        cpf = input("CPF do professor: ")
        areaM = input("Matéria do professor: ")

        print("--- Cadastro Realizado ---")

        print("Nome: ", nome, "" \
        "\n E-mail: ", email, "" \
        "\n CPF: ", cpf)

        print("--------------------------------------")

    else:
        print("--------------------------------------")
        print("Tudo bem, então vá para o próximo passo!")
        print("--------------------------------------")

        def Escola():
            funcao = int(input("Digite 1 se você for professor;" \
            "\nDigite 2 se você é aluno." \
            "\nQual sua função: "))

            print("--------------------------------------")

            if funcao == 1:
                professor = int(input("O que você quer fazer:" \
                "\n Digite 1 para cadastrar avaliação do aluno;" \
                "\n Digite 2 para reservar um equipamento" \
                "\n Digite 3 para colocar falta." \
                "\n Qual será: "))

                if professor == 1:
                    print("--- Cadastro Aluno ---")
                    nome = input("Nome do aluno: ")
                    materia = input("Qual a matéria: ")
                    nota = int(input("Nota: "))

                    print("--- Alunos Salvados ---")

                    print("Nome: ", nome, "\n" \
                    "Matéria: ",materia, "\n" \
                    "Nota: ", nota)

                    print("--------------------------------------")

                elif professor == 2:

                    data = []
                    contador = 0

                    equipamento = input("Qual equipamento o senhor gostaria de reservar: ")
                    dat = input("Qual o dia desse mês o senhor gostaria de fazer a reserva: ")
                    data.append(dat)

                    gt = input("voce gostaria de adicionar mais um dia: ")
                    qd = int(input("quantos dias (você pode adicionar até mais 4 dias): "))
                    
                    if gt == "Sim" or gt == "sim":

                        for contador in range(qd):

                            dat = input("qual dia (digite 1 por vez): ")
                            data.append(dat)
                            

                    ordenada = sorted(data)

                    print("\n--- Equipamento Reservado ---")

                    print("Equipamento: ", equipamento, "\n" \
                    "Dia(s): ", ordenada)

                    print("--------------------------------------")

                    
                        
                elif professor == 3:
                    nomeAluno = input("Qual o nome do aluno: ")
                    materiaF = input("Qual matéria ele faltou: ")
                    dia = input("Qual o dia: ")

                    print("--- Falta Registrada ---")

                    print("Nome: ", nomeAluno, "\n" \
                    "Matéria: ",materiaF, "\n" \
                    "Dia: ", dia)

                    print("--------------------------------------")

                else: 
                    print("--------------------------------------")
                    print("Falha! Reinicie o sistema e tente novamente!")
                    print("--------------------------------------")

            elif funcao == 2:
                aluno = int(input("O que você quer fazer:" \
                "\n Digite 1 para fazer uma reclemação para a gestão;" \
                "\n Digite 2 para reservar um livro" \
                "\n Digite 3 para justificar falta." \
                "\n Qual será: "))

                if aluno == 1:
                    print("--- Reclamação ---")
                    reclamacao = input("Escreva a sua reclamação: ")

                    print("--- Reclamação Salva ---")

                    print(reclamacao)

                    print("--------------------------------------")

                elif aluno == 2:
                    livro = input("Qual livro gostaria de reservar: ")
                    dias = input("Por quantos dias: ")

                    print("--- Livro Reservado ---")

                    print("Livro: ", livro, "\n" \
                    "Dias: ", dias)

                    print("--------------------------------------")

                elif aluno == 3:
                    nomeAlunoF = input("Qual o seu nome: ")
                    materiaa = input("Qual matéria faltou: ")
                    diaF = input("Qual o dia: ")
                    motivo = input("Digite o seu motivo: ")

                    print("--- Falta Justificada ---")

                    print("Nome: ", nomeAlunoF, "\n" \
                    "Matéria: ",materiaa, "\n" \
                    "Dia: ", diaF, "\n" \
                    "Motivo: ", motivo)

                    print("--------------------------------------")

                else: 
                    print("--------------------------------------")
                    print("Falha! Reinicie o sistema e tente novamente!")
                    print("--------------------------------------")

            else:
                print("Ocorreu um erro! Reinicie o sistema e tente novamente!")

        Escola()

def Refeitorio():
    sn = int(input("Você gostaria de saber o cadápio da semana?" \
    "\n Digite 1 se for sim;" \
    "\n Digite qulaquer número se for não." \
    "\n Gostaria: "))
    print("--------------------------------------")

    if sn == 1:
        print("--- SEGUNDA ---" \
        "\nMANHÃ - Sopa com pão;" \
        "\nALMOÇO - Carne, arroz, feijão, farofa e salada;" \
        "\nTARDE - Bolacha com suco.")
        print("--------------------------------------")

        print("--- TERÇA ---" \
        "\nMANHÃ - Pão com patê;" \
        "\nALMOÇO - Frango cozido, arroz, feijão, farofa de cuscuz e beterraba;" \
        "\nTARDE - Bolo.")
        print("--------------------------------------")

        print("--- QUARTA ---" \
        "\nMANHÃ - Sopa de carne com torrada;" \
        "\nALMOÇO - Paçoca, arroz, feijão, farofa e salada;" \
        "\nTARDE - Bruaca.")
        print("--------------------------------------")

        print("--- QUINTA ---" \
        "\nMANHÃ - Bolacha doce;" \
        "\nALMOÇO - Frango assado, arroz, feijão, farofa e salada com cenoura ralada;" \
        "\nTARDE - Torta de frango.")
        print("--------------------------------------")

        print("--- SEXTA ---" \
        "\nMANHÃ - Pão com manteiga com suco;" \
        "\nALMOÇO - Feijoada, arroz, farofa e salada;" \
        "\nTARDE - Bolo.")
        print("--------------------------------------")

    else:
        print("Tudo bem!")
        print("--------------------------------------")

EscolaCoodenacao()
Refeitorio()
