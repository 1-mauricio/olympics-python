import pandas as pd
import mysql.connector
import functions
from mysql.connector import errorcode

aux = 0
end_all = False
menu_inicio = True
menu_tabela = True

functions.inicio()
while not end_all:
	while menu_inicio:
		try:
			if aux == 0:
				functions.menu_inicial()
				aux += 1

			menu_inicial = input(": ")

			if menu_inicial == "1":
				database = input("Digite o nome do banco de dados para tentar a conexão: ")
				cnx = functions.conexao_database(database)
				cursor = cnx.cursor()

				print("Conexão feita com sucesso")

				menu_next = input("Você gostaria de acessar esse banco de dados?(S/N): ")
				if menu_next == "S":
					menu_inicio = False

			elif menu_inicial == "2":
				cnx_i = functions.conexao_inicial()

				cursor_i = cnx_i.cursor()
				nome = input("Digite o nome do banco de dados: ")
				functions.create_database(nome, cnx_i, cursor_i)
				print("Banco de dados criado com sucesso.\n")

			elif menu_inicial == "3":
				drop_database = input("Digite o noem do banco de dados que deseja exluir: ")

				cnx_i = functions.conexao_inicial()
				cursor_i = cnx_i.cursor()

				functions.drop_database(drop_database, cnx_i, cursor_i)

				print(f"Banco de dados {drop_database} excluido com sucesso")
				
			elif menu_inicial == "4":
				comando = input("Digite o comando que deseja: ")

				cnx_i = functions.conexao_inicial()
				cursor_i = cnx_i.cursor()

				functions.command(comando, cnx_i, cursor_i)

			elif menu_inicial == "5":
				cnx_i = functions.conexao_inicial()
				cursor_i = cnx_i.cursor()

				functions.show_databases(cnx_i, cursor_i)
			
			elif menu_inicial == "6":
				aux = 0
			
		except mysql.connector.errors.DatabaseError:
			print("Não existe nenhum banco de dados com esse nome. Você pode criar um ou tentar outro nome.")

	
