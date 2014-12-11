from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#from tkinter import font


def level1():
    maailm = """
##################################################
#     #  $#      #       ##    #   #$            #
#     #   # #### ##### #    ## ### ######## #### #
#       ###    # #   # ######         #   # # #  #
#              #   #     # ########## # # # # #  #
### ## ######  ######### # #   #       $#   #    #
#    # #               # # # # # ############### #
#### # ######### ##### #     # #         #       #
#    #        $#     # ####### # ### ### # #######
###  ####### ######### #           # #   # #     #
#$     #               # ######### # # ### #  #  #
###### # ###############  $#     # ### # # ##### #
#   #  # #      #     #  # # ### #       # #     #
#   #  # #### # ##### # ## # #   ######### # ### #
#      #    # # #     #  #   #       #       #$  #
#  ######## # # # # ###  ########### # ######### #
#  #$$$     # # # # #$               #     #     #
#  #######  ### ### ### ############## ##### #####
#                 #  #  #     #   #        # #   #
####### ############ # ## ### # ###  ##### #   # #
#             #   #  #    #   #      #     ##### #
############# # # # ## #### ### #### #######     #
# #   #     # #           #     #    #       #####
#   #   #         ## #### ############ ##### #   #
## ################  #    # #  #         # # #   #
#                   ##### # #  #  ######## #     #
#### # ###############         #  #   # ## ##### #
#$   # #    # #   #    #  # #  #  #   #          #
## ###   ## #   #   # ##########  ### ############
#  # #####  ######### #      #                   #
## #   # #     #      #$#  # #########  #####    #
#  # # # ##### # #### #### # #   #   #      #### #
## # #       # # # #  #    # # # # # ###### #    #
#    #########   #    # # ## # #     #    # #    #
# ####   #   ##### #### # #  # # ### #  # #####  #
# #    # ###     #      # # ## # #   #  #   #    #
# ## ### #   ################### #  ### ### #### #
#    #   # #    #   #   #   #    #    # #   # $# #
# ##$#     #  #   #   #   #      #  #   # #    # #
################################################!#
    """
    maailma_loomine(maailm)
    kuva_seis(punktid,raha,aeg)
    tegelase_pilt = PhotoImage(file="tegelane.gif")
    global tegelane
    tegelane = tahvel.create_image(15,15,image=tegelase_pilt,tag="tegelane")
    # Sellega töötab, aga pilt talle ei meeldi.
    #tegelane = tahvel.create_rectangle(10, 10, 19, 19,fill="blue",outline="blue")


punktid = 0
raha = 0
aeg = 0
akna_laius = 500
akna_kõrgus = 400

#Akna ja tahvli loomine
raam = Tk()
raam.title("Mäng")
tahvel = Canvas(raam, width=akna_laius, height=akna_kõrgus, background="white")
tahvel.grid()

tahvel2 = Canvas(raam, width=akna_laius, height=akna_kõrgus-300, background="lightgray")
tahvel2.grid()


#Maailma suuruse määramine ruutudes
ruudustik_x = int(akna_laius / 10)
ruudustik_y = int(akna_kõrgus / 10)



def maailma_loomine(maailm):
    read = maailm.strip().split("\n")
    for rea_nr in range(len(read)):
        rida = read[rea_nr]
        for veeru_nr in range(len(rida)):
            if rida[veeru_nr] == "#":
                loo_objekt(veeru_nr,rea_nr,"black")
            elif rida[veeru_nr] == " ":
                loo_objekt(veeru_nr,rea_nr,"white")
            elif rida[veeru_nr] == "@":
                loo_objekt(veeru_nr,rea_nr,"yellow")
            elif rida[veeru_nr] == "!":
                loo_objekt(veeru_nr,rea_nr,"brown")
            elif rida[veeru_nr] == "$":
                loo_objekt(veeru_nr,rea_nr,"pilt")



def anna_koordinaadid(item):
    return tahvel.coords(item)

def anna_ruudustiku_koordinaadid(item):
    list = anna_koordinaadid(item)
    koordinaadid = []
    for koordinaat in list:
        koordinaadid.append(koordinaat/10)
    return koordinaadid







#def rand_sein(x,y):
#    rida = x
#    tulp = y
#    väljapääs = False
#    while y > 0:
#        x = rida
#        while x > 0:
#            if randint(0,100) < 58 and (x % 2 == 0 or y % 2 == 0) :
#                loo_sein(x*10,y*10,"black")
#            if rida == x or tulp == y or x == 1 or y == 1:
#                if väljapääs == False and randint(0,100) == 1:
#                    väljapääs = True
#                else:
#                    loo_sein(x*10,y*10,"red")
#            x -= 1
#        y -= 1

münt = PhotoImage(file="mynt.gif")

def loo_objekt(ruudustik_x,ruudustik_y,color):
    if color == "black":
        tahvel.create_rectangle(ruudustik_x*10,ruudustik_y*10,ruudustik_x*10+10,ruudustik_y*10+10,outline="black", fill=color,tags="sein")
    elif color == "white":
        tahvel.create_rectangle(ruudustik_x*10,ruudustik_y*10,ruudustik_x*10+10,ruudustik_y*10+10,outline="white", fill=color,tag="põrand")
    elif color == "yellow":
        tahvel.create_rectangle(ruudustik_x*10,ruudustik_y*10,ruudustik_x*10+10,ruudustik_y*10+10,outline="black", fill=color,tag="elekter")
    elif color == "brown":
        tahvel.create_rectangle(ruudustik_x*10,ruudustik_y*10,ruudustik_x*10+10,ruudustik_y*10+10,outline="brown", fill=color,tag="lõpp")
    elif color == "pilt":
        pilt = tahvel.create_image(ruudustik_x*10+5,ruudustik_y*10+5,image=münt,tag="münt")
        print("pilt",tahvel.coords(pilt))
        print(pilt)


def kuva_seis(punktid,raha,aeg):
    tahvel2.create_rectangle(2,2,500,100,fill="beige")
    silt1 = tahvel2.create_text(10,10,text="Punktid:" + str(punktid), anchor="w")
    silt2 = tahvel2.create_text(10,30,text="Raha:"+ str(raha),anchor="w")
    silt3 = tahvel2.create_text(10,50,text="Aeg(sek):"+ str(aeg),anchor="w")


#kuva_seis(punktid,raha,aeg)



#Tegelane ja tema liikumine
#tegelase_pilt = PhotoImage(file="tegelane.gif")
#tegelane = tahvel.create_image(15,15,image=tegelase_pilt,tag="tegelane")
#tegelane = tahvel.create_rectangle(10, 10, 19, 19,fill="blue",outline="blue")
sammu_pikkus = 10

def leia_id(tegelane,x,y):
    koordinaadid = tahvel.coords(tegelane)
    return tahvel.find_overlapping(koordinaadid[0]+x,koordinaadid[1]+y,koordinaadid[0]+x,koordinaadid[1]+y)



def nool_üles(event):
    if not tahvel.gettags(leia_id(tegelane,0,-10)).__contains__("sein"):
        tahvel.move(tegelane, 0, -sammu_pikkus)
        print(anna_koordinaadid(tegelane))
        print(leia_id(tegelane,0,0))
    if tahvel.find_withtag("münt").__contains__(leia_id(tegelane,0,0)[0]):
        global raha
        global punktid
        punktid += 100
        raha += 5
        tahvel.delete(leia_id(tegelane,0,0)[0])
        kuva_seis(punktid,raha,aeg)

def nool_alla(event):
    if not tahvel.gettags(leia_id(tegelane,0,10)).__contains__("sein"):
        tahvel.move(tegelane, 0, sammu_pikkus)
        print(anna_koordinaadid(tegelane))
        print(leia_id(tegelane,0,0))
    if tahvel.find_withtag("münt").__contains__(leia_id(tegelane,0,0)[0]):
        global raha
        global punktid
        punktid += 100
        raha += 5
        tahvel.delete(leia_id(tegelane,0,0)[0])
        kuva_seis(punktid,raha,aeg)

def nool_vasakule(event):
    if not tahvel.gettags(leia_id(tegelane,-10,0)).__contains__("sein"):
        tahvel.move(tegelane, -sammu_pikkus, 0)
        print(anna_koordinaadid(tegelane))
        print(leia_id(tegelane,0,0))
    if tahvel.find_withtag("münt").__contains__(leia_id(tegelane,0,0)[0]):
        global raha
        global punktid
        punktid += 100
        raha += 5
        tahvel.delete(leia_id(tegelane,0,0)[0])
        kuva_seis(punktid,raha,aeg)

def nool_paremale(event):
    if not tahvel.gettags(leia_id(tegelane,10,0)).__contains__("sein"):
        tahvel.move(tegelane, sammu_pikkus, 0)
        print(anna_koordinaadid(tegelane))
        print(leia_id(tegelane,0,0))
    if tahvel.find_withtag("münt").__contains__(leia_id(tegelane,0,0)[0]):
        global raha
        global punktid
        punktid += 100
        raha += 5
        tahvel.delete(leia_id(tegelane,0,0)[0])
        kuva_seis(punktid,raha,aeg)

raam.bind_all("<Up>",    nool_üles)
raam.bind_all("<Down>",  nool_alla)
raam.bind_all("<Left>",  nool_vasakule)
raam.bind_all("<Right>", nool_paremale)


#rand_sein(ruudustik_x,ruudustik_y)
#Akna ilmutamine ekraanile







#uus_font = font.Font(family='Helvetica', size=32, weight='bold')



raam = Tk()
raam.title("Mäng")
raam.geometry("500x400")


silt = ttk.Label(raam, text="Mängu nimi")
silt.place(x=200, y=10)


nupp = ttk.Button(raam, text="New game", command=level1)
nupp.place(x=160, y=40, width=150)

nupp2 = ttk.Button(raam, text="High score")
nupp2.place(x= 160, y = 70,width= 150)


raam.mainloop()
