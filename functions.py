import pandas as pd
import mysql.connector

# MENUS
def inicio():
    print("----------------------------------------------------")
    print("OLÁ, ESTE É UM PROGRAMA FEITO PARA O USO DE DADOS")
    print("RELACIONADOS AS OLIMPIEDAS E PARA A MANIPULAÇÃO")
    print("DO MYSQL")
    print("----------------------------------------------------")

def menu_inicial():
    print("\n----------------------------------------------------")
    print("------------------------MENU------------------------")
    print("1 - Se conectar ao banco de dados (Se conecte a um database para conseguir manipular as tabelas)")
    print("2 - Criar novo banco de dados")
    print("3 - Excluir algum banco de dados")
    print("4 - Executar algum comando no MySQL")
    print("5 - Mostrar os bancos de dados existentes")
    print("6 - Mostrar esse menu novamente")
    print("7 - Entrar no menu de dados das olimpiedas (NÃO ESTÁ PRONTO)")
    print("----------------------------------------------------")
    print("----------------------------------------------------")

def menu_database(database):
    print("\n----------------------------------------------------")
    print("------------------------MENU------------------------")
    print(f"DATABASE: {database}")
    print("1 - Mostrar as tabelas existentes")
    print("2 - Criar alguma tabela (POR FAZER)")
    print("3 - Deletar alguma tabela")
    print("4 - Manipular dados das olimpiedas nesse banco de dados")
    print("5 - Voltar ao menu anterior")
    print("6 - Mostrar esse menu novamente")
    print("----------------------------------------------------")
    print("----------------------------------------------------")

def menu_olympics():
    print("\n----------------------------------------------------")
    print("----------------------------------------------------")
    print("Existem 5 bases de dados que podem ser manipulados: (1) Athletes - ")
    print("(2) Coaches - (3) EntriesGender - (4) Medals - (5) Teams")
    print("Primeiramente digite um desses números para acessar esses dados.")
    print("Após isso você pode escolher o que fazer com base no menu abaixo")
    print("1 - Criar tabela")
    print("2 - Deletar tabela")
    print("3 - Inserir dados na tabela")
    print("4 - Apagar dados dessa tabela")
    print("5 - Encontrar alguma informação")
    print("6 - Voltar a seleção da base de dados")
    print("7 - Voltar ao menu anterior")
    print("----------------------------------------------------")
    print("----------------------------------------------------")

# CONEXAO
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

# MENU INICIAL
def create_database(database, cnx, cursor):
    create_database = (f"CREATE DATABASE {database}")

    cursor.execute(create_database)
    cnx.commit()

def drop_database(database, cnx, cursor):
    drop_database = (f"DROP DATABASE {database}")

    cursor.execute(drop_database)
    cnx.commit()

def show_databases(cnx, cursor):
    cursor.execute("SHOW DATABASES")
    cont = 1
    print("\n----------------------------------------------------")
    for database in cursor:
        print(f"{cont} - {database[0]}")
        cont += 1
    print("----------------------------------------------------\n")

# MENU TABELAS
def create_table(nome, cursor):
    if nome == "athletes":
        create_table = ("CREATE TABLE athletes ( name VARCHAR(100), noc VARCHAR(100), disclipline VARCHAR(100))")

    elif nome == "medals":
        create_table = ("CREATE TABLE medals ( rank INT(10), team VARCHAR(100), gold INT(4), silver INT(4), bronze INT(4), total INT(4), rank_total INT(10))")

    cursor.execute("USE olympics")
    cursor.execute(create_table)

def delete_table(table, where, cnx, cursor):
    delete_medals = f"DELETE FROM {table} WHERE {where}"

    cursor.execute(delete_medals)
    cnx.commit()

def drop_table(table, cnx, cursor):
    drop_table = f"DROP TABLE {table}"
    
    cursor.execute(drop_table)
    cnx.commit()

def insert_medals(cnx, cursor):
    rank_medalhas = pd.read_excel("data\Medals.xlsx")
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
    
def insert_athletes(cnx, cursor):
    athletes = pd.read_excel("data\Athletes.xlsx")
    for name, noc, discipline in athletes:
        insert_athletes = f"""INSERT INTO athletes (name, noc, discipline) VALUES ({name}, {noc}, {discipline})"""

def insert_coaches(cnx, cursor):
    coaches = pd.read_excel("data\Coaches.xlsx")
    for name, noc, discipline in coaches:
        insert_coaches = f"""INSERT INTO coaches (name, noc, discipline) VALUES ({name}, {noc}, {discipline})"""

def command(command, cnx, cursor):
    com = f"{command}"

    cursor.execute(com)
    cnx.commit()

def show_tables(cursor):
    cursor.execute("SHOW TABLES")
    cont = 1
    print("\n---------------------------------------")
    for database in cursor:
        print(f"{cont} - {database[0]}")
        cont += 1
    
    if cont == 1:
        print("Não existe nenhuma tabela nesse banco de dados")
    
    print("---------------------------------------\n")
