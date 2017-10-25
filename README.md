# ZipyBreak
## Obten Contraseñas De Archivos Comrpimidos ZIP con Fuerza Bruta con Python.
- - -

* __Python 2.7__
* __By: LawlietJH__
* __v1.2.5__

- - -

### Modo De Uso:

 __[+] Modo De Uso:__

 __ZipyBreak.py [-A Arch.zip][-C "0-9" | -h ][-L 4] [-D Dic.txt] | [-h|--help]__


  __-h, --help            Muestra este Mensaje y Sale del Script.__

  __-v, --version         Muestra los Banners y Sale del Script.__

  __-A, --Archivo         Ruta\Nombre del Archivo ZIP A Usar.__

  __-C, --Charset         Caracteres a Utilizar Para El Ataque.__

  __-L, --Longitud        Longitud Máxima de Caracteres a Utilizar.__

  __-D, --Diccionario     Ruta\Nombre del Diccionario A Usar.__


   __Ejemplos:__

   __ZipyBreak.py -C -h     Mostrará las opciones para el Charset.__

   __ZipyBreak.py -A Arch.zip -C "a-z" -L 4.__

---

### Modo De Uso Charset:

 __[+] Ejemplo:   ZipyBreak.py -A Arch.zip -C "0-9" -L 4__

   __Usará Caracteres Númericos desde 1 hasta 4 de Longitud.__

   __======================================================================__

   __Comando      Descripción__

   __[ a-z ]      Alfabeto en Minúsculas.__

   __[ A-Z ]      Alfabeto en Mayúsculas.__

   __[ a-Z ]      Alfabeto en Minúsculas y Mayúsculas.__

   __[ 0-9 ]      Dígitos del 0 al 9.__

   __[ 0-z-Z ]    Dígitos del 0 al 9 + Alfabeto en Minúsculas y Mayúsculas.__

   __[ 0-z ]      Dígitos del 0 al 9 + Alfabeto en Minúsculas.__

   __[ 0-Z ]      Dígitos del 0 al 9 + Alfabeto en Mayúsculas.__

   __[ 0-f-F ]    Hexadecimal en Minúsculas y Mayúsculas.__

   __[ 0-f ]      Hexadecimal en Minúsculas.__

   __[ 0-F ]      Hexadecimal en Mayúsculas.__
   
   
