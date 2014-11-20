from tkinter import *
from random import randint


maailm = """
##################################################
#     #   #      #       ##    #   #             #
##### #   # #### ##### #    ## ### ######## #### #
#       ###    # #   # ######         #   # # #  #
#   #          #   #     # ########## # # # # #  #
### ## ######  ######### # #   #        #   #    #
#    # #               # # # # # ############### #
#### # ######### ##### #     # #         #       #
#    #         #     # ####### # ### ### # #######
###  ####### ######### #           # #   # #     #
#      #               # ######### # # ### #  #  #
###### # ###############   #     # ### # # ##### #                                #
#   #  # #      #     #  # # ### #       # #     #
#   #  # #### # ##### # ## # #   ######### # ### #
#      #    # # #     #  #   #       #       #   #
#  ######## # # # # ###  ########### # ######### #                                 #
#  #        # # # # #                #     #     #
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
#    # #    # #   #    #  # #  #  #   #          #
## ###   ## #   #   # ##########  ### ############
#  # #####  ######### #      #                   #
## #   # #     #      # #  # #########  #####    #
#  # # # ##### # #### #### # #   #   #      #### #
## # #       # # # #  #    # # # # # ###### #    #
#    #########   #    # # ## # #     #    # #    #
# ####   #   ##### #### # #  # # ### #  # #####  #
# #    # ###     #      # # ## # #   #  #   #    #
# ## ### #   ################### #  ### ### #### #
#    #   # #    #   #   #   #    #    # #   #  # #
# ## #     #  #   #   #   #      #  #   # #    # #
################################################ #
"""


akna_laius = 500
akna_kõrgus = 400

#Akna ja tahvli loomine
raam = Tk()
raam.title("Mäng")
tahvel = Canvas(raam, width=akna_laius, height=akna_kõrgus, background="white")
tahvel.grid()


#Maailma suuruse määramine ruutudes
ruudustik_x = int(akna_laius / 10)
ruudustik_y = int(akna_kõrgus / 10)



def maailma_loomine(maailm):
    read = maailm.strip().split("\n")
    for rea_nr in range(len(read)):
        rida = read[rea_nr]
        for veeru_nr in range(len(rida)):
            if rida[veeru_nr] == "#":
                loo_sein(veeru_nr,rea_nr,"black")
            elif rida[veeru_nr] == " ":
                loo_sein(veeru_nr,rea_nr,"gray")



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

def loo_sein(ruudustik_x,ruudustik_y,color):
    if color == "black":
        tahvel.itemconfig(tahvel.create_rectangle(ruudustik_x*10,ruudustik_y*10,ruudustik_x*10+10,ruudustik_y*10+10, fill=color),tag="sein")
    elif color == "yellow":
        tahvel.itemconfig(tahvel.create_rectangle(ruudustik_x*10,ruudustik_y*10,ruudustik_x*10+10,ruudustik_y*10+10, fill=color),tag="põrand")

maailma_loomine(maailm)

#Tegelane ja tema liikumine
tegelane = tahvel.create_rectangle(10, 10, 20, 20,fill="blue")
sammu_pikkus = 10

def leia_id(tegelane,x,y):
    koordinaadid = tahvel.coords(tegelane)
    return tahvel.find_closest(koordinaadid[0]+x,koordinaadid[1]+y)

def nool_üles(event):
    print(leia_id(tegelane,5,-5))
    if not tahvel.gettags(leia_id(tegelane,5,-5)).__contains__("sein"):
        tahvel.move(tegelane, 0, -sammu_pikkus)
        anna_koordinaadid(tegelane)
        print(anna_ruudustiku_koordinaadid(tegelane))

def nool_alla(event):
    print(leia_id(tegelane,5,15))
    if not tahvel.gettags(leia_id(tegelane,5,15)).__contains__("sein"):
        tahvel.move(tegelane, 0, sammu_pikkus)
        anna_koordinaadid(tegelane)
        print(anna_ruudustiku_koordinaadid(tegelane))

def nool_vasakule(event):
    print(leia_id(tegelane,-5,5))
    if not tahvel.gettags(leia_id(tegelane,-5,5)).__contains__("sein"):
        tahvel.move(tegelane, -sammu_pikkus, 0)
        anna_koordinaadid(tegelane)
        print(anna_ruudustiku_koordinaadid(tegelane))

def nool_paremale(event):
    print(leia_id(tegelane,15,5))
    if not tahvel.gettags(leia_id(tegelane,15,5)).__contains__("sein"):
        tahvel.move(tegelane, sammu_pikkus, 0)
        anna_koordinaadid(tegelane)
        print(anna_ruudustiku_koordinaadid(tegelane))

raam.bind_all("<Up>",    nool_üles)
raam.bind_all("<Down>",  nool_alla)
raam.bind_all("<Left>",  nool_vasakule)
raam.bind_all("<Right>", nool_paremale)



#rand_sein(ruudustik_x,ruudustik_y)
#Akna ilmutamine ekraanile
raam.mainloop()
