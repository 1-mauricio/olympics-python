import pandas as pd
import mysql.connector
import functions
from mysql.connector import errorcode

aux_menu_inicio = 0
aux_menu_database = 0
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
				if aux_menu_inicio == 0:
					functions.menu_inicial()
					aux_menu_inicio = 1

				menu_inicial = input("Digite uma opção: ")

				if menu_inicial == "1":
					database = input("Digite o nome do banco de dados para tentar a conexão: ")
					cnx = functions.conexao_database(database)
					cursor = cnx.cursor()

					print("Conexão feita com sucesso")
					aux_all = 1
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
					aux_menu_inicio = 0
				
				else:
					print("A entrada digitada não condiz com uma opção. Tente novamente.\n")

			except mysql.connector.Error as err:
  				print(f"Algo deu errado: {err}")

			except mysql.connector.errors.DatabaseError:
				print("Não existe nenhum banco de dados com esse nome. Você pode criar um ou tentar outro nome.")

	elif aux_all == 1:
		while menu_database:
			if aux_menu_database == 0:
				functions.menu_database(database)
				aux_menu_database = 1
			menu_data = int(input(": "))

			if menu_data == 1:
				functions.show_tables(cursor)

			elif menu_data == 3:
				table = input("Digite o nome da tabela: ")
				functions.drop_table(table, cnx, cursor)
			
			elif menu_data == 4:
				aux_all = 2
				menu_database = False
				menu_olympics = True
			
			elif menu_data == 5:
				aux_all = 0
				aux_menu_inicio = 0
				menu_database = False
				menu_inicio = True

			elif menu_data == 6:
				aux_menu_database = 0

			else:
				print("A entrada digitada não condiz com uma opção. Tente novamente.\n")
				
	elif aux_all == 2:
		while menu_olympics:
			functions.menu_olympics()
			menu_oly = int(input(": "))
			if menu_oly == 1:
				print("TABELA: athletes")
				athletes = True
				while athletes:
					menu_medals = int(input("Digite alguma opção para a tabela athletes: "))
					if menu_medals == 1:
						functions.create_table("athletes", cursor)
					elif menu_medals == 2:
						functions.drop_table("athletes", cnx, cursor)
					elif menu_medals == 3:
						functions.insert_medals(cnx, cursor)
					elif menu_medals == 4:
						functions.delete_table("athletes", 'gold < 1000', cnx, cursor)
					elif menu_medals == 5:
						pass
					elif menu_medals == 6:
						athletes = False
					elif menu_medals == 7:
						athletes = False
						aux_all = 1
						menu_olympics = False
						menu_database = True
				

			elif menu_oly == 2:
				pass

			elif menu_oly == 3:
				pass

			elif menu_oly == 4:
				print("TABELA: Medals")
				medals = True
				while medals:
					menu_medals = int(input("Digite alguma opção para a tabela Medals: "))
					if menu_medals == 1:
						functions.create_table("medals", cursor)
					elif menu_medals == 2:
						functions.drop_table("medals", cnx, cursor)
					elif menu_medals == 3:
						functions.insert_medals(cnx, cursor)
					elif menu_medals == 4:
						functions.delete_table("medals", 'gold < 1000', cnx, cursor)
					elif menu_medals == 5:
						pass
					elif menu_medals == 6:
						medals = False
					elif menu_medals == 7:
						medals = False
						aux_all = 1
						menu_olympics = False
						menu_database = True
			
			elif menu_oly == 5:
				aux_all = 1
				menu_olympics = False
				menu_database = True