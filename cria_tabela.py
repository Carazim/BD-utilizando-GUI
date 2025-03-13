import psycopg2

conexao = psycopg2.connect(
    database ="postgres",
    user ="postgres",
    password ="123456",
    host ="localhost",
    port ="5432"
)
print("Conexao com o banco de Dados aberta com sucesso!")


meu_cursor = conexao.cursor()

if __name__ == '__main__':
    meu_cursor.execute('''
        CREATE TABLE IF NOT EXISTS PRODUTO (
            CODIGO SERIAL PRIMARY KEY,
            NOME VARCHAR(100) NOT NULL,
            PRECO NUMERIC(10, 2) NOT NULL
        );
    ''')

    conexao.commit()
    print("Tabela criada com sucesso!")
    conexao.close()