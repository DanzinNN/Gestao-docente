# Gestão Docente

Sistema de gestão acadêmica em Python, com foco nas ações do **professor**: cadastro, chamada, lançamento de notas, cadastro de trabalhos e emissão de boletim. Desenvolvido como projeto de estudo de Programação Orientada a Objetos (POO).

## Funcionalidades

- Cadastro de professor (nome, CPF, matrícula, telefone, endereço, disciplinas, carga horária)
- Vínculo de alunos ao professor
- Realização de chamada (registro de presença/falta)
- Lançamento de notas por aluno
- Cadastro de trabalhos/atividades
- Listagem de alunos vinculados
- Emissão de boletim (média de notas e percentual de frequência)
- Validação de CPF (11 dígitos numéricos)
- Tratamento de erros de entrada (ex: letras em campos numéricos)

## Estrutura do projeto

```
├── main.py      # ponto de entrada, menu interativo
├── models.py    # classes do sistema (Pessoa, Aluno, Professor)
├── utils.py     # animações de ligar e desligar
└── README.md
```

## Classes

### `Pessoa`
Classe base com atributos e comportamentos comuns a qualquer pessoa do sistema.
- `nome: str`
- `cpf: str` (privado, com `get_cpf()` e `set_cpf()`)
- `autenticar(cpf_digitado: str) -> bool`

### `Aluno` (herda de `Pessoa`)
- `matricula: int`
- `data_de_nascimento: str`
- `idade: int`
- `notas: list` — notas lançadas pelo professor
- `presencas: list` — histórico de presença/falta

### `Professor` (herda de `Pessoa`)
- `matricula_professor: int` (privado)
- `telefone: str`
- `endereco: str` (privado)
- `quantidade_disciplinas: int`
- `carga_horaria: int`
- `alunos: list` — alunos vinculados
- `trabalhos: list` — trabalhos cadastrados

**Métodos:**
- `vincular_aluno(aluno)` — associa um aluno ao professor
- `realizar_chamada()` — registra presença/falta de cada aluno vinculado
- `cadastrar_trabalho(titulo)` — cadastra um novo trabalho/atividade
- `lancar_nota(aluno, nota)` — lança uma nota para o aluno
- `listar_alunos()` — lista os alunos vinculados
- `emitir_boletim(aluno)` — exibe notas, média e frequência do aluno

## Como executar

```bash
python main.py
```

O sistema abre um menu interativo no terminal:

```
=== Menu do Professor ===
1 - Fazer chamada
2 - Lançar nota
3 - Cadastrar trabalho
4 - Listar alunos
5 - Emitir boletim
0 - Sair
```

## Requisitos

- Python 3.10+ (por causa dos type hints usados, como `list[str]`)

## Possíveis melhorias futuras

- Persistência de dados (salvar em arquivo ou banco de dados)
- Classes `Turma`, `Disciplina` e `Direcao` (já modeladas em diagrama UML)
- Autenticação real com hash de senha
- Validação completa de CPF (dígitos verificadores)

## Autor

Daniel Guimarães Souza — [GitHub](https://github.com/DanzinNN)
