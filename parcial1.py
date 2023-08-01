'''
Al presionar el botón  'Mostrar', se deberán mostrar los números 
almacenados en el vector lista_datos utilizando Dialog Alert para informar cada elemento.
list.append(x): Agrega un elemento x al final de la lista.
list.remove(x): Elimina la primera aparición del elemento x de la lista.
list.pop([i]): Elimina y devuelve el elemento en la posición i de la lista. Si no se especifica i, se eliminará y devolverá el último elemento.
list.clear(): Elimina todos los elementos de la lista, dejándola vacía.
list.index(x[, start[, end]]): Devuelve el índice de la primera aparición del elemento x. Puedes proporcionar un rango opcional start y end para buscar
list.index(x[, start[, end]]): Devuelve el índice de la primera aparición del elemento x. Puedes proporcionar un rango opcional start y end para buscar dentro de una subsección de la lista.
list.count(x): Devuelve el número de apariciones del elemento x en la lista.
list.reverse(): Invierte el orden de los elementos en la lista.
len(list): Devuelve la longitud (número de elementos) de la lista.  

def btn_agregar_on_click(self):
    flag_nombre_articulo = true
    nombre_articulo = self.txt_nombre_articulo.get()

    flag_precio_articulo_texto = true
    precio_articulo_texto = self.txt_precio_articulo.get()

    coontador_de_puntos = 0

    for letra in nombre_articulo:
        if not letra.isalpha() and letra != ""
        flag_nombre_articulo = false
        alert("Error", "Nombre incorrecto")
        break

    if precio_articulo_texto:
            for letra in precio_articulo_texto:
                if not letra.isdecimal() and letra != ".":
                    flag_precio_articulo_texto = False
                    break
                elif letra == ".":
                    contador_de_puntos += 1
                    if contador_de_puntos > 1:
                        peso_es_valido = False
                        break
                else:
                    flag_precio_articulo_texto = True



    if flag_nombre_articulo == true:
            txt = "es valido"
        
        alert("Carga", txt)














def btn_mostrar_on_click(self):
Para agregar cosas a las listas ejemplo 

    self.lista_nombre_articulos = ["tv", "computadora"]
    self.lista_precios = [1000, 2000]


    cantidad_elementos = len(self.lista_nombre_articulos)
        for indice in range(cantidad_elementos):
            mensaje = "indice: {0} - {1} - {2}".format(indice, self.lista_nombre_articulo[indice],self.lista_precios[indice])

            print (mensaje)


def btn_informar_on_click(self):
'''
