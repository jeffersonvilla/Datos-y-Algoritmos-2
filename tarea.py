import csv

archivo = 'listacsv.csv'

minimos = {"Proteina":8, "Harina":10, "Granos":3, "Aseo":4, 
			"Aceite y salsa":3, "Vegetales":12}

orden = {"Proteina": 16, "Vegetales":8, "Harina":4, "Aceite y salsa":2,
	 "Granos":1, "Aseo":0, "Varios": 0, "Delicatese":0}


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

def voraz(array, mini, presup):
	lista_compras = {}
	compra_realizada = False
	i = 0
	#mientras aun tengamos presupuesto
	while(not compra_realizada):
		#recorremos la lista de productos 
		for lista in array:			
			#Evitamos que se salga del rango
			if int(len(lista)) > int(i):
				elem = lista[i]
				print("\n")
				print(elem)
				print(mini)
				try:
					if mini[elem[0]] <= 0:
						continue
				except:
					print("Categoria no encontrada: {}".format(elem[0]))
			#realizamos compra
			try:
				valor = float(elem[2])
				if float(valor) < float(presup):
					presup -= valor
					try:
						lista_compras[elem[1]] += 1
						mini[elem[0]] -= 1						
					except:
						lista_compras[elem[1]] = 1										
						mini[elem[0]] -= 1
				else:
					compra_realizada = True
			except:
				print("Categoria no encontrada: {}".format(elem[0]))
		i+=1

	print("\nRestan.. {}$".format(presup))
	return lista_compras

def voraz2(array, minim, presup):
	mini = minim
	lista_compras = {}
	compra_realizada = False
	i = 0
	#mientras aun tengamos presupuesto
	while(not compra_realizada):
		#recorremos la lista de productos 
		for lista in array:			
			#Evitamos que se salga del rango
			if int(len(lista)) > int(i):
				elem = lista[i]
				#print("\n")
				#print(elem)
				#print(mini)
				try:
					if mini[elem[0]] <= 0:
						continue
				except:
					print("Categoria no encontrada: {}".format(elem[0]))
			#realizamos compra
			if mini[elem[0]] > 0:
				try:
					valor = float(elem[2])
					if float(valor) < float(presup):
						presup -= valor
						try:
							lista_compras[elem[1]] += 1
							mini[elem[0]] -= 1						
						except:
							lista_compras[elem[1]] = 1										
							mini[elem[0]] -= 1
					else:
						compra_realizada = True
				except:
					print("Categoria no encontrada: {}".format(elem[0]))
			#Aceptamos o rehacemos la lista de compras
			suma = 0
			for item in mini:
				suma += mini[item]
			if suma == 0 and presup > 20000:
				mini = minim
				for item in mini:
					if mini[item] == 0:
						mini[item] = 0
					else:
						mini[item] *= 2	
			elif suma == 0:
				compra_realizada = True
		i+=1

	print("\nRestan.. {}$".format(presup))
	return lista_compras

array = cargarDatos(archivo)
compras = voraz(array, minimos, 300000)
#print("\n")
for item in compras:
	print("{} : {}".format(item, compras[item]))

compras = voraz2(array, orden, 200000)
#print("\n")
for item in compras:
	print("{} : {}".format(item, compras[item]))


