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
#																v1.0.7

from time import time
import optparse
import zipfile
import sys
import os
import locale


Autor = "LawlietJH"
Version = "v1.0.7"



parser = optparse.OptionParser()
parser.add_option('-A', '--Archivo', 	 action="store", dest="Archivo", 	 help="Ruta\Nombre del Archivo ZIP",	default=None)
parser.add_option('-D', '--Diccionario', action="store", dest="Diccionario", help="Ruta\Nombre del Diccionario",	default=None)
options, args = parser.parse_args()



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
                            ╩═╝┴ ┴└┴┘┴─┘┴└─┘ ┴╚╝╩ ╩"""
#~ Fuente: 'Calvin S' - Página: http://patorjk.com/software/taag/#p=display&f=Calvin%20S&t=LawlietJH



#=======================================================================



def Dat():	# Imprime Los Banners.
		
	Nombre = BZB
	Autor = BA
	Ver = "\n\n{:^80}".format(Version)
	print(Nombre + "\n" + Autor + Ver)



def Modo_de_Uso():
	
	print """
	
Modo de Uso: ZipyBreak.py [-A Nomb.zip][-D Diccionario.txt] | [-h|--help]

  -h, --help            Muestra este Mensaje y Sale del Script.
  
  -A, --Archivo         Ruta\Nombre del Archivo ZIP
                        
  -D, --Diccionario     Ruta\Nombre del Diccionario

	"""




#=======================================================================



def Tiempo(sec):	# Imprime El Tiempo Restante.
	
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



def main(A, D):
	
	try: ZIP = zipfile.ZipFile(A)
		
	except zipfile.BadZipfile:
		
		print "Por favor, compruebe la ruta del archivo. No parece ser un archivo ZIP."
		quit()
		
	except KeyboardInterrupt:
		
		print "\n\n\t [!] Cancelado!"
		quit()
	
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

					print "\n\n\n\t [+] Password Descifrado: {}".format(Pwd) 
					print u"\n\n\t [+] Tomó {} para descifrar el Password.\n\n".format(Tiempo_Total) 
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



if __name__ == '__main__':
	
	os.system("Cls")
	
	print("\n\n\n")
	Dat()
	print("\n\n\n")
	
	locale.setlocale(locale.LC_ALL, 'esp')
	if options.Archivo == None and options.Diccionario == None:
		
		Modo_de_Uso()
		
	main(options.Archivo, options.Diccionario)


