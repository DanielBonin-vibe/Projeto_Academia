from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = 'sqlite:///database/academia.db'  # Estamos indicando qual banco queremos utilizar
 
class Base(DeclarativeBase):    # Uma classe base para todos os nossos models
    pass

engine = create_engine(DATABASE_URL, echo=False,) # Criamos 'engine' e passamos 'DABASE_URL', indicando com quem o engine vais e comunicar, o 'echo' faz com que o comando mostre os comandos SQL no terminal ou não.

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False,)    # 'bind=engine' indica que que toda sessão criada pelo SessionLocal deve utilizar esse 'engine' ; 'autoflush' serve para enviar automaticamente alteraçõies pendentes ; 'autocommit' salva autotomaticamente.

# sessionmaker -> Usado para criar sessões no banco de dados
# engine -> Objeto responsável por conversar com o banco
# Sessionlocal -> Serve para criar criar sessões, é uma fábrica de sessões
# session -> É um objeto que normalmente utilizamos para trabalhar com os dados. no caso, 'Session' é aquilo que nosso código trabalha diretamente.

# Base -> models/tabelas
# Engine -> Conexão com o banco
# Session -> Operações no banco.