import pandas as pd
import mysql.connector


def conexao_database(database):
    cnx = mysql.connector.connect(
        host='localhost', 
        user='root',
        database=f'{database}')

    return cnx

def conexao_inicial():
    cnx = mysql.connector.connect(
        host='localhost', 
        user='root')
    
    return cnx

def create_database(database, cnx, cursor):
    create_database = (f"CREATE DATABASE {database}")

    cursor.execute(create_database)
    cnx.commit()

def drop_database(database, cnx, cursor):
    drop_database = (f"DROP DATABASE {database}")

    cursor.execute(drop_database)
    cnx.commit()

def create_medals(cnx, cursor):
    create_medals = ("CREATE TABLE medals ( rank INT(10), team VARCHAR(100), gold INT(4), silver INT(4), bronze INT(4), total INT(4), rank_total INT(10))")

    cursor.execute("USE olympics")
    cursor.execute(create_medals)

def delete_table(table, where, cnx, cursor):
    delete_medals = f"DELETE FROM {table} WHERE {where}"

    cursor.execute(delete_medals)
    cnx.commit()

def insert_medals(cnx, cursor):
    rank_medalhas = pd.read_excel("Olimpiedas dados\Medals.xlsx")
    for i in range(0, len(rank_medalhas)):
        rank = rank_medalhas["Rank"][i]
        team = rank_medalhas["Team/NOC"][i]
        gold = rank_medalhas["Gold"][i]
        silver = rank_medalhas["Silver"][i]
        bronze = rank_medalhas["Bronze"][i]
        total = rank_medalhas["Total"][i]
        rank_total = rank_medalhas["Rank by Total"][i]

        insert_medals = f"""INSERT INTO medals (rank, team, gold, silver, bronze, total, rank_total) VALUES ({rank}, "{team}", {gold}, {silver}, {bronze}, {total}, {rank_total})"""

        cursor.execute(insert_medals)
        cnx.commit()

def drop_table(table, cnx, cursor):
    drop_table = f"DROP TABLE {table}"
    
    cursor.execute(drop_table)
    cnx.commit()

def command(command, cnx, cursor):
    com = f"{command}"

    cursor.execute(com)
    cnx.commit()

def show_databases(cnx, cursor):
    cursor.execute("SHOW DATABASES")
    cont = 1
    print("\n---------------------------------------")
    for database in cursor:
        print(f"{cont} - {database[0]}")
        cont += 1
    
    print("---------------------------------------\n")

def menu_inicial():
    print("\n----------------------------------------------------")
    print("------------------------MENU------------------------")
    print("1 - Se conectar ao banco de dados (Se conecte a um database para conseguir manipular as tabelas)")
    print("2 - Criar novo banco de dados")
    print("3 - Excluir algum banco de dados")
    print("4 - Executar algum comando no MySQL")
    print("5 - Mostrar os bancos de dados existentes")
    print("6 - Mostrar esse menu novamente")
    print("----------------------------------------------------")
    print("----------------------------------------------------")

def menu_tabela():
    print("\n----------------------------------------------------")
    print("------------------------MENU------------------------")
    print("1 - Se conectar ao banco de dados (Se conecte a um database para conseguir manipular as tabelas)")
    print("2 - Criar novo banco de dados")
    print("3 - Excluir algum banco de dados")
    print("4 - Executar algum comando no MySQL")
    print("5 - Mostrar as tabelas existentes")
    print("----------------------------------------------------")
    print("----------------------------------------------------")

def show_tables(cnx, cursor):
    cursor.execute("SHOW DATABASES")
    cont = 1
    print("\n---------------------------------------")
    for database in cursor:
        print(f"{cont} - {database[0]}")
        cont += 1
    
    print("---------------------------------------\n")
    

def inicio():
    print("------------------------------------------------")
    print("OLÁ, ESTE É UM PROGRAMA FEITO PARA O USO DE DADOS")
    print("RELACIONADOS AS OLIMPIEDAS E PARA A MANIPULAÇÃO")
    print("DO MYSQL")
    print("------------------------------------------------")