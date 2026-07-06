from mysql.connector import Error

class CriptoRepository:
    def __init__ (self,conexao_banco):
        self.connection = conexao_banco
    
    def save(self, codigo, data_cripto, preco_moeda):
        try:
            cursor = self.connection.cursor()
        
            sql = """
                    INSERT INTO precos_cripto (codigo, data_cripto, preco_moeda) 
                    VALUES (%s, %s, %s)
                """
            valores = (codigo, data_cripto, preco_moeda)

            cursor.execute(sql,valores)
            
            self.connection.commit()

            cursor.close()
        except Error as e:
            print(f"Erro ao salvar o repositorio:{e}")
