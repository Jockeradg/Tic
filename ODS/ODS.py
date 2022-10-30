#Comienzo del programa
#Importacion de librerias
from tkinter import *
from tkinter.ttk import *


#Crear pantalla y ajustes
window = Tk()
window.title("ODS")
window.geometry('500x300')
window.wm_iconbitmap('OIP.ico')
lista = Combobox()

#Texto, cada letras un ODS, letras + i, el texto del ods
a = "Fin de la Pobreza"
b = "Hambre Cero"
c = "Salud y Bienestar"
d = "Educación de Calidad"
e = "Igualdad de Género"
f = "Agua Limpia y Saneamiento"
g = "Energía Asequible y No Contaminante"
h = "Trabajo Decente y Crecimiento Económico"
i = "Industria, Innovación e Infrasestructura"
j = "Reducción de las Desigualdades"
k = "Ciudades y Comunidades Sostenibles"
l = "Producción y Consumo Responsables"
m = "Acción por el clima"
n = "Vida Submarina"
ñ = "Vida de Ecosistemas Terrestres"
o = "Paz. Justicia e Instituciones Sólidas"
p = "Alianzas para Lograr los Objetivos"

#Array con todos los titulos
ods = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p]

def Titulos(ods):
    for z in range(0, len(ods)):
        if z == len(ods):
            print(ods[z])
        else:
            print(str(z) + ". " + ods[z] , end = ", ")

window.mainloop()

