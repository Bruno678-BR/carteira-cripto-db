from database import DBConnection
from repository import CriptoRepository
db = DBConnection()

conexao = db.connect()

if conexao is not None:
    print("Conexão ativa! Preparando o repositório de dados...")

    repo = CriptoRepository(conexao)

    repo.save(codigo = "BTC",data_cripto = "2026-07-05 15:30:00",preco_moeda = 350000.00)
    db.disconnect()