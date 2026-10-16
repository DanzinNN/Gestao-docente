from models import *
from utils import *

professor_cadastro = None
alunos_cadastrados = [
    Aluno("Ana Souza", "11122233344", 2001, "12/03/2005", 20),
    Aluno("Carlos Lima", "22233344455", 2002, "25/07/2004", 21),
    Aluno("Mariana Costa", "33344455566", 2003, "08/01/2006", 19),
    Aluno("Pedro Alves", "44455566677", 2004, "14/09/2003", 22),
    Aluno("Juliana Pires", "55566677788", 2005, "30/11/2005", 19),
    Aluno("Rafael Nogueira", "66677788899", 2006, "03/05/2004", 21),
    Aluno("Beatriz Martins", "77788899900", 2007, "19/02/2006", 19),
    Aluno("Lucas Ferreira", "88899900011", 2008, "27/10/2003", 22),
    Aluno("Camila Rodrigues", "99900011122", 2009, "11/06/2005", 20),
    Aluno("Gustavo Barbosa", "10011122233", 2010, "05/04/2004", 21),
    Aluno("Fernanda Castro", "12121212121", 2011, "22/08/2005", 20),
    Aluno("Thiago Mendes", "13131313131", 2012, "16/12/2003", 22),
    Aluno("Larissa Teixeira", "14141414141", 2013, "09/03/2006", 19),
    Aluno("Bruno Carvalho", "15151515151", 2014, "01/07/2004", 21),
    Aluno("Isabela Ramos", "16161616161", 2015, "28/09/2005", 20),
]







print("BEM VINDO(A) AO SISTEMA DE GESTÃO DO DOCENTE!")
input("Aperte enter para iniciar")
animacao_incialializador()

while True:
    print("\n=== Menu do Professor ===")
    print("1 - Cadastrar Professor")
    print("2 - Fazer chamada")
    print("3 - Lançar nota")
    print("4 - Cadastrar trabalho")
    print("5 - Listar alunos")
    print("6 - Emitir boletim")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao in (2, 3, 4, 5, 6) and professor_cadastro is None:
        print("Você precisa cadastrar o professor primeiro (opção 1).")
        time.sleep(2)
        os.system('cls')
        continue

    if opcao == 1:
            os.system('cls')
            print("Vamos realizar seu cadastro!")
            nome = input("Digite seu nome:")
            cpf = input("Digite seu cpf:")
            while True:
                try:
                    matricula = int(input("Digite sua matricula:"))
                    break
                except ValueError:
                    print("Digite apenas números.")
            telefone = input("Digite seu telefone:")
            endereco_prof = input("Digite seu endereço:")
            while True:
                try:
                    quantidade_disciplina = int(input("Digite quantidade de disciplinas:"))
                    break
                except ValueError:
                    print("Digite apenas números.")
            while True:
                try:
                    carga_hora = int(input("Digite a carga horária:"))
                    break
                except ValueError:
                    print("Digite apenas números.")

            professor_cadastro = Professor(nome, cpf, matricula, telefone, endereco_prof, quantidade_disciplina, carga_hora)

            print("Professor cadastrado!")
            print(f"Nome: {nome}\nMatricula: {matricula}")
            for aluno in alunos_cadastrados:
                professor_cadastro.vincular_aluno(aluno)
            time.sleep(4)
            os.system('cls')
    elif opcao == 2:
        os.system('cls')
        professor_cadastro.realizar_chamada()

    elif opcao == 3:
        os.system('cls')
        while True:
            professor_cadastro.listar_alunos()
            if professor_cadastro.alunos:
                try:
                    indice = int(input("Número do aluno: ")) - 1
                    if 0 <= indice < len(professor_cadastro.alunos):
                        nota = float(input("Nota: "))
                        professor_cadastro.lancar_nota(professor_cadastro.alunos[indice], nota)
                        time.sleep(4)
                        os.system('cls')
                        break
                    else:
                        print("Aluno inválido.")
                        time.sleep(4)
                        os.system('cls')
                except ValueError:
                    print("Digite apenas números")
                    time.sleep(4)
            else:
                print("Nenhum aluno cadastrado")
                break

    elif opcao == 4:
        os.system('cls')
        titulo = input("Título do trabalho: ")
        professor_cadastro.cadastrar_trabalho(titulo)

    elif opcao == 5:
        os.system('cls')
        professor_cadastro.listar_alunos()

    elif opcao == 6:
        os.system('cls')
        professor_cadastro.listar_alunos()
        if professor_cadastro.alunos:
            indice = int(input("Número do aluno: ")) - 1
            if 0 <= indice < len(professor_cadastro.alunos):
                professor_cadastro.emitir_boletim(professor_cadastro.alunos[indice])
            else:
                print("Aluno inválido.")

    elif opcao == 0:
        animacao_desligamento()
        os.system('cls')
        break

    else:
        print("Opção inválida.")