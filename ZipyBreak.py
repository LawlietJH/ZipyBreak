# -*- coding: utf-8 -*-
# Python 2.7
#
#  ███████╗██╗██████╗ ██╗   ██╗██████╗ ██████╗ ███████╗ █████╗ ██╗  ██╗
#  ╚══███╔╝██║██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██║ ██╔╝
#    ███╔╝ ██║██████╔╝ ╚████╔╝ ██████╔╝██████╔╝█████╗  ███████║█████╔╝ 
#   ███╔╝  ██║██╔═══╝   ╚██╔╝  ██╔══██╗██╔══██╗██╔══╝  ██╔══██║██╔═██╗ 
#  ███████╗██║██║        ██║   ██████╔╝██║  ██║███████╗██║  ██║██║  ██╗
#  ╚══════╝╚═╝╚═╝        ╚═╝   ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
#                                                         By: LawlietJH
#                                                               v1.2.5

from time import time
import zipfile
import locale
import string
import sys
import os


Autor = "LawlietJH"
Version = "v1.2.5"



BZB = u"""
      ███████╗██╗██████╗ ██╗   ██╗██████╗ ██████╗ ███████╗ █████╗ ██╗  ██╗
      ╚══███╔╝██║██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██║ ██╔╝
        ███╔╝ ██║██████╔╝ ╚████╔╝ ██████╔╝██████╔╝█████╗  ███████║█████╔╝ 
       ███╔╝  ██║██╔═══╝   ╚██╔╝  ██╔══██╗██╔══██╗██╔══╝  ██╔══██║██╔═██╗ 
      ███████╗██║██║        ██║   ██████╔╝██║  ██║███████╗██║  ██║██║  ██╗
      ╚══════╝╚═╝╚═╝        ╚═╝   ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
"""
#~ Fuente: 'ANSI Shadow' - Página: http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=ZipyBreak

BA = u"""
                            ╦  ┌─┐┬ ┬┬  ┬┌─┐┌┬┐╦╦ ╦
                            ║  ├─┤││││  │├┤  │ ║╠═╣
                            ╩═╝┴ ┴└┴┘┴─┘┴└─┘ ┴╚╝╩ ╩
"""
#~ Fuente: 'Calvin S' - Página: http://patorjk.com/software/taag/#p=display&f=Calvin%20S&t=LawlietJH



#=======================================================================



def Dat():	# Imprime Los Banners.
		
	Nombre = BZB
	Autor = BA
	Ver = "\n\n{:^80}".format(Version)
	print(Nombre + "\n" + Autor + Ver)



#========================================================================



Modo_De_Uso = """ [+] Modo De Uso:\n\n\n ZipyBreak.py [-A Arch.zip][-C "0-9" | -h ][-L 4] [-D Dic.txt] | [-h|--help]


  -h, --help            Muestra este Mensaje y Sale del Script.
  
  -v, --version         Muestra los Banners y Sale del Script.
  
  -A, --Archivo         Ruta\Nombre del Archivo ZIP A Usar.
  
  -C, --Charset         Caracteres a Utilizar Para El Ataque."""\
 + u"\n\n  -L, --Longitud        Longitud Máxima de Caracteres a Utilizar."\
 + """  

  -D, --Diccionario     Ruta\Nombre del Diccionario A Usar.


    Ejemplos:
    
"""\
+ u"    ZipyBreak.py -C -h     Mostrará las opciones para el Charset.\n\n"\
+ u"    ZipyBreak.py -A Arch.zip -C \"a-z\" -L 4.\n\n"



#========================================================================



Archivo = ""
Charset = ""
Longitud = 1
Diccionario = ""
xD = False
Eny = []


#=======================================================================



def EliminaRepetidas(Keys):
	
	Alf = ""
	
	for y in Keys:	# Eliminamos Letras Repetidas. Asi Evitamos Las Cadenas Repetidas.
		
		if not y in Alf: Alf += y
	
	if len(Alf) > 70:
		print("\n\n [!] Es Una Locura Viejo!!! Hay Más de 1 Cuatrillon De Posibilidades!!!"+
		"\n\n\t Algo así como: 1'000,000'000,000'000,000'000,000"+
		"\t\t\t  Trillon  Billon  Millon  Miles")
		sys.exit(0)
		
	return Alf



def KeyGen(Keys):	#~ Comprueba si hay alguna petición especial de caracteres.
	
	Keys = Keys.replace("a-z", string.ascii_lowercase)	#~ Alfabeto Minúsculas.
	Keys = Keys.replace("A-Z", string.ascii_uppercase)	#~ Alfabeto Mayúsculas.
	Keys = Keys.replace("a-Z", string.ascii_lowercase + string.ascii_uppercase)	#~ Alfabeto Minúsculas + Alfabeto Mayúsculas.
	Keys = Keys.replace("0-9", string.digits)	#~ Dígitos del 0 al 9.
	Keys = Keys.replace("0-z-Z", string.digits + string.ascii_lowercase + string.ascii_uppercase)	#~ Dígitos del 0 al 9 + Alfabeto Minúsculas + Alfabeto Mayúsculas.
	Keys = Keys.replace("0-z", string.digits + string.ascii_lowercase)	#~ Dígitos del 0 al 9 + Alfabeto Minúsculas.
	Keys = Keys.replace("0-Z", string.digits + string.ascii_uppercase)	#~ Dígitos del 0 al 9 + Alfabeto Mayúsculas.
	Keys = Keys.replace("0-f-F", string.hexdigits)	#~ Hexadecimal Minúsculas + Hexadecimal Mayúsculas.
	Keys = Keys.replace("0-f", string.hexdigits[:-6])	#~ Hexadecimal Minúsculas.
	Keys = Keys.replace("0-F", string.hexdigits.upper()[:-6])	#~ Hexadecimal Mayúsculas.
	
	return Keys



def ComandosRapidos():
	
	print u"""


 [+] Ejemplo:   ZipyBreak.py -A Arch.zip -C "0-9" -L 4
                
                Usará Caracteres Númericos desde 1 hasta 4 de Longitud.
	
    ======================================================================
	
    Comando      Descripción
    
    [ a-z ]      Alfabeto en Minúsculas.
    
    [ A-Z ]      Alfabeto en Mayúsculas.
    
    [ a-Z ]      Alfabeto en Minúsculas y Mayúsculas.
    
    [ 0-9 ]      Dígitos del 0 al 9.
    
    [ 0-z-Z ]    Dígitos del 0 al 9 + Alfabeto en Minúsculas y Mayúsculas.
    
    [ 0-z ]      Dígitos del 0 al 9 + Alfabeto en Minúsculas.
    
    [ 0-Z ]      Dígitos del 0 al 9 + Alfabeto en Mayúsculas.
    
    [ 0-f-F ]    Hexadecimal en Minúsculas y Mayúsculas.
    
    [ 0-f ]      Hexadecimal en Minúsculas.
    
    [ 0-F ]      Hexadecimal en Mayúsculas.

   
"""



def Combin(L, C):	# Función Que Crea Las Cadenas Con Caracteres Desde 1 Hasta La Máximo Longitud Elegida.
	
	if L == 1:
		
		for _1 in C: Eny.append(_1)
	
	if L == 2:
		
		for _1 in C:
			Eny.append(_1)
			for _2 in C: _2 = _1 + _2; Eny.append(_2)
		
	elif L == 3:
		
		for _1 in C:
			Eny.append(_1)
			for _2 in C:
				_2 = _1 + _2; Eny.append(_2)
				for _3 in C: _3 = _2 + _3; Eny.append(_3)
			
	elif L == 4:
		
		for _1 in C:
			Eny.append(_1)
			for _2 in C:
				_2 = _1 + _2; Eny.append(_2)
				for _3 in C:
					_3 = _2 + _3; Eny.append(_3)
					for _4 in C: _4 = _3 + _4; Eny.append(_4)
				
	elif L == 5:
		
		for _1 in C:
			Eny.append(_1)
			for _2 in C:
				_2 = _1 + _2; Eny.append(_2)
				for _3 in C:
					_3 = _2 + _3; Eny.append(_3)
					for _4 in C:
						_4 = _3 + _4; Eny.append(_4)
						for _5 in C: _5 = _4 + _5; Eny.append(_5)
				
	elif L == 6:
		
		for _1 in C:
			Eny.append(_1)
			for _2 in C:
				_2 = _1 + _2; Eny.append(_2)
				for _3 in C:
					_3 = _2 + _3; Eny.append(_3)
					for _4 in C:
						_4 = _3 + _4; Eny.append(_4)
						for _5 in C:
							_5 = _4 + _5; Eny.append(_5)
							for _6 in C: _6 = _5 + _6; Eny.append(_6)
				
	elif L == 7:
		
		for _1 in C:
			Eny.append(_1)
			for _2 in C:
				_2 = _1 + _2; Eny.append(_2)
				for _3 in C:
					_3 = _2 + _3; Eny.append(_3)
					for _4 in C:
						_4 = _3 + _4; Eny.append(_4)
						for _5 in C:
							_5 = _4 + _5; Eny.append(_5)
							for _6 in C:
								_6 = _5 + _6; Eny.append(_6)
								for _7 in C: _7 = _6 + _7; Eny.append(_7)



#=======================================================================



def Args():
	
	global Archivo, Diccionario, Charset, Longitud, xD
	
	xD = False
	
	#~ Argumentos que puede leer el Script.
	if len(sys.argv) == 7: #===============================================
		
		# ZipyBreak.py -A Arch.zip -C Caracteres -L Número
		if  (sys.argv[1] == "-A" or sys.argv[1] == "--Archivo")\
		and (sys.argv[3] == "-C" or sys.argv[3] == "--Charset")\
		and (sys.argv[5] == "-L" or sys.argv[5] == "--Longitud"):
			
			if sys.argv[4] == "-h":
				
				ComandosRapidos()
				sys.exit(0)
			
			Archivo  = sys.argv[2]
			Charset  = sys.argv[4]
			Longitud = sys.argv[6]
			
			if int(Longitud) > 7:
				
				print u"\n\n\t [!] Elige Un Número Entre 1-7 Para La Longitud.\n\n"
				print Modo_De_Uso
				sys.exit(0)
			
			return True
		
		# ZipyBreak.py -A Arch.zip -L Número -C Caracteres
		elif (sys.argv[1] == "-A" or sys.argv[1] == "--Archivo")\
		and  (sys.argv[3] == "-L" or sys.argv[3] == "--Longitud")\
		and  (sys.argv[5] == "-C" or sys.argv[5] == "--Charset"):
			
			if sys.argv[6] == "-h":
				
				ComandosRapidos()
				sys.exit(0)
			
			Archivo  = sys.argv[2]
			Longitud = sys.argv[4]
			Charset  = sys.argv[6]
			
			if int(Longitud) > 7:
				
				print u"\n\n\t [!] Elige Un Número Entre 1-7 Para La Longitud.\n\n"
				print Modo_De_Uso
				sys.exit(0)
			
			return True
		
		# ZipyBreak.py -C Caracteres -L Número -A Arch.zip
		elif (sys.argv[1] == "-C" or sys.argv[1] == "--Charset")\
		and  (sys.argv[3] == "-L" or sys.argv[3] == "--Longitud")\
		and  (sys.argv[5] == "-A" or sys.argv[5] == "--Archivo"):
			
			if sys.argv[2] == "-h":
				
				ComandosRapidos()
				sys.exit(0)
			
			Charset  = sys.argv[2]
			Longitud = sys.argv[4]
			Archivo  = sys.argv[6]
			
			if int(Longitud) > 7:
				
				print u"\n\n\t [!] Elige Un Número Entre 1-7 Para La Longitud.\n\n"
				print Modo_De_Uso
				sys.exit(0)
			
			return True
		
		# ZipyBreak.py -C Caracteres -A Arch.zip -L Número
		elif (sys.argv[1] == "-C" or sys.argv[1] == "--Charset")\
		and  (sys.argv[3] == "-A" or sys.argv[3] == "--Archivo")\
		and  (sys.argv[5] == "-L" or sys.argv[5] == "--Longitud"):
			
			if sys.argv[2] == "-h":
				
				ComandosRapidos()
				sys.exit(0)
			
			Charset  = sys.argv[2]
			Archivo  = sys.argv[4]
			Longitud = sys.argv[6]
			
			if int(Longitud) > 7:
				
				print u"\n\n\t [!] Elige Un Número Entre 1-7 Para La Longitud.\n\n"
				print Modo_De_Uso
				sys.exit(0)
			
			return True
		
		# ZipyBreak.py -L Número -A Arch.zip -C Caracteres
		elif (sys.argv[1] == "-L" or sys.argv[1] == "--Longitud")\
		and  (sys.argv[3] == "-A" or sys.argv[3] == "--Archivo")\
		and  (sys.argv[5] == "-C" or sys.argv[5] == "--Charset"):
			
			if sys.argv[6] == "-h":
				
				ComandosRapidos()
				sys.exit(0)
			
			Longitud = sys.argv[2]
			Archivo  = sys.argv[4]
			Charset  = sys.argv[6]
			
			if int(Longitud) > 7:
				
				print u"\n\n\t [!] Elige Un Número Entre 1-7 Para La Longitud.\n\n"
				print Modo_De_Uso
				sys.exit(0)
			
			return True
		
		# ZipyBreak.py -L Número -C Caracteres -A Arch.zip
		elif (sys.argv[1] == "-L" or sys.argv[1] == "--Longitud")\
		and  (sys.argv[3] == "-C" or sys.argv[3] == "--Charset")\
		and  (sys.argv[5] == "-A" or sys.argv[5] == "--Archivo"):
			
			if sys.argv[4] == "-h":
				
				ComandosRapidos()
				sys.exit(0)
			
			Longitud = sys.argv[2]
			Charset  = sys.argv[4]
			Archivo  = sys.argv[6]
			
			if int(Longitud) > 7:
				
				print u"\n\n\t [!] Elige Un Número Entre 1-7 Para La Longitud.\n\n"
				print Modo_De_Uso
				sys.exit(0)
			
			return True
		
		else: return False
		
	elif len(sys.argv) == 5: #=============================================
			
		if  (sys.argv[1] == "-D" or sys.argv[1] == "--Diccionario")\
		and (sys.argv[3] == "-A" or sys.argv[3] == "--Archivo"):
		
			Diccionario = sys.argv[2]
			Archivo = sys.argv[4]
			xD = True
			
			return True
			
		elif (sys.argv[1] == "-C" or sys.argv[1] == "--Charset")\
		and  (sys.argv[3] == "-A" or sys.argv[3] == "--Archivo"):
			
			if sys.argv[2] == "-h":
				
				ComandosRapidos()
				sys.exit(0)
			
			return False
		
		elif (sys.argv[1] == "-A" or sys.argv[1] == "--Archivo")\
		and  (sys.argv[3] == "-D" or sys.argv[3] == "--Diccionario"):
			
			Archivo = sys.argv[2]
			Diccionario = sys.argv[4]
			xD = True
			
			return True
		
		elif (sys.argv[1] == "-A" or sys.argv[1] == "--Archivo")\
		and  (sys.argv[3] == "-C" or sys.argv[3] == "--Charset"):
			
			if sys.argv[4] == "-h":
				
				ComandosRapidos()
				sys.exit(0)
			
			return False
		
		else: return False
		
	elif len(sys.argv) == 3: #=============================================
			
		if sys.argv[1] == "-C" or sys.argv[1] == "--Charset":
		
			if sys.argv[2] == "-h":
				
				ComandosRapidos()
				sys.exit(0)
				
	elif len(sys.argv) == 2: #=============================================
		
		if sys.argv[1] == "-v" or sys.argv[1] == "--version":
			
			os.system("Cls")
			print "\n\n\n"
			Dat()
			print "\n\n"
			sys.exit(0)
			
		elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
			
			print "\n\n"
			print Modo_De_Uso
			sys.exit(0)
				
	else: return False



#=======================================================================



def Tiempo(sec):	# Convierte El Tiempo.
	
	secs = int(sec)
	mins = secs/60
	hors = mins/60
	dias = hors/24
	
	if sec >= 86400:  # Convierte a Dias
		return "{:d} Dia(s) {:d} hora(s) {:d} minuto(s) {:d} segundo(s)".format(dias, hors%24, mins%60, secs%60)
	elif sec >= 3600:  # Convierte a Horas
		return "{:d} hora(s) {:d} minuto(s) {:d} segundo(s)".format(hors, mins%24, secs%60)
	elif sec >= 60:  # Convierte a Minutos
		return "{:d} minuto(s) {:d} segundo(s)".format(mins, secs%60)
	else:            # Sin Conversión
		return "{:d} segundo(s)".format(secs)



#=======================================================================



def main():
	
	global Eny
	
	Eny = []
	A = Archivo
	C = Charset
	D = Diccionario
	L = int(Longitud)
	
	try:
		
		ZIP = zipfile.ZipFile(A)
	
	except IOError:
		
		if not Archivo.lower().endswith(".zip"): print "\n\n\t [!] El Archivo " + Archivo + u" No tiene extensión .zip.\n\n"
		else: print "\n\n\t [!] Por favor, compruebe el nombre o ruta del archivo.\n\n"
		print Modo_De_Uso
		sys.exit(0)
		
	except KeyboardInterrupt:
		
		print "\n\n\t [!] Cancelado!"
		sys.exit(0)
	
	print "\n\n\n"
	
	Pwd = None
	Cont = 0 
	TiempoI = time()
	TiempoF = 1
	Tiempo_Total = None
	
	try:
		
		if xD:
			
			with open(D, "r") as Arch:
				
				Cadenas = Arch.readlines()
				
				for Palabra in Cadenas:
					
					Cont += 1
					Pwd = Palabra.split("\n")[0]
					
					try:
						TiempoF = time() - TiempoI
						Tiempo_Total = Tiempo(TiempoF)
						ZIP.extractall(pwd=Pwd)
						
						sys.stdout.writelines("\r  [+] Probando: " + Pwd + "\t\t[~] " + str(int(Cont/TiempoF)) + " Palabras/s. ")
						
						print u"\n\n\n\t [+] Password Descifrado: {}".format(Pwd) 
						print u"\n\n\t [+] Tomó {} para descifrar el Password.".format(Tiempo_Total)
						print u"\n\n\t [+] Con {} Palabras Probadas.\n\n\n".format(Cont) 
						sys.exit(0)
						
					except Exception:
						
						if Cont % 250 == 0:
							
							if len(Pwd) < 8:
								sys.stdout.writelines("\r  [+] Probando: " + Pwd + "\t\t[~] " + str(int(Cont/TiempoF)) + " Palabras/s. ")
							elif len(Pwd) >= 8 or len(Pwd) < 16:
								sys.stdout.writelines("\r  [+] Probando: " + Pwd + "\t[~] " + str(int(Cont/TiempoF)) + " Palabras/s. ")
					
					except KeyboardInterrupt:
						
						print "\n\n\t [!] Cancelado!"
						sys.exit(0)
						
				print "\n\n\t [!] Password No Encontrada." 
		
		else:
			
			C = KeyGen(C)
			C = EliminaRepetidas(C)
			Combin(L, C)
			
			for Palabra in Eny:

				#~ print(Palabra)
				
				Cont += 1
				Pwd = Palabra
				
				try:
					TiempoF = time() - TiempoI
					Tiempo_Total = Tiempo(TiempoF)
					ZIP.extractall(pwd=Pwd)
					
					sys.stdout.writelines("\r  [+] Probando: " + Pwd + "\t\t[~] " + str(int(Cont/TiempoF)) + " Palabras/s. ")
						
					print u"\n\n\n\t [+] Password Descifrado: {}".format(Pwd) 
					print u"\n\n\t [+] Tomó {} para descifrar el Password.".format(Tiempo_Total)
					print u"\n\n\t [+] Con {} Palabras Probadas.\n\n\n".format(Cont) 
					sys.exit(0)
					
				except Exception:
					
					if Cont % 300 == 0:
						
						if len(Pwd) < 8:
							sys.stdout.writelines("\r  [+] Probando: " + Pwd + "\t\t[~] " + str(int(Cont/TiempoF)) + " Palabras/s. ")
						elif len(Pwd) >= 8 or len(Pwd) < 16:
							sys.stdout.writelines("\r  [+] Probando: " + Pwd + "\t[~] " + str(int(Cont/TiempoF)) + " Palabras/s. ")
				
				except KeyboardInterrupt:
					
					print "\n\n\t [!] Cancelado!"
					sys.exit(0)
					
			print "\n\n\t [!] Password No Encontrada." 
			
	except KeyboardInterrupt:
		
		print "\n\n\t [!] Cancelado!"
		quit()



#=======================================================================



if __name__ == '__main__':
	
	os.system("Cls")
	
	print("\n\n\n")
	Dat()
	
	#~ locale.setlocale(locale.LC_ALL, 'esp')

	if Args(): main()
	else:
		print "\n\n\t [!] Faltan Argumentos."
		print "\n\n" + Modo_De_Uso


