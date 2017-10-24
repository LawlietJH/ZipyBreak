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
#																v1.1.1

from time import time
import zipfile
import locale
import sys
import os


Autor = "LawlietJH"
Version = "v1.1.1"



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



Modo_De_Uso = """ [+] Modo De Uso: ZipyBreak.py [-A Arch.zip][-D Dic.txt] | [-h|--help]



  -h, --help            Muestra este Mensaje y Sale del Script.

  -v, --version         Muestra los Banners y Sale del Script.
 
  -A, --Archivo         Ruta\Nombre del Archivo ZIP A Usar.

  -D, --Diccionario     Ruta\Nombre del Diccionario A Usar.


"""

Archivo = ""
Diccionario = ""



#=======================================================================



def Args():
	
	global Archivo, Diccionario
	
	#~ Argumentos que puede leer el Script.
	if len(sys.argv) == 5:
			
		if  (sys.argv[1] == "-D" or sys.argv[1] == "--Diccionario")\
		and (sys.argv[3] == "-A" or sys.argv[3] == "--Archivo"):
			
			Diccionario = sys.argv[2]
			Archivo = sys.argv[4]
			
			return True
		
		elif (sys.argv[1] == "-A" or sys.argv[1] == "--Archivo")\
		and  (sys.argv[3] == "-D" or sys.argv[3] == "--Diccionario"):
			
			Archivo = sys.argv[2]
			Diccionario = sys.argv[4]
			
			return True
		
		else: return False
	elif len(sys.argv) == 2:
		
		if sys.argv[1] == "-v" or sys.argv[1] == "--version":
			
			os.system("Cls")
			print "\n\n\n"
			Dat()
			print "\n\n"
			sys.exit(0)
			
		if sys.argv[1] == "-h" or sys.argv[1] == "--help":
			
			print "\n\n"
			print Modo_De_Uso
			sys.exit(0)
				
	else: return False



#=======================================================================



def Tiempo(sec):	# Convierte El Tiempo.
	
	sec = int(sec)
	
	if sec >= 31449600:  # Convierte a Años
		return "{:d} año(s)".format(int(sec / 31449600))
	elif sec >= 604800:  # Convierte a Semanas
		return "{:d} Semana(s)".format(int(sec / 604800))
	elif sec >= 86400:  # Convierte a Dias
		return "{:d} Dia(s)".format(int(sec / 86400))
	elif sec >= 3600:  # Convierte a Horas
		return "{:d} hora(s)".format(int(sec / 3600))
	elif sec >= 60:  # Convierte a Minutos
		return "{:d} minuto(s)".format(int(sec / 60))
	else:            # Sin Conversión
		return "{:d} segundo(s)".format(int(sec))



#=======================================================================



def main():
	
	A = Archivo
	D = Diccionario
	
	try:
		
		ZIP = zipfile.ZipFile(A)
	
	except IOError:
		
		if not Archivo.lower().endswith(".zip"): print "\n\n\t [!] El Archivo " + Archivo + u" No tiene extensión .zip.\n\n"
		else: print "\n\n\t [!] Por favor, compruebe el nombre o ruta del archivo.\n\n"
		print Modo_De_Uso
		quit()
		
	except KeyboardInterrupt:
		
		print "\n\n\t [!] Cancelado!"
		quit()
	
	print "\n\n\n"
	
	Pwd = None
	Cont = 0 
	TiempoI = time()
	TiempoF = 1
	Tiempo_Total = None
	
	try:
		
		with open(D, "r") as Arch:
			
			Cadenas = Arch.readlines()
			
			for Palabra in Cadenas:
				
				Cont += 1
				Pwd = Palabra.split("\n")[0]
				
				try:
					TiempoF = time() - TiempoI
					Tiempo_Total = Tiempo(TiempoF)
					ZIP.extractall(pwd=Pwd)

					print u"\n\n\n\t [+] Password Descifrado: {}".format(Pwd) 
					print u"\n\n\t [+] Tomó {} para descifrar el Password.".format(Tiempo_Total)
					print u"\n\n\t [+] Con {} Palabras Probadas.\n\n\n".format(Cont) 
					quit()
					
				except Exception:
					
					if Cont % 250 == 0:
						
						if len(Pwd) < 8:
							sys.stdout.writelines("\r  [+] Probando: " + Pwd + "\t\t[~] " + str(int(Cont/TiempoF)) + " Palabras/s. ")
						elif len(Pwd) >= 8 or len(Pwd) < 16:
							sys.stdout.writelines("\r  [+] Probando: " + Pwd + "\t[~] " + str(int(Cont/TiempoF)) + " Palabras/s. ")
				
				except KeyboardInterrupt:
					
					print "\n\n\t [!] Cancelado!"
					quit()
					
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


