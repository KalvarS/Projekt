from tkinter import *

mapi_laius = 800
mapi_kõrgus = 800
sammu_pikkus = 10

def nool_üles(event):
    tahvel.move(tegelane, 0, -sammu_pikkus)

def nool_alla(event):
    tahvel.move(tegelane, 0, sammu_pikkus)

def nool_vasakule(event):
    tahvel.move(tegelane, -sammu_pikkus, 0)

def nool_paremale(event):
    tahvel.move(tegelane, sammu_pikkus, 0)


raam = Tk()
raam.title("Map")
tahvel = Canvas(raam, width=mapi_laius, height=mapi_kõrgus, background="white")
tahvel.grid()

tegelane = tahvel.create_rectangle(390, 390, 400, 400)


raam.bind_all("<Up>",    nool_üles)
raam.bind_all("<Down>",  nool_alla)
raam.bind_all("<Left>",  nool_vasakule)
raam.bind_all("<Right>", nool_paremale)

raam.mainloop()


