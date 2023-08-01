import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

# Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de los 
# televidentes y saber cuál será el participante que deberá abandonar la casa más famosa del mundo.
# Los participantes en la placa son: Giovanni, Gianni y Facundo. 
# Fausto no fue nominado y Marina no está en la placa esta semana por haber ganado la inmunidad.


# Cada televidente que vota deberá ingresar:
# Nombre del votante
# Edad del votante (debe ser mayor a 13)
# Género del votante (Masculino, Femenino, Otro)
# El nombre del participante a quien le dará el voto negativo (Debe estar en placa)
# No se sabe cuántos votos entrarán durante la gala.

# Se debe informar al usuario:
# El promedio de edad de las votantes de género Femenino 
# Cantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo.
# Nombre del votante más joven qué votó a Gianni.
# Nombre de cada participante y porcentaje de los votos qué recibió.
# El nombre del participante que debe dejar la casa (El que tiene más votos)

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")



    def btn_mostrar_on_click(self):
        lista_nombres = ["lala", "julieta", "pepe", "coco", "ñaño", "pato"]
        lista_edades = [25, 23, 27, 29, 30, 15]
        lista_generos = ["femenino", "femenino", "masculino", "masculino", "masculino", "masculino"]
        lista_votos = ["facundo", "giovanni", "facundo", "gianni", "gianni", "facundo"]

        # for _ in range(1):
        #     nombre = prompt("Mostrar", "Nombre")
        #     while nombre == None or not nombre.isalpha():
        #         nombre = prompt("Mostrar", "Nombre")
        #     lista_nombres.append(nombre)

        #     edad = prompt("Mostrar", "Edad")
        #     while edad == None or not edad.isdigit() or int(edad) < 13:
        #         edad = prompt("Mostrar", "Edad")
        #     edad = int(edad)
        #     lista_edades.append(edad)

        #     genero = prompt("Mostrar", "Género")
        #     while genero == None or genero not in ["masculino", "femenino", "otro"]:
        #         genero = prompt("Mostrar", "Género")
        #     lista_generos.append(genero)

        #     voto = prompt("Mostrar", "a quien votas?")
        #     while voto == None or not voto.isalpha() or voto not in ["giovanni", "gianni", "facundo"]:
        #         voto = prompt("Mostrar", "a quien votas?")
        #     lista_votos.append(voto)

        promedio_de_edad = 0
        i = 0
        contador = 0
        contador_mujeres = 0
        votante_mas_joven = 1000    
        for genero in lista_generos:
            if genero == "femenino":
                contador_mujeres +=1
                edad = lista_edades[i]
                promedio_de_edad += edad
            if genero == "masculino":
                edad = lista_edades[i]
                if edad >= 25 and edad <= 40:
                    voto = lista_votos[i]
                    if voto == "giovanni" or voto == "facundo":
                        contador += 1

            i+=1
        promedio_de_edad = promedio_de_edad/contador_mujeres

        if promedio_de_edad > 0:
            print (f"el promedio de edad en votantes mujeres es {promedio_de_edad}")
        else:
            print ("No se han registrado votantes mujeres")

        if contador > 0:
            print (f"la Cantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo: {contador}")
        else:
            print ("No se han registrado votantes de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo")

        i = 0
        contador_gianni = 0
        contador_facu = 0
        contador_gio = 0
        promedio_de_votos_gio = 0
        promedio_de_votos_facu = 0
        promedio_de_votos_gia = 0

        for voto in lista_votos:
            if voto == "gianni":
                edad = lista_edades[i]
                contador_gianni += 1
                if edad < votante_mas_joven:
                    votante_mas_joven = edad
                    nombre_del_votante_mas_joven = lista_nombres[i] 
            if voto == "facundo":
                contador_facu += 1
            elif voto == "giovanni":
                contador_gio += 1    
            i += 1  

        promedio_de_votos_gio = contador_gio/len(lista_votos) * 100
        promedio_de_votos_facu = contador_facu/len(lista_votos) * 100
        promedio_de_votos_gia = contador_gianni/len(lista_votos) * 100
        print (f"el nombre del votante más joven qué votó a Gianni es {nombre_del_votante_mas_joven}")
        print (f"promedio de votos de facu: {promedio_de_votos_facu}% - promedio de votos de gio {promedio_de_votos_gio}% - promedio de votos de gia {promedio_de_votos_gia}%")

        if promedio_de_votos_gio > promedio_de_votos_gia and promedio_de_votos_gio > promedio_de_votos_facu:
            print (f"el nombre del participante que debe dejar la casa es Giovanni con {contador_gio} votos")
        elif promedio_de_votos_facu > promedio_de_votos_gia:
            print (f"el nombre del participante que debe dejar la casa es Facundo con {contador_facu} votos")
        else:
            print (f"el nombre del participante que debe dejar la casa es Gianni con {contador_gianni} votos")

        

            
            


        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()