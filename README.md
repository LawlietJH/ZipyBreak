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


  __-h, --help            _Muestra este Mensaje y Sale del Script.___

  __-v, --version         _Muestra los Banners y Sale del Script.___

  __-A, --Archivo         _Ruta\Nombre del Archivo ZIP A Usar.___

  __-C, --Charset         _Caracteres a Utilizar Para El Ataque.___

  __-L, --Longitud        _Longitud Máxima de Caracteres a Utilizar.___

  __-D, --Diccionario     _Ruta\Nombre del Diccionario A Usar.___


   __Ejemplos:__

   __ZipyBreak.py -C -h     _Mostrará las opciones para el Charset.___

   __ZipyBreak.py -A Arch.zip -C "a-z" -L 4__
   
   __ZipyBreak.py -A Arch.zip -D Diccionario.txt__

---

### Modo De Uso Charset:

 __[+] Ejemplo:   ZipyBreak.py -A Arch.zip -C "0-9" -L 4__

   ___Usará Caracteres Númericos desde 1 hasta 4 de Longitud.___

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
   
   
