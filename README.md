Sistema de gerenciamento de academia desenvolvido em **Python** utilizando Programação Orientada a Objetos (POO) e persistência de dados com JSON.

O projeto foi criado com o objetivo de praticar conceitos fundamentais da linguagem Python, organização de código e modelagem orientada a objetos.

---

# 🚀 Funcionalidades

### Alunos
- ✅ Matricular aluno
- ✅ Listar alunos
- ✅ Buscar aluno por CPF
- ✅ Alterar plano

### Professores
- ✅ Cadastrar professor
- ✅ Listar professores
- ✅ Buscar professor por CPF
- ✅ Remover professor

### Persistência de dados
- ✅ Salvamento automático em arquivos JSON
- ✅ Carregamento automático ao iniciar o sistema
- ✅ Conversão de objetos para dicionários (`to_dict`)
- ✅ Reconstrução de objetos (`from_dict`)

---

# 🧠 Conceitos utilizados

- Programação Orientada a Objetos (POO)
- Classes
- Objetos
- Encapsulamento
- Métodos
- Atributos
- Class Methods (`@classmethod`)
- Serialização de objetos
- Persistência de dados com JSON
- Organização em módulos
- Importação entre arquivos
- Manipulação de arquivos
- Estruturas de repetição
- Estruturas condicionais

---

# 📁 Estrutura do projeto

```
Projeto_Academia/
│
├── models/
│   ├── academia.py
│   ├── aluno.py
│   ├── professor.py
│   ├── plano.py
│   └── mensalidade.py
│
├── utils/
│   └── persistencia.py
│
├── dados/
│   ├── alunos.json
│   └── professores.json
│
├── main.py
└── README.md
```

---

# 💾 Persistência

Os dados são armazenados em arquivos JSON.

Cada objeto é convertido para um dicionário utilizando o método:

```python
to_dict()
```

Quando o sistema inicia, os dados são reconstruídos através do método:

```python
from_dict()
```

Dessa forma, todas as informações permanecem salvas mesmo após o encerramento do programa.

---

# ▶️ Como executar

Clone o repositório:

```bash
git clone https://github.com/DanielBonin-vibe/Projeto_Academia.git
```

Entre na pasta:

```bash
cd Projeto_Academia
```

Execute:

```bash
python main.py
```

---

# 📚 Objetivo

Este projeto faz parte da minha jornada de estudos em Python.

O foco principal foi praticar:

- Programação Orientada a Objetos
- Organização de projetos
- Persistência de dados
- Manipulação de arquivos
- Boas práticas de programação

---

# 👨‍💻 Autor

Desenvolvido por **Daniel Bonin**.

GitHub:
https://github.com/DanielBonin-vibe
