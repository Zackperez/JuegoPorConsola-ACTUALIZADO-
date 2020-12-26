import personajes
import os
import time
import random


guerreros = ['Eleven','Hall','Urbus','Catris','Kale']
armas = ['Espada','Hacha']

eleven = personajes.Eleven()
urbus = personajes.Urbus()
enemigo = personajes.Enemigo()

def eleccion_personaje_verificacion():
	opc = True
	while opc == True:
		try:
			for j in range(1):
				for element in guerreros:
					print(j+1," ",element)
					j =j+1	
				return int(input("Elige un guerrero\n---->"))
			opc = False
		except ValueError:
			os.system('cls')
			print("Escribe el numero del personaje a elegir")	

def eleccion_personaje():
	loop = True
	while loop == True:

		opc = eleccion_personaje_verificacion()
		#Sale un personaje elegido

		if opc == 1:
			jugador = "Eleven"
			return jugador
			break

		elif opc == 2: 	# HALL
			jugador = "Hall"
			return jugador
			break
		
		elif opc == 3:	# URBUS
			jugador = "Urbus"
			return jugador
			break
		
		elif opc == 4:	# CATRIS
			jugador = "Catris"
			return jugador
			break
		
		elif opc == 5:	# KALE
			jugador = "Kale"
			return jugador
			break

		else: 				# CONDICION	
			os.system('cls')
			print("Personaje no encontrado cole")		

def eleccion_armas_verificacion():
	opc = True 
	while opc == True:
		try:
			for x in range(1):
				for element in armas:
					print(x+1,"",element)
					x = x+1	
			return	int(input("Elige tu arma\n"))	
			opc= False
		except ValueError: #SI DIGITA ALFABETO, ERROR
			print("Elige el numero de arma que quieres")

def eleccion_arma(): 
	loop= True
	#empezar = True

	while loop == True: #ELECCION DE ARMA

		opc = eleccion_armas_verificacion()

		if opc == 1: #Espada
			arma= "Espada"
			loop = False
			return arma

		elif opc == 2: #Hacha
			arma= "Hacha"
			loop = False
			return arma

		else:
			print("\nDigita una de las opciones de armas listadas\n")

def eleccion_mostrar(jugador, arma):

	print("Jugador = "+jugador)
	print("Arma = "+arma)			

def empezar_juego_verificacion():	
	empezar = True
	oportunidad = True
	while empezar == True:	
		try:
			aux = int(input("¿Listo para empezar?\n1.Si \n2.No\n"))
			if aux == 1:
				return aux #En caso de ser "SI" devolverá 1
				empezar = False	
			elif aux > 2:
				os.system('cls')
				print("Digita una de las opciones (ERROR PRIMERA OPCION) ")	
			else:			#Sí no es 1
				print("Bueno, te daré unos segundos...")
				time.sleep(3.0)

				while oportunidad == True:
					try:
						opc = int(input("¿Quieres salir del juego?\n1.Si \n2.No\n"))
						if opc == 1:
							print("Bueno, bai")
							empezar = False
							oportunidad = False
						if opc == 2:
							oportunidad = False	
						elif opc > 2:
							os.system('cls')
							print("Tienes que escribir el numero de la opcion ")	
					except ValueError:
						os.system('cls')
						print("Digita una de las opciones (SEGUNDA OPCION)")

		except ValueError:
			os.system('cls')
			print("Digita una de las opciones (PRIMERA OPCION)")

def asignar_atributos(jugador):
	pass			

def empezar_juego(jugador):

	opc = empezar_juego_verificacion()	
	if opc == 1:
		i = 4;
		f = -1;
		for x in range(i,f,-1):
			if x < 1:
				print("Empieza la batalla")
				empezar_batalla(jugador)
			else:
				print("El juego empezará en",x)
				time.sleep(1.0)

def empezar_batalla(jugador):

	if jugador == "Eleven":

		vida_jugador = eleven.get_playerVida()
		ataque_jugador = eleven.ataque()
		vida_enemigo = enemigo.get_enemyVida()
		ataque_enemigo = enemigo.ataque()
		daño_total = 0

		while vida_jugador > 1 or vida_enemigo > 1:
			print(f"""
				-------------------------------------------------
				| VIDA DEL JUGADOR = {vida_jugador}			|
				| VIDA DEL ENEMIGO = {vida_enemigo}			|
				-------------------------------------------------
				""")
			print(ataque_jugador)
			if ataque_jugador >= 18:
				frases = ["Golpe crítico", "Brutal", "Criticazo", "Buen golpe"]
				frase_random = random.choice(frases)
				daño_total = print("Daño:",str(ataque_jugador),"¡"+frase_random+"!")
			else:
				daño_total = print("Daño:",str(ataque_jugador))

			vida_enemigo =  vida_enemigo - ataque_jugador	

			if vida_enemigo < 1:
				print(f"""
					Vida del jugador: {vida_jugador}
					Vida del enemigo: {vida_enemigo}
					¡Haz ganado el combate!
				 """)
				break
			elif vida_jugador > 1:
				print ("ok")	
			time.sleep(1.0)

			print(ataque_enemigo)
			if ataque_enemigo >= 14:
				daño_total = print("Daño:",str(ataque_enemigo)+" critico del enemigo")
			else:
				daño_total = print("Daño:",str(ataque_enemigo))

			vida_jugador =  vida_jugador - ataque_enemigo	

			if vida_jugador <= 1:
				print(f"""
					Vida del jugador: {vida_jugador}
					Vida del enemigo: {vida_enemigo}
					¡Haz perdido el combate!
				 """)
				break
			elif vida_enemigo > 1:
				print("ok, pero enemigo")	
	

					
	elif jugador == "Urbus":
		urbus.info()

if __name__ == '__main__':

	print("-------Juego medieval xd-------\n")
	#time.sleep(3.0)

	#Seleccion de jugador
	print("A continuación, elige el numero del personaje con el que quieres jugar\n")
	jugador = eleccion_personaje()
	print("\n"+jugador+" elegido"+"\n")

	#Seleccion de arma
	print("Ármate con una de estas poderosas\n")
	arma = eleccion_arma()
	print ("\n"+arma+" elegida")

	#Mostrar información final

	if jugador == "Eleven":
		eleven.set_playerName(jugador)
		eleven.set_playerVida(100)
		eleven.set_playerArmadura(0)
		eleven.set_playerRol("Guerrero")
		eleven.info()
		empezar_juego(jugador)

	if jugador == "Urbus":
		urbus.set_playerName(jugador)
		urbus.set_playerVida(100)
		urbus.set_playerArmadura(0)
		urbus.set_playerRol("Guerrero")
		urbus.info()
		empezar_juego(jugador)	
