import pandas as pd
import mysql.connector
import functions
from mysql.connector import errorcode

aux = 0
aux_all = 0
end_all = False
menu_inicio = True
menu_database = True
menu_olympics = True

functions.inicio()
while not end_all:
	if aux_all == 0:
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
					aux_all += 1
					menu_inicio = False
					menu_database = True

				elif menu_inicial == "2":
					cnx_i = functions.conexao_inicial()

					cursor_i = cnx_i.cursor()
					nome = input("Digite o nome do banco de dados: ")
					functions.create_database(nome, cnx_i, cursor_i)
					print("Banco de dados criado com sucesso.\n")

				elif menu_inicial == "3":
					drop_database = input("Digite o nome do banco de dados que deseja exluir: ")

					cnx_i = functions.conexao_inicial()
					cursor_i = cnx_i.cursor()

					functions.drop_database(drop_database, cnx_i, cursor_i)

					print(f"Banco de dados {drop_database} excluido com sucesso\n")
					
				elif menu_inicial == "4":
					comando = input("Digite o comando que deseja: ")

					cnx_i = functions.conexao_inicial()
					cursor_i = cnx_i.cursor()

					functions.command(comando, cnx_i, cursor_i)
					print("Comando executado com sucesso.\n")

				elif menu_inicial == "5":
					cnx_i = functions.conexao_inicial()
					cursor_i = cnx_i.cursor()

					functions.show_databases(cnx_i, cursor_i)
				
				elif menu_inicial == "6":
					aux = 0
				
			except mysql.connector.errors.DatabaseError:
				print("Não existe nenhum banco de dados com esse nome. Você pode criar um ou tentar outro nome.")

	elif aux_all == 1:
		while menu_database:
			functions.menu_tabela()
			menu_data = int(input(": "))

			if menu_data == 1:
				functions.show_tables(cursor)
			
			elif menu_data == 2:
				aux_all += 1
				menu_database = False
				menu_olympics = True
			
			elif menu_data == 3:
				aux_all -= 1
				aux = 0
				menu_database = False
				menu_inicio = True
				
	elif aux_all == 2:
		while menu_olympics:
			menu_oly = int(input(": "))
			if menu_oly == 1:
				functions.create_medals(cnx, cursor)

			if menu_oly == 2:
				functions.delete_table("medals", 'gold < 1000', cnx, cursor)

			if menu_oly == 3:
				functions.insert_medals(cnx, cursor)

			if menu_oly == 4:
				functions.drop_table("medals", cnx, cursor)
			
			elif menu_oly == 5:
				aux_all -= 1
				menu_olympics = False
				menu_database = True