		# CREO REPOSITORIO Y PEGO UN ARCHIVO
		
1- creé el repositorio desde github
2- git clone FinalProject-Individual
3- touch prueba.py
4- git add prueba.py
5- git commit -m "Archivo de prueba"
6- git push
7- Añadí de colaboradora a 'paobtorres'

		# CREO RAMAS (para el merge)
		
8- git checkout -b rama_uno
9- touch archivo.txt
10- vim archivo.txt 		#cambio la primer línea
11- git add archivo.txt
12- git commit -m "Archivo rama_uno"

13- git checkout main
14- git chekout -b rama_dos
15- vim archivo.txt 		#acá modifico la primer línea
16- git add archivo.txt
17- git commit -m "Cambio misma línea"

18- git checkout main
19- git merge rama_uno
20- git merge rama_dos
