import random

class Personaje():

	def __init__ (self):
		self._vida = 0
		self._armadura = 0

class Eleven(Personaje):

	#def __init__(self, nombre, vida, armadura, rol):
	def __init__(self):	
		super(Eleven, self).__init__()
		self._vida = 0
		self._armadura = 0
		self._nombre = ""
		self._rol = ""

	def get_playerName(self):
		return self._nombre	

	def set_playerName(self, nombre):
		self._nombre = nombre

	def get_playerVida(self):
		return self._vida

	def set_playerVida(self, vida):
		self._vida=vida 	

	def get_playerArmadura(self):
		return self._armadura

	def set_playerArmadura(self, x):
		self._armadura = x		

	def get_playerRol(self):
		return self._rol	

	def set_playerRol(self, x):
		self._rol= x

	def info(self):
		informacion = "nombre:",self._nombre,"vida:",self._vida,"armadura:",self._armadura,"Rol:",self._rol
		return print(informacion)

	def ataque(self):
		ataque = random.randint(10,20)
		return ataque


class Urbus(Personaje):

	def __init__(self):
		super(Urbus, self).__init__()
		self._vida = 0
		self._armadura = 0
		self._nombre = ""
		self._rol = ""

	def get_playerName(self):
		return self._nombre	

	def set_playerName(self, nombre):
		self._nombre = nombre

	def get_playerVida(self):
		return self._vida

	def set_playerVida(self, vida):
		self._vida=vida 	

	def get_playerArmadura(self):
		return self._armadura

	def set_playerArmadura(self, armadura):
		self._armadura = armadura

	def get_playerRol(self):
		return self._rol	

	def set_playerRol(self, rol):
		self._rol= rol

	def info(self):
		informacion = "nombre:",self._nombre,"vida:",self._vida,"armadura:",self._armadura,"Rol:",self._rol
		return print(informacion)

	#retorna daño_total
	def ataque(self):
		import random
		frases = ["Golpe crítico", "Brutal", "Criticazo", "Buen golpe"]
		ataque = random.randint(13,20)
		frase_random = random.choice(frases)
		if ataque > 16:
			daño_total = print("Daño:",str(ataque),"¡"+frase_random+"!")
			return daño_total
		else:
			daño_total = print("Daño:",str(ataque))
			return daño_total	

class Enemigo(Personaje):

	def __init__ (self):
		super(Enemigo, self).__init__()
		self._vida = 100
		self._armadura = 0
		self._habilidad = "CUERPO A CUERPO"

	def get_enemyVida(self):
		return self._vida

	def set_enemyVida(self, vida):
		self._vida=vida 	

	def get_enemyArmadura(self):
		return self._armadura

	def set_enemyArmadura(self, armadura):
		self._armadura = armadura	

	def info (self):
		return print("Enemigo\nVida: "+str(self._vida)+"\nArmadura: "+str(self._armadura)+"\nHabilidad: "+ str(self._habilidad))	

	def ataque(self):
		ataque = random.randint(10,16)
		return ataque




