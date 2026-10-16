import time
import sys
import os

class Pessoa:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.__cpf = cpf

    def get_cpf(self) -> str:
        return self.__cpf

    def set_cpf(self, novo_cpf: str):
        cpf_numeros = novo_cpf.replace(".", "").replace("-", "")
        if cpf_numeros.isdigit() and len(cpf_numeros) == 11:
            self.__cpf = cpf_numeros
        else:
            print("CPF inválido, não foi alterado")

    def autenticar(self, cpf_digitado: str) -> bool:
        cpf_numeros = cpf_digitado.replace(".", "").replace("-", "")
        if not cpf_numeros.isdigit() or len(cpf_numeros) != 11:
            return False
        return cpf_numeros == self.__cpf


class Aluno(Pessoa):
    def __init__(self, nome: str, cpf: str, matricula: int, data_de_nascimento: str, idade: int):
        super().__init__(nome, cpf)
        self.matricula = matricula
        self.data_de_nascimento = data_de_nascimento
        self.idade = idade
        self.notas = []
        self.presencas = []

    def fazer_atividade(self) -> None:
        pass

    def assinar_chamada(self) -> bool:
        pass

    def apresentar_trabalho(self) -> None:
        pass

    def fazer_prova(self) -> None:
        pass


class Professor(Pessoa):
    def __init__(self, nome: str, cpf: str, matricula_professor: int, telefone: str, endereco: str, quantidade_disciplinas:int, carga_horaria:int):
        super().__init__(nome, cpf)
        self.__matricula_professor = matricula_professor
        self.telefone = telefone
        self.endereco = endereco
        self.quantidade_disciplinas = quantidade_disciplinas
        self.carga_horaria = carga_horaria
        self.alunos = []
        self.trabalhos = []

    def vincular_aluno(self, aluno: Aluno):
        self.alunos.append(aluno)

    def realizar_chamada(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
            return
        for aluno in self.alunos:
            resposta = input(f"{aluno.nome} está presente? (s/n): ").strip().lower()
            while resposta not in ("s", "n"):
                print("Responda a chamada da maneira correta!")
                resposta = input(f"{aluno.nome} está presente? (s/n): ").strip().lower()

            presente = resposta == "s"
            aluno.presencas.append(presente)
        print("Chamada registrada com sucesso.")

    def cadastrar_trabalho(self, titulo: str):
        self.trabalhos.append(titulo)
        print(f"Trabalho '{titulo}' cadastrado.")

    def lancar_nota(self, aluno: Aluno, nota: float):
        aluno.notas.append(nota)
        print(f"Nota {nota} lançada para {aluno.nome}.")

    def listar_alunos(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
            return
        for i, aluno in enumerate(self.alunos, start=1):
            print(f"{i} - {aluno.nome} (matrícula: {aluno.matricula})")

    def emitir_boletim(self, aluno: Aluno):
        media = sum(aluno.notas) / len(aluno.notas) if aluno.notas else 0
        total_aulas = len(aluno.presencas)
        presencas = aluno.presencas.count(True)
        frequencia = (presencas / total_aulas * 100) if total_aulas > 0 else 0

        print(f"\n--- Boletim de {aluno.nome} ---")
        print(f"Notas: {aluno.notas}")
        print(f"Média: {media:.2f}")
        print(f"Frequência: {frequencia:.1f}%")


class Direcao:
    def __init__(self, id_direcao: int, nome_diretor: str, tipo_diretor: str):
        self.id_direcao = id_direcao
        self.nome_diretor = nome_diretor
        self.tipo_diretor = tipo_diretor
        self.turmas = []       
        self.disciplinas = []  

    def cadastrar_aluno(self) -> bool:
        pass

    def cadastrar_professor(self) -> bool:
        pass

    def cadastrar_turma(self) -> bool:
        pass

    def emitir_declaracao(self) -> str:
        pass

    def enviar_aviso(self) -> bool:
        pass

    def consultar_aluno(self) -> "Aluno":
        pass

    def consultar_professor(self) -> "Professor":
        pass

    def cadastrar_disciplina(self) -> bool:
        pass


class Turma:
    def __init__(self, id_turma: int, nome_turma: str, sala: str,quantidade_alunos: int, nome_cordenacao: str):
        self.id_turma = id_turma
        self.nome_turma = nome_turma
        self.sala = sala
        self.quantidade_alunos = quantidade_alunos
        self.nome_cordenacao = nome_cordenacao
        self.alunos = []       
        self.disciplinas = []  

    def adicionar_aluno(self) -> bool:
        pass

    def remover_aluno(self) -> bool:
        pass

    def listar_alunos(self) -> list:
        pass

    def verificar_vagas(self) -> int:
        pass

    def reservar_sala(self) -> bool:
        pass

    def reservar_laboratorio(self) -> bool:
        pass

    def atualizar_quantidade_alunos(self) -> int:
        pass


class Disciplina:
    def __init__(self, id_disciplina: int, nome: str, carga_horaria: int, conteudo: str):
        self.id_disciplina = id_disciplina
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.conteudo = conteudo

    def atualizar_nome(self) -> bool:
        pass

    def atualizar_conteudo(self) -> bool:
        pass

    def definir_carga_horaria(self) -> bool:
        pass

    def validar_carga_horaria(self) -> bool:
        pass

    def obter_resumo(self) -> str:
        pass