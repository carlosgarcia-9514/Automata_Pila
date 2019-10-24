from automata import *
from tkinter import *
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('rate', 100)     # setting up new voice rate
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male


def validar():
	if(entrada.get()==""):
	   engine.say("La entrada esta Vacía")
	   engine.runAndWait()
	   print("Vacía")
	else:

	    automata = Automata(entrada.get(),ventana, lienzo)
	    engine.say("su palabra fue" + entrada.get())
	    engine.runAndWait()
	    if(automata.estado != "rechazado"):
	      automata.validar(esfera, flecha, flecha3, flecha4, borde, esfera2, esfera3, flecha2, apuntador)

def borrar():
    lienzo.delete("all")
    imagen_esfera = lienzo.create_image(150, 100, anchor=NE, image=esfera)
    flecha_esfera = lienzo.create_image(180, 70, anchor=NE, image=flecha)
    flecha_esfera12 = lienzo.create_image(84, 140, anchor=NE, image=flecha3)
    flecha_esfera122 = lienzo.create_image(260, 140, anchor=NE, image=flecha3)
    borde_esfera = lienzo.create_image(513, 87, anchor=NE, image=borde)
    imagen_esfera2 = lienzo.create_image(325, 100, anchor=NE, image=esfera)
    flecha_esfera2 = lienzo.create_image(355, 70, anchor=NE, image=flecha)
    flecha_esfera22 = lienzo.create_image(435, 140, anchor=NE, image=flecha3)
    imagen_esfera3 = lienzo.create_image(500, 100, anchor=NE, image=esfera2)

ventana = Tk()
ventana.title("Automata")
ventana.geometry("700x650")
ventana.config(bg="white")

texto = Label (ventana, text="palabra")
texto.grid(column=2, row=2, columnspan=1)

entrada = Entry(ventana, width=15)
entrada.grid(column=3, row=2)

boton = Button(ventana, text="validar", command=validar)
boton.grid(column=4, row=2)

boton = Button(ventana, text="reiniciar", command=borrar)
boton.grid(column=6, row=2)

lienzo = Canvas(ventana, width=650, height=400, bg="white")
lienzo.grid(column=2, row=30, columnspan=17)

esfera = PhotoImage(file = "assets/esfera12.png")
esfera2 = PhotoImage(file = "assets/esfera22.png")
esfera3 = PhotoImage(file = "assets/esfera32.png")
flecha = PhotoImage(file = "assets/flecha2.png")
flecha2 = PhotoImage(file = "assets/flecha_iluminada2.png")
flecha3 = PhotoImage(file = "assets/imagen_recta1.png")
flecha4 = PhotoImage(file = "assets/flecha_rectailu1.png")
borde = PhotoImage(file = "assets/borde2.png")
apuntador = PhotoImage(file = "assets/apuntador.png")

imagen_esfera = lienzo.create_image(150, 100, anchor=NE, image=esfera)
flecha_esfera = lienzo.create_image(180, 70, anchor=NE, image=flecha)
flecha_esfera12 = lienzo.create_image(84, 140, anchor=NE, image=flecha3)
flecha_esfera122 = lienzo.create_image(260, 140, anchor=NE, image=flecha3)
borde_esfera = lienzo.create_image(513, 87, anchor=NE, image=borde)
imagen_esfera2 = lienzo.create_image(325, 100, anchor=NE, image=esfera)
flecha_esfera2 = lienzo.create_image(355, 70, anchor=NE, image=flecha)
flecha_esfera22 = lienzo.create_image(435, 140, anchor=NE, image=flecha3)
imagen_esfera3 = lienzo.create_image(500, 100, anchor=NE, image=esfera2)
mainloop()
