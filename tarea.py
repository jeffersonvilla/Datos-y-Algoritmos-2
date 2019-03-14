import csv

archivo = 'listacsv.csv'

minimos = {"Proteina":8, "Harina":10, "Granos":3, "Aseo":4, 
			"Aceite y salsa":3, "Vegetales":12}

def cargarDatos(archivo):

	array = []
	aux = []

	with open (archivo) as File:
		reader = csv.reader(File, delimiter = ';')

		#lee cada fila del archivo
		for row in reader:
			aux = []
			esta = False
			#cuando el array no esta vacio
			if len(array) != 0:
				#recorre cada lista del array
				for lista in array:
					item = lista[0]
					#si el elemento que hemos leido
					#pertenece a esta lista
					#Lo insertamos
					if item[0] == row[0]:
						esta = True
						i = 0;
						#iteramos hasta encontrar su posicion
						#en orden de menor a mayor
						for item in lista:						
							if int(item[2]) > int(row[2]):
								break
							i = i + 1
						lista.insert(i, row)		
				#Si el elemento que hemos leido
				#No pertence a ninguna lista
				#Creamos una nueva
				if not esta: 
					aux.append(row)
					array.append(aux)
			#cuando el array esta vacio
			#inserta una lista al array				
			elif row[0] != "Categoria":
				aux.append(row)
				array.append(aux)
				print(array)

	#mostramos la estructura de datos
	#ahora llena y ordenada
	i = 0
	for lista in array:
		print("\narray[{}]".format(i))
		i = i + 1
		for item in lista:
			print(item)

	return array

def voraz(array, minimos, presup):
	lista_compras = {}
	compra_realizada = False
	while(not compra_realizada):
		for lista in array:
			elem = lista[0]
			print(elem[0])
			try:
				valor = float(elem[2])*float(minimos[elem[0]])
				if float(valor) < float(presup):
					presup -= valor
					try:
						lista_compras[elem[1]] += minimos[elem[0]]						
						val = lista_compras[elem[1]]
					except:
						lista_compras[elem[1]] = minimos[elem[0]]
						val = lista_compras[elem[1]]						
				else:
					compra_realizada = True
				print(presup)
			except:
				print("Categoria no encontrada: {}".format(elem[0]))

	return lista_compras

array = cargarDatos(archivo)
compras = voraz(array, minimos, 300000)
print(compras)
		
