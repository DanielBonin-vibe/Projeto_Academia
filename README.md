🏋️ Sistema de Academia

Sistema de gerenciamento de academia desenvolvido em Python utilizando SQLite3 como banco de dados.

O projeto foi desenvolvido com o objetivo de praticar conceitos de programação, persistência de dados e banco de dados relacionais, utilizando uma aplicação Python integrada ao SQLite.

🚀 Funcionalidades:

👤 Alunos:

- Cadastro de alunos
- Listagem de alunos
- Busca de alunos
- Desmatrícula de alunos
- Associação do aluno a um plano
- Criação automática da mensalidade durante a matrícula

💰 Controle financeiro:

- Consulta do status financeiro do aluno
- Verificação do plano contratado
- Consulta do valor do plano
- Verificação se a mensalidade está paga ou pendente

🏋️ Planos:

- Cadastro e armazenamento de planos
- Definição do valor de cada plano
- Associação dos planos aos alunos e mensalidades
- 
👨‍🏫 Professores:

- Cadastro de professores
- Listagem de professores
- Busca de professores
- Remoção de professores

🗄️ Banco de Dados

O sistema utiliza SQLite3 para persistência dos dados.

O banco possui as seguintes tabelas:

aluno:
Armazena os dados dos alunos e seu respectivo plano.

id_aluno — chave primária
nome
idade
cpf
id_plano — chave estrangeira

plano:
Armazena os planos disponíveis na academia.

id_plano — chave primária
nome_plano
valor

mensalidade:
Relaciona o aluno ao seu plano e controla o pagamento.

id_mensalidade — chave primária
id_aluno — chave estrangeira
id_plano — chave estrangeira
pago

professor:
Armazena os dados dos professores.

id_professor — chave primária
nome
idade
cpf
especialidade

🔗 Relacionamentos:

O banco utiliza chaves estrangeiras (Foreign Keys) para relacionar as tabelas.

PLANO
  │
  ├──────────────┐
  ↓              ↓
ALUNO       MENSALIDADE
  │              ↑
  └──────────────┘

O aluno possui um id_plano, enquanto a mensalidade possui referências ao aluno e ao plano.

Dessa forma, o sistema consegue consultar informações relacionadas utilizando JOIN.

🧠 Conceitos praticados

Durante o desenvolvimento foram utilizados diversos conceitos de Python e SQL:

- Python
- SQLite3
- CRUD
- INSERT
- SELECT
- UPDATE
- DELETE
- WHERE
- LIKE
- JOIN
- Primary Key (PK)
- Foreign Key (FK)
- cursor
- commit()
- close()
- lastrowid
- Funções (def)
- Classes
- Modularização
- Organização de projeto
- 
📁 Estrutura do projeto
Projeto_Academia/
│
├── database/
│   └── academia.db
│
├── models/
│   ├── academia.py
│   ├── aluno.py
│   ├── mensalidade.py
│   ├── plano.py
│   └── professor.py
│
├── utils/
│   └── banco_de_dados.py
│
├── main.py
└── README.md

▶️ Como executar

1. Clone o repositório
git clone <URL_DO_REPOSITORIO>
2. Entre na pasta do projeto
cd Projeto_Academia
3. Execute o programa
python main.py

📌 Fluxo de matrícula:
Ao cadastrar um aluno, o sistema recebe o id_plano.

Depois de inserir o aluno no banco, o sistema utiliza lastrowid para obter o ID recém-criado e cria automaticamente sua mensalidade.

Cadastro do aluno
       ↓
Escolha do plano
       ↓
Aluno cadastrado
       ↓
lastrowid
       ↓
Mensalidade criada
       ↓
Pagamento = pendente

🔎 Status financeiro:
O status financeiro utiliza o relacionamento entre mensalidade e plano.

Por meio de JOIN, o sistema consegue consultar:

Plano contratado
Valor do plano
Situação do pagamento
mensalidade
     │
     │ id_plano
     ↓
   plano
     │
     ├── nome_plano
     └── valor
🎯 Objetivo do projeto

Este projeto faz parte dos estudos de Python e Banco de Dados, tendo como principal objetivo colocar em prática conceitos de programação e SQL em uma aplicação funcional.

O projeto também serve como base para futuras melhorias, como novos recursos de gerenciamento, controle financeiro e evolução da estrutura do banco de dados.

Desenvolvido para estudos de Python, SQLite3 e Banco de Dados.
