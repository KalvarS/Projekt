from tkinter import *
from tkinter import font
from time import *


kaart = """
##################################################
#     Z  $#      #       ##    #   #$            #
# T   Z   # #### ##### #    ## ### ######## #### #
#  E    ###    # #   # ######         #   # # #  #
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
################################################E#
"""
kaart2 = """
##################################################
#   # #  $#      #$      ##    #                T#
# #   #   # #### #######    ## ### ######## ######
#####   ###    # #   # ######         #   # #$   #
#              #   #     # ########## # #F# ###  #
### ## ################# # #   #        #        #
#    # #               # # # # # ######### #######
#### # ##### ### ##### #     # #         #      $#
#    #         #    $# ####### # ### ### # #######
###  ####### ######### #     #     # #   #       #
#      #               # ######### # # ### #  #  #
###### # ###############   #     # ### # # ##### #
#   #  # #      #     #  # # ### #         #     #
#   #  # #### # ##### # ## # #   ######### # ### #
#  $#  #    # # #     #  #   #       #     # #$  #
#  ## ##### # # # # ###  ########### # ######### #
#  #        # # # # #                #     #     #
#  #######  ### ### ### ############## ##### #####
#                 #  #  #     #   #        # #   #
### ### ############ # ## ### # ###  #####     # #
#   #         #   #  #    #   #      #     ##### #
# ########### # # # ## #### ### #### #######     #
# #   #     # #           #     #$   #       #####
#   #   #         ## #### ############ ##### #   #
########## ########  #    # #  #         # # #   #
#$$  #              ####### #  #  ######## #     #
#### # ###############         #  #   # ## ##### #
#$   # #    # #   #    #  # #     #   #          #
## ### # ## #   #   # ##### ##### ### ############
#  # #####  ######### #      #                   #
## #   # #     #      #$#  # ##### ###  #####    #
#  # # # ##### # #### ###### #   #   #      #### #
## # #         # # #  #    # # # # # ###### #    #
#    #########   #    # # ## # #     #    # #    #
# ####   #   ##### #### # #  # ##### #  # #####  #
# #    # ###     #      # # ## # #   #  #   #    #
# ## ### #   ################### #  ### ### #### #
#    #   # #    #   #   #   #    #    # #   # $# #
#F##$#     #  #   # # #   #      #  #   # #    # #
##################################################
"""


raam = Tk()
raam.title("Mäng")

tahvel = Canvas(raam, width=500, height=400, background="white")
tahvel.pack()

tahvel2 = Canvas(raam, width=500, height= 100, background="lightgray")
tahvel2.pack()


def click(event):
    print("X:",event.x)
    print("Y:",event.y)


class Maailm:
    maailm = [] #Tühi maailm
    def __init__(self,laius,pikkus,kaart,tahvel):
        self.kaart = kaart
        self.laius = laius
        self.pikkus = pikkus
        self.tahvel = tahvel


#Loob tühja maailma(kahemõõtmelise listi) antud mõõtmetega.
    def looMaailmMõõtmetega(self):
        for y in range(self.pikkus):
            self.maailm.append([])
            for x in range(self.laius):
                self.maailm[y].append(" ")

    def loeKaartSisse(self):
        read = self.kaart.strip().split("\n")
        for rea_nr in range(len(read)):
            rida = read[rea_nr]
            for veeru_nr in range(len(rida)):
                if rida[veeru_nr] == "T":
                    Õhk(veeru_nr,rea_nr).looAknasse()
                    Tegelane.tegelase_ID = Tegelane(veeru_nr,rea_nr,10,"Juks").looAknasse()
                elif rida[veeru_nr] == " ":
                    Õhk(veeru_nr,rea_nr).looAknasse()
                    Udu(veeru_nr,rea_nr).looAknasse()
                elif rida[veeru_nr] == "#":
                    Sein(veeru_nr,rea_nr).looAknasse()
                    Udu(veeru_nr,rea_nr).looAknasse()
                elif rida[veeru_nr] == "Z":
                    ElektriAed(veeru_nr,rea_nr).looAknasse()
                    Udu(veeru_nr,rea_nr).looAknasse()
                elif rida[veeru_nr] == "E":
                    Väljapääs(veeru_nr,rea_nr).looAknasse()
#                    Udu(veeru_nr,rea_nr).looAknasse()
                elif rida[veeru_nr] == "$":
                    Õhk(veeru_nr,rea_nr).looAknasse()
                    Münt(veeru_nr,rea_nr).looAknasse()
                    Udu(veeru_nr,rea_nr).looAknasse()
                elif rida[veeru_nr] == "F":
                    Finish(veeru_nr,rea_nr).looAknasse()

                #elif rida[veeru_nr] == "T":
                #    teg = maailm.muudaObjekti(1,1,Tegelane(1,1,10,"Juks"))
                #    teg.looAknasse()

    def muudaObjekti(self,veeru_nr,rea_nr,objekt):
        self.maailm[veeru_nr][rea_nr] == objekt
        return objekt

    def leiaObjekt(self,x,y):
        #print(self.maailm)
        return self.maailm[x][y]



class Objekt(Maailm):
    objektideLoendur = 0
    def __init__(self,x,y):
        self.x = x * 10 + 5  #Teisendab listi koordinaadid tahvli omadesse
        self.y = y * 10 + 5
        Objekt.objektideLoendur += 1
        self.objektiID = Objekt.objektideLoendur
        Maailm.maailm[x][y] = self

    def tagastaSümbol(self):
        return self.märk

    def koordinaadid(self):
        return [self.x,self.y]

    def id(self):
        return self.objektiID

    def kuvaKogus(self):
        print("Objekte kokku" , Objekt.objektideLoendur)

    def eemalda(self):
        self.maailm[self.x][self.y] = " "

    def looAknasse(self):
        return tahvel.create_image(self.x,self.y,image=self.pilt,tag=self.tag, anchor="center")

class Õhk(Objekt):
    nimi = "õhk"
    tag = "läbitav"
    märk = " "
    pilt = PhotoImage(file="õhk.gif")

class Sein(Objekt):
    nimi = "sein"
    tag = "takistus"
    märk = "#"
    pilt = PhotoImage(file="sein.gif")

class ElektriAed(Objekt):
    nimi = "elektri aed"
    tag = ("takistus", "surmav")
    märk = "Z"
    pilt = PhotoImage(file="elekter.gif")

class Väljapääs(Objekt):
    nimi = "väljapääs"
    tag = "lõpp"
    märk = "E"
    pilt = PhotoImage(file="lõpp.gif")

class Münt(Objekt):
    nimi = "münt"
    tag = ("läbitav", "korjatav")
    märk = "$"
    pilt = PhotoImage(file="mynt.gif")

class Udu(Objekt):
    nimi = "udu"
    tag = ("läbitav", "hajuv")
    märk = "%"
    pilt = PhotoImage(file="udu.gif")

class Finish(Objekt):
    nimi = "finish"
    tag = "finish"
    märk = "F"
    pilt = PhotoImage(file="finish.gif")

class Olend(Objekt):
    olendid = 0
    def __init__(self,x,y,elud,nimi):
        Objekt.__init__(self,x,y)
        self.olendid += 1
        self.elud = elud
        self.nimi = nimi
        self.olendiID = Objekt.objektideLoendur
        Objekt.objektideLoendur += 1

    #Leiab objektide ID-d mingite kindlate koordinaatide järgi.
    def leiaID(self,x,y): #Enne oli ilma x ja y-ita
        return tahvel.find_overlapping(x,y,x,y)
        #return tahvel.find_closest(x,y)

    def olendeidKokku(self):
        return Olend.olendid

    def id(self):
        return self.olendiID


    def kaotaUdu(self,x,y,suund):
        uusX = x
        uusY = y
        if suund == "E":
            uusX = x+10
        elif suund == "W":
            uusX = x-10
        elif suund == "N":
            uusY = y-10
        elif suund == "S":
            uusY = y+10

        for element in self.leiaID(x,y):
            if tahvel.find_withtag("takistus").__contains__(element):
                if tahvel.find_withtag("hajuv").__contains__(self.leiaID(x,y)[-1]):
                    tahvel.delete(self.leiaID(x,y)[-1])
                return
            if tahvel.find_withtag("hajuv").__contains__(element):
                tahvel.delete(self.leiaID(x,y)[-1])
            self.kaotaUdu(uusX,uusY,suund)

    def tuvastaTakistus(self,x,y,suund):
        print("Ees on objekt(id) ID-ga: ", self.leiaID(x,y))
        if tahvel.find_withtag("hajuv").__contains__(self.leiaID(x,y)[-1]):
            self.kaotaUdu(x,y,suund)
            #tahvel.delete(self.leiaID(x,y)[-1])
        if tahvel.find_withtag("takistus").__contains__(self.leiaID(x,y)[-1]):
            if tahvel.find_withtag("surmav").__contains__(self.leiaID(x,y)[-1]):
                print("Said elektrit, kaotasid",2, "elupunkti")
                self.elud -= 2
                if self.elud <= 0:
                    self.sure()
                    print(self.nimi, "sai surma")
                else:
                    print("Elusid alles", self.elud)
            return True
        elif tahvel.find_withtag("lõpp").__contains__(self.leiaID(x,y)[-1]):
            print("Läbisid leveli!")
            maailm = Maailm(500,500,kaart2,tahvel)
            maailm.looMaailmMõõtmetega()
            maailm.loeKaartSisse()
            return True
        elif tahvel.find_withtag("korjatav").__contains__(self.leiaID(x,y)[-1]):
            print("Leidsid mündi!")
            i = self.leiaID(x,y)
            for element in i:
                if tahvel.find_withtag("korjatav").__contains__(element):
                    tahvel.delete(element)
        elif tahvel.find_withtag("finish").__contains__(self.leiaID(x,y)[-1]):
            self.sure()
            lõpp()

        else:
            return False

    def liiguVasakule(self,event):
        if self.elus:
            if not self.tuvastaTakistus(self.x-10,self.y,"W"):
                tahvel.move(Tegelane.tegelase_ID,-10,0) #Tegelase ID 2001
                tahvel.lift(Tegelane.tegelase_ID)
                self.x -= 10
    def liiguParemale(self,event):
        if self.elus:
            if not self.tuvastaTakistus(self.x+10,self.y,"E"):
                tahvel.move(Tegelane.tegelase_ID,10,0)
                tahvel.lift(Tegelane.tegelase_ID)
                self.x += 10
    def liiguÜlesse(self,event):
        if self.elus:
            objekt = self.tuvastaTakistus(self.x,self.y-10,"N") #Kontrollib kas objekt on takistus
            if not objekt:
                tahvel.move(Tegelane.tegelase_ID,0,-10)
                tahvel.lift(Tegelane.tegelase_ID)
                self.y -= 10
                #self.valiObjekt()
                #self.eemaldaValitudObjektid()

    def liiguAlla(self,event):
        if self.elus:
            if not self.tuvastaTakistus(self.x,self.y+10,"S"):
                tahvel.move(Tegelane.tegelase_ID,0,10)
                tahvel.lift(Tegelane.tegelase_ID)
                self.y += 10

class Tegelane(Olend):
    elus = True
    tag = ("läbitav", "olend")
    nimi = "Juks"
    märk = "T"
    pilt = PhotoImage(file="Tegelane.gif")
    tegelase_ID = None

    def __init__(self,x,y,elud,nimi):
        Olend.__init__(self,x,y,elud,nimi)
        raam.bind_all("<Up>",    self.liiguÜlesse)
        raam.bind_all("<Down>",  self.liiguAlla)
        raam.bind_all("<Left>",  self.liiguVasakule)
        raam.bind_all("<Right>", self.liiguParemale)
        raam.bind_all("<a>", self.räägi)


    def sure(self):
        self.elus = False

    def id(self):
        print(self.tegelase_ID)

    def määraNimi(self,nimi):
        self.nimi = nimi

    def tagastaNimi(self):
        return self.nimi

    def tapaTegelane(self):
        Tegelane.elus = False

    def räägi(self, event):
        if self.elus:
            print(self.nimi+":", input("Sisesta tekst:"))
        else:
            print(self.nimi+"i vaim:", input("Sisesta tekst:"))

def lõpp():
    raam = Tk()
    raam.title("Tahvel")
    tahvel = Canvas(raam, width=500, height=500, background="white")
    tahvel.grid()

    suur_font = font.Font(family='Verdana', size=32, weight='bold')
    tahvel.create_text(200, 100, text="GAME OVER", font=suur_font, anchor=NW)

    skoori_font = font.Font(family="Verdana", size=18, weight="bold")
    tahvel.create_text(200, 200, text="Skoor:", font=skoori_font, anchor=NW)

    raam.mainloop()

maailm = Maailm(500,500,kaart,tahvel)
maailm.looMaailmMõõtmetega()
maailm.loeKaartSisse()


print("LEia objekt",maailm.leiaObjekt(1,1))



#teg = maailm.muudaObjekti(1,1,Tegelane(1,1,10,"Juks"))
#teg.looAknasse()
#teg = maailm.leiaObjekt(1,1)
#teg = Tegelane(1,1,10,"Juks")




tahvel.bind("<ButtonPress-1>", click)

raam.mainloop()
