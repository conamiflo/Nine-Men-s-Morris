from email.errors import MisplacedEnvelopeHeaderDefect
import random
from re import M
import time
import copy
import math

class HashMap(object):

    def __init__(self,kapacitet=24):
        self._podaci = kapacitet * ["*"]
        self._kapacitet = kapacitet
        self._velicina = 0

    def hesiraj(self,kljuc):
        
        hesirano = int(kljuc) ^ 7 + 3
        hesirano2 = hesirano % self._kapacitet
        return hesirano2

    def dodajuhes(self,kljuc,vrednost):

        hesirankljuc = self.hesiraj(kljuc)
        kljucvr = [kljuc,vrednost]

        if self._podaci[hesirankljuc] == "*":
            self._podaci[hesirankljuc] = list([kljucvr])
        else:
            for kljucv in self._podaci[hesirankljuc]:
                if kljucv[0] == kljuc:
                    kljuc[1] = vrednost

            self._podaci[hesirankljuc].append(kljucvr)
    
    def pronadjihes(self,kljuc):

        hesiranikljuc = self.hesiraj(int(kljuc))
        if self._podaci[hesiranikljuc] != "*":
            for i in self._podaci[hesiranikljuc]:
                if i[0] == kljuc:
                    return i[1]
            
    def setujvr(self,kljuc,vr):
        hesiranikljuc = self.hesiraj(kljuc)
        for i in self._podaci[hesiranikljuc]:
            if i[0] == kljuc:
                i[1] = vr       

hesmapa = HashMap()


class Polja():

    def __init__(self,vr):
        self.gore = ""
        self.desno = ""
        self.dole = ""
        self.levo = ""
        self.skokovi = ""
        self.vr = vr


p0 = Polja("*")
p1 = Polja("*")
p2 = Polja("*")
p3 = Polja("*")
p4 = Polja("*")
p5 = Polja("*")
p6 = Polja("*")
p7 = Polja("*")
p8 = Polja("*")
p9 = Polja("*")
p10 = Polja("*")
p11 = Polja("*")
p12 = Polja("*")
p13 = Polja("*")
p14 = Polja("*")
p15 = Polja("*")
p16 = Polja("*")
p17 = Polja("*")
p18 = Polja("*")
p19 = Polja("*")
p20 = Polja("*")
p21 = Polja("*")
p22 = Polja("*")
p23 = Polja("*")

p0.desno = p1;p0.dole = p9;p1.desno = p2;p1.dole = p4 ;p1.levo = p0;p2.dole = p14;p2.levo = p1;p3.desno = p4;p3.dole = p10;p4.desno = p5;p4.dole = p7;p4.levo = p3;p4.gore = p1;p5.dole = p13;p5.levo = p4
p6.desno = p7;p6.dole = p11;p7.desno = p8;p7.levo = p6;p7.gore = p4;p8.dole = p12;p8.levo = p7;p9.desno = p10;p9.dole = p21;p9.gore = p0;p10.desno = p11;p10.dole = p18;p10.levo = p9;p10.gore = p3;p11.dole = p15;p11.levo = p10;p11.gore = p6
p12.desno = p13;p12.dole = p17;p12.gore = p8;p13.desno = p14;p13.dole = p20;p13.levo = p12;p13.gore = p5;p14.dole = p23;p14.levo = p13;p14.gore = p2;p15.desno = p16;p15.gore = p11;p16.desno = p17;p16.dole = p19;p16.levo = p15;p17.levo = p16;p17.gore = p12
p18.desno = p19;p18.gore = p10;p19.desno = p20;p19.dole = p22;p19.levo = p18;p19.gore = p16;p20.levo = p19;p20.gore = p13;p21.desno = p22;p21.gore = p9;p22.desno = p23;p22.levo = p21;p22.gore = p19;p23.levo = p22;p23.gore = p14

p0.skokovi = [p1,p9] ; p1.skokovi = [p0,p2,p4] ; p2.skokovi = [p1,p5] ; p3.skokovi = [p4,p10] ; p4.skokovi = [p5,p7,p3,p1] ; p5.skokovi = [p13,p4] ; p6.skokovi = [p7,p11]
p7.skokovi = [p8,p6,p4] ; p8.skokovi = [p12,p7] ; p9.skokovi = [p10,p21,p0] ; p10.skokovi = [p11,p18,p9,p3] ; p11.skokovi = [p15,p10,p6] ; p12.skokovi = [p13,p17,p8]
p13.skokovi = [p14,p20,p12,p5] ; p14.skokovi = [p23,p13,p2] ; p15.skokovi = [p16,p11] ; p16.skokovi = [p17,p19,p15] ; p17.skokovi = [p16,p12] ; p18.skokovi = [p19,p10]
p19.skokovi = [p20,p22,p18,p16] ; p20.skokovi = [p19,p13] ; p21.skokovi = [p22,p9] ; p22.skokovi = [p23,p21,p19] ; p23.skokovi = [p22,p14]



sva_polja = {
    "0": p0 , "1": p1 , "2": p2 , "3": p3 , "4": p4 , "5": p5 , "6": p6 , "7": p7 ,
    "8": p8 , "9": p9 , "10": p10 , "11": p11 , "12": p12 , "13": p13 , "14": p14 , "15": p15,
    "16": p16 , "17": p17 , "18": p18 , "19": p19 , "20": p20 , "21": p21 , "22": p22 , "23": p23
}

for kljucevi in sva_polja.keys():
    hesmapa.dodajuhes(kljucevi,sva_polja[kljucevi].vr)

komsije = {

    "0": ["1","9"] , "1": ["2","4","0"] , "2": ["14","1"] , "3": ["4","10"] , "4": ["5","7","3","1"] , "5": ["13","4"] , "6": ["7","11"] , "7": ["8","6","4"] ,
    "8": ["12","7"] , "9": ["10","21","0"] , "10": ["11","18","9","3"] , "11": ["15","10","6"] , "12": ["13","17","8"] , "13": ["14","20","12","5"] , "14": ["23","13","2"] , "15": ["16","11"],
    "16": ["17","19","15"] , "17": ["16","12"] , "18": ["19","10"] , "19": ["20","22","18","16"] , "20": ["19","13"] , "21": ["22","9"] , "22": ["23","21","19"] , "23": ["22","14"]
}


br_b = 9
br_c = 9



def tabla(polja):
    print(polja["0"].vr +"(0)-----------------------------------"+polja["1"].vr +"(1)----------------------------------"+polja["2"].vr +"(2)")
    print("|                                      |                                     |")
    print("|                                      |                                     |")
    print("|                                      |                                     |")
    print("|          "+polja["3"].vr +"(3)------------------------"+polja["4"].vr +"(4)----------------------"+polja["5"].vr +"(5)        |")
    print("|            |                         |                         |           |")
    print("|            |                         |                         |           |")
    print("|            |                         |                         |           |")
    print("|            |         "+polja["6"].vr +"(6)------------"+polja["7"].vr +"(7)----------"+polja["8"].vr +"(8)        |           |")
    print("|            |           |                           |           |           |")
    print("|            |           |                           |           |           |")
    print(polja["9"].vr +"(9)------"+polja["10"].vr +"(10)--------"+polja["11"].vr +"(11)                         "+polja["12"].vr +"(12)-------"+polja["13"].vr +"(13)-------"+polja["14"].vr +"(14)")
    print("|            |           |                           |           |           |")
    print("|            |           |                           |           |           |")
    print("|            |         "+polja["15"].vr +"(15)-----------"+polja["16"].vr +"(16)---------"+polja["17"].vr +"(17)       |           |")
    print("|            |                         |                         |           |")
    print("|            |                         |                         |           |")
    print("|            |                         |                         |           |")
    print("|          "+polja["18"].vr +"(18)-----------------------"+polja["19"].vr +"(19)---------------------"+polja["20"].vr +"(20)       |")
    print("|                                      |                                     |")
    print("|                                      |                                     |")
    print("|                                      |                                     |")
    print(polja["21"].vr +"(21)----------------------------------"+polja["22"].vr +"(22)---------------------------------"+polja["23"].vr +"(23)")


def slobodna_polja():

    slobodna = []

    for kljuc , vred in sva_polja.items():
        if vred.vr == "*":
            slobodna.append(kljuc) 

    return slobodna

def slobodna_za_pomeranje(polje):

    moguca_za_pomeranje = []

    for polja in komsije[polje]:
        if sva_polja[polja].vr == "*":
            moguca_za_pomeranje.append(polja)

    return moguca_za_pomeranje


def broj_figura(figura):
    broj = 0
    for i in sva_polja.values():
        if i.vr == figura:
            broj+=1
    return broj

dostupna_polja = ('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23')

def provera_stage1():
    while True:
        polje = input("Unesite broj polja na koje zelite da postavite figuru: ")
        if polje not in dostupna_polja:
            print("Polje koje ste izabrali ne postoji! ")
        elif sva_polja[polje].vr == "*":
            return polje
        else:
            print("Polje koje ste izabrali je vec zauzeto! ")

def provera_uklanjanje():
    while True:
        polje = input("Unesite broj polja sa kog zelite da uklonite figuru: ")
        if polje not in dostupna_polja:
            print("Polje koje ste izabrali ne postoji! ")
        elif sva_polja[polje].vr == "C":
            return polje
        else:
            print("Polje koje ste izabrali nije C ili je prazno! ")

def provera_stage2():
    
    while True:
        polje = input("Unesite broj polja sa kog zelite da pomerite figuru: ")

        if polje not in dostupna_polja:
            print("Polje koje ste izabrali ne postoji! ")
        elif sva_polja[polje].vr == "B":
            moguca_za_pomeranje = slobodna_za_pomeranje(polje)
            if moguca_za_pomeranje:
                return polje,moguca_za_pomeranje
            else:
                print("Figura na polju koje ste izabrali ne moze da se pomeri! ")
        else:
            print("Polje koje ste izabrali nije B ili je prazno! ")

           

def mica(polje,polja,crnibeli):

    imamicu = False

    if polja[polje].desno:
        if polja[polje].desno.vr == crnibeli and polja[polje].desno.desno and polja[polje].desno.desno.vr == crnibeli:
            imamicu = True
        if polja[polje].levo:
            if polja[polje].levo.vr == crnibeli and polja[polje].desno.vr == crnibeli:
                imamicu = True
    if polja[polje].levo:
        if polja[polje].levo.vr == crnibeli and polja[polje].levo.levo and polja[polje].levo.levo.vr == crnibeli:
            imamicu = True
    if polja[polje].dole:
        if polja[polje].dole.vr == crnibeli and polja[polje].dole.dole and polja[polje].dole.dole.vr == crnibeli:
            imamicu = True
    if polja[polje].gore:
        if polja[polje].gore.vr == crnibeli and polja[polje].gore.gore and polja[polje].gore.gore.vr == crnibeli:
            imamicu = True
        if polja[polje].dole:
            if polja[polje].dole.vr == crnibeli and polja[polje].gore.vr == crnibeli:
               imamicu = True
    return imamicu



def broj_blokiranih(figura,sva_polja):

    br_neblokiranih = broj_figura(figura)
    br_nebl = br_neblokiranih

    for polje in sva_polja.values():

        if polje.vr == figura:

            if polje.desno:
                if polje.desno.vr == "*":
                    continue
            if polje.dole:
                if polje.dole.vr == "*":
                    continue
            if polje.levo:
                if polje.levo.vr == "*":
                    continue
            if polje.gore:
                if polje.gore.vr == "*":
                    continue
            br_nebl -= 1

    return (br_neblokiranih - br_nebl)


def provera_kraja():

    status = 0

    br_belih = broj_figura("B")
    br_crnih = broj_figura("C")

    broj_blokiranih_beli = broj_blokiranih("B",sva_polja)
    broj_blokiranih_crni = broj_blokiranih("C",sva_polja)

    if br_belih == broj_blokiranih_beli:
        status = 1
    if br_crnih == broj_blokiranih_crni:
        status = -1
    
    if br_belih < 3:
        status = 1
    if br_crnih < 3:
        status = -1
    
    return status


dvice_polja = [ ["0","1"], ["1","2"], ["3","4"], ["4","5"], ["6","7"], ["7","8"], ["15","16"], 
                ["16","17"], ["18","19"], ["19","20"], ["21","22"], ["22","23"], ["9","10"], ["10","11"],
                ["12","13"], ["13","14"], ["0","9"], ["9","21"], ["3","10"], ["10","18"], ["6","11"], 
                ["11","15"] ,["1","4"] ,["4","7"], ["16","19"], ["19","22"], ["8","12"], ["12","17"],
                ["5","13"], ["13","20"], ["2","14"], ["14","23"]]

trice_polja = [ ["0","1","2"], ["3","4","5"], ["6","7","8"], ["9","10","11"], ["12","13","14"], ["15","16","17"], 
                ["18","19","20"],["21","22","23"], ["0","9","21"], ["3","10","18"], ["6","11","15"],
                ["1","4","7"], ["16","19","22"], ["8","12","17"],["5","13","20"],["2","14","23"]]

tri_pis = [
    ["0","1","9","21","2"],["21","0","2","9","1"],["1","2","14","0","23"],["0","2","23","1","14"],
    ["1","2","14","0","23",],["2","23","21","14","22"],
    ["18","3","5","10","4"],["10","3","4","18","5"],["1","4","3","5","7"],["3","4","7","5","1"],["9","10","3","18","11"],["3","10","11","18","9"],["3","5","20","4","13"],["20","18","3","10","19"],
    ["1","4","5","3","7"],["7","4","5","3","1"],["6","7","4","1","8"],["8","7","4","6","1"],["4","5","13","3","20"],
    ["5","20","18","13","19"],["12","13","5","14","20"],["5","13","14","12","20"],
    ["6","8","17","7","12"],["17","15","6","16","11"],["6","11","10","9","15"],["11","6","7","15","8"],["15","6","8","11","7"],
    ["7","8","12","6","17"],
    ["8","17","15","12","16"],["8","12","13","17","14"],
    ["22","21","9","23","0"],["18","9","10","3","11"],["9","3","10","18","11"],#
    ["3","9","10","18","11"],["19","18","10","3","20"],["10","3","11","18","9"],["11","10","18","9","3"],["10","9","18","11","3"],["6","10","11","9","15"],["15","10","11","6","9"],
    ["11","3","10","9","18"],["11","6","10","15","9"],["15","11","15","17","6"],["11","7","6","8","15"],
    ["12","16","17","8","15"],["12","8","7","17","6"],["12","13","20","5","14"],["12","13","8","17","14"],["12","17","13","8","14"],
    ["13","14","20","12","5"],["20","13","12","5","14"],["13","12","8","17","14"],["12","13","17","8","14"],["13","4","5","3","20"],["13","20","19","5","18"],["13","12","5","14","20"],["13","14","5","12","20"],
    ["14","1","2","0","23"],["14","23","22","2","21"],["14","13","5","12","20"],["14","13","20","12","5"],
    ["15","17","8","12","16"],["15","11","16","17","6"],["15","17","6","16","11"],["15","16","19","17","22"],["15","11","10","6","9"],
    ["16","12","17","8","15"],["16","15","11","17","6"],["16","19","20","18","22"],["18","19","16","22","20"],["15","16","19","22","17"],
    ["17","1","19","22","20"],
    ["17","6","8","7","12"],["12","17","16","15","8"],["17","15","8","12","16"],["17","12","13","8","14"],
    ["18","5","20","13","19"],["18","19","10","20","3"],["22","19","18","16","20"],["11","18","10","9","3"],["18","10","9","3","11"],
    ["19","13","20","5","18"],["19","18","10","20","3"],["16","19","20","22","18"],["20","19","22","16","18"],#["17","1","19","22","20"]],
    ["20","3","5","4","13"],["20","13","19","5","18"],["20","5","18","13","19"],
    ["21","0","2","1","9"],["21","2","23","14","22"],["21","22","9","23","0"],["21","23","0","22","9"],
    ["22","14","23","2","21"],["22","19","20","16","18"],
    ["23","2","0","1","14"],["23","14","22","2","21"],["23","2","21","14","22"],["23","21","0","22","1"]
]

def broj_dvica_cf(figura):

    br_dv = 0

    for lis in trice_polja:
        if sva_polja[lis[0]].vr == figura and sva_polja[lis[1]].vr == figura and sva_polja[lis[2]].vr == "*":
            br_dv += 1
        elif sva_polja[lis[1]].vr == figura and sva_polja[lis[2]].vr == figura and sva_polja[lis[0]].vr == "*":
            br_dv += 1
        elif sva_polja[lis[0]].vr == figura and sva_polja[lis[2]].vr == figura and sva_polja[lis[1]].vr == "*":
            br_dv += 1

    return br_dv


def dvice(figura):

    dvice_ja = 0
    dvice_protivnik = 0
    razlika_dvice = 0
    protivnik = [figura , "*"]

    for dva_polja in dvice_polja:
        if sva_polja[dva_polja[0]].vr == figura and sva_polja[dva_polja[1]].vr == figura:
            dvice_ja += 1
            razlika_dvice += 1
        if sva_polja[dva_polja[0]].vr not in protivnik and sva_polja[dva_polja[1]].vr not in protivnik:
            dvice_protivnik += 1
            razlika_dvice -= 1
    return dvice_ja #,dvice_protivnik,razlika_dvice



def trice(figura):
    trice_ja = 0
    trice_protivnik = 0
    razlika_trice = 0
    protivnik = [figura , "*"]

    for tri_polja in trice_polja:
        if sva_polja[tri_polja[0]].vr == figura and sva_polja[tri_polja[1]].vr == figura and sva_polja[tri_polja[2]].vr == figura:
            trice_ja += 1
            razlika_trice += 1
        if sva_polja[tri_polja[0]].vr not in protivnik and sva_polja[tri_polja[1]].vr not in protivnik and sva_polja[tri_polja[2]].vr not in protivnik:
            trice_protivnik += 1
            razlika_trice -= 1

    return trice_ja #,trice_protivnik,razlika_trice

def blokirana_mica(figura):
    blokirane = 0
    protivnik = [figura, "*"]

    for polje in trice_polja:
        if sva_polja[polje[0]].vr not in protivnik and sva_polja[polje[1]].vr not in protivnik:
            if sva_polja[polje[2]].vr == figura:
                blokirane += 1
        elif sva_polja[polje[1]].vr not in protivnik and sva_polja[polje[2]].vr not in protivnik:
            if sva_polja[polje[0]].vr == figura:
                blokirane += 1
        elif sva_polja[polje[0]].vr not in protivnik and sva_polja[polje[2]].vr not in protivnik:
            if sva_polja[polje[1]].vr == figura:
                blokirane +=1

    return blokirane

def duple_trice(figura):
    duple_trice_ja = 0
    duple_trice_protivnik = 0 
    razlika_duple_trice = 0
    protivnik = [figura, "*"]

    for polje in ["4","10","13","19"]:
        tacka = sva_polja[polje]
        if tacka.vr == figura:
            if tacka.desno.vr == figura and tacka.dole.vr == figura and tacka.levo.vr == figura and tacka.gore.vr == figura:
                duple_trice_ja += 1
                razlika_duple_trice += 1
    for polje in ["1","16","7","22"]:
        tacka = sva_polja[polje]
        if tacka.vr == figura:
            if tacka.dole:
                if tacka.desno.vr == figura and tacka.dole.vr == figura and tacka.dole.dole.vr == figura and tacka.levo.vr == figura:
                    duple_trice_ja +=1
            if tacka.gore:
                if tacka.desno.vr == figura and tacka.levo.vr == figura and tacka.gore.vr == figura and tacka.gore.gore.vr == figura:
                    duple_trice_ja +=1
    for polje in ["11","14","9","12"]:
        tacka = sva_polja[polje]
        if tacka.vr == figura:
            if tacka.levo:
                if tacka.levo.vr == figura and tacka.levo.levo.vr == figura and tacka.gore.vr == figura and tacka.dole.vr == figura:
                    duple_trice_ja += 1
            if tacka.desno:
                if tacka.desno.vr == figura and tacka.desno.desno.vr == figura and tacka.gore.vr == figura and tacka.dole.vr == figura:
                    duple_trice_ja += 1
    for polje in ["0","3","6"]:
        tacka = sva_polja[polje]
        if tacka.vr == figura:
            if tacka.desno.vr == figura and tacka.desno.desno.vr == figura and tacka.dole.vr == figura and tacka.dole.dole.vr == figura:
                duple_trice_ja += 1
    for polje in ["2","5","8"]:
        tacka = sva_polja[polje]
        if tacka.vr == figura:
            if tacka.levo.vr == figura and tacka.levo.levo.vr == figura and tacka.dole.vr == figura and tacka.dole.dole.vr == figura:
                duple_trice_ja += 1
    for polje in ["17","20","23"]:
        tacka = sva_polja[polje]
        if tacka.vr == figura:
            if tacka.levo.vr == figura and tacka.levo.levo.vr == figura and tacka.gore.vr == figura and tacka.gore.gore.vr == figura:
                duple_trice_ja += 1
    for polje in ["21","18","15"]:
        tacka = sva_polja[polje]
        if tacka.vr == figura:
            if tacka.desno.vr == figura and tacka.desno.desno.vr == figura and tacka.gore.vr == figura and tacka.gore.gore.vr == figura:
                duple_trice_ja += 1
            
    return duple_trice_ja

def tri_konfiguracije(figura,polja):
    
    tri_k = 0
    
    for i in tri_pis:
        if polja[i[0]].vr == figura and polja[i[1]].vr == figura and polja[i[2]].vr == figura and polja[i[3]].vr == "*" and polja[i[4]].vr == "*":
            tri_k = 1
    return tri_k

def zatvorena_mica(figura,polja):

    zatvorena = 0
    for polje in polja.keys():
        if polja[polje].vr == figura:
            if mica(polje,polja,figura):
                zatvorena += 1
    return zatvorena

def zatvorena_mica2(figura,polja):
    zatvorene = 0

    for polje in trice_polja:
        if mica(polje[0],polja,figura) and polja[polje[1]].vr == figura and polja[polje[2]].vr == figura:
            zatvorene += 1
        elif polja[polje[0]].vr == figura and mica(polje[1],polja,figura) and polja[polje[2]].vr == figura:
            zatvorene += 1
        elif polja[polje[0]].vr == figura and polja[polje[2]].vr == figura and  mica(polje[2],polja,figura):
            zatvorene += 1
    return zatvorene

def sva_polja_mice(figura,polja):

    brf = broj_figura(figura)
    brumici = 0
    sveumici = False

    for kljuc in polja.keys():
        if polja[kljuc].vr == figura:
            if mica(kljuc,polja,figura):
                brumici += 1
    if brf == brumici:
        sveumici = True
    
    return sveumici


def otvorena_mica(figura,polja):

    otvorene = 0
    tru0 = False
    tru1 = False
    tru2 = False

    for ki in trice_polja:
        komsije0 = komsije[ki[0]]
        komsije1 = komsije[ki[1]]
        komsije2 = komsije[ki[2]]
        
        for k in komsije0:
            if polja[k].vr == figura:
                tru0 = True
                break
        for k1 in komsije1:
            if polja[k1].vr == figura:
                tru1 = True
                break
        for k2 in komsije2:
            if polja[k2].vr == figura:
                tru2 = True
                break

        if polja[ki[0]].vr == figura and polja[ki[1]].vr == figura and  polja[ki[2]].vr == "*" and tru2 == True:
            otvorene += 1
        elif polja[ki[0]].vr == figura and polja[ki[1]].vr == "*" and tru1 == True and polja[ki[2]].vr == figura:
            otvorene += 1
        elif tru0 == True and polja[ki[0]].vr == "*" and polja[ki[1]].vr == figura and polja[ki[2]].vr == figura:
            otvorene += 1

    return otvorene

def heuristike(figura,polja,stejdz):
    
    figure = ["B", "C", "*"]
    for i in figure:
        if i != figura and i != "*":
            protivnik = i
            break
    
    if stejdz == 1:
        zatvorene = zatvorena_mica(figura,polja) - zatvorena_mica(protivnik,polja)
        br_mica = trice(figura) - trice(protivnik)
        blokirane_figure =  broj_blokiranih(protivnik,polja) - broj_blokiranih(figura,polja)
        br_figura = br_b - br_c#broj_figura(protivnik) - broj_figura(figura)
        br_2pc = broj_dvica_cf(figura) - broj_dvica_cf(protivnik)
        tri_pis_conf = tri_konfiguracije(figura,polja) - tri_konfiguracije(protivnik,polja)
        br_bl_mica = blokirana_mica(figura) - blokirana_mica(protivnik)
        bodovi = 18*zatvorene + 26*br_mica + 1*blokirane_figure + 6*br_figura + 12*br_2pc + 11*br_bl_mica + 7*tri_pis_conf
        return bodovi
    elif stejdz == 2:
        zatvorene = zatvorena_mica2(figura,polja) - zatvorena_mica2(protivnik,polja)
        br_mica = trice(figura) - trice(protivnik)
        blokirane_figure =  broj_blokiranih(protivnik,polja) - broj_blokiranih(figura,polja)
        br_figura = br_b - br_c #broj_figura(protivnik) - broj_figura(figura)
        br_duplih_trica = duple_trice(figura) - duple_trice(protivnik)
        otvorene_mice = otvorena_mica(figura,polja) - otvorena_mica(protivnik,polja)
        br_bl_mica = blokirana_mica(figura) - blokirana_mica(protivnik)
        kraj = provera_kraja()

        bodovi = 14*zatvorene + 43*br_mica + 10*blokirane_figure + 8*br_figura +42*br_duplih_trica + 1086*kraj +7*otvorene_mice + 12*br_bl_mica
        return bodovi


brisanje = None

def zabrisanje(figura,polja):
    moguci = []

    for k in polja.keys():
        if polja[k].vr == figura:
            moguci.append(k)
    return moguci



def minimax(polja,dubina,ai,alfa,beta,stejdz):
    # pomocna = polja
    # pomocna2 = polja
    if dubina != 0:

        if ai:
            maxEval = -math.inf
            if stejdz == 1:
                
                polja_za_stage_1 = []
                for polje in sva_polja.keys():
                    if sva_polja[polje].vr == "*":
                        polja_za_stage_1.append(polje)

                for i in polja_za_stage_1:
                    #nova_tabla = copy.deepcopy(sva_polja)
                    polja[i].vr = "C"
                    if mica(i,polja,"C"):
                        micaje = True
                    else:
                        micaje = False
                    #tabla(polja)
                    noviminmax = minimax(polja,dubina-1,False,alfa,beta,stejdz)[2]
                    polja[i].vr = "*"

                    if noviminmax > maxEval:
                        maxEval = noviminmax
                        potez = i
                    alfa = max(alfa,maxEval)
                    if alfa >= beta:
                        break
                #npolja = polja
                #npolja[potez].vr = "C"
                return None,potez,maxEval,micaje
            if stejdz == 2:
                
                for polje in polja.keys():

                    if polja[polje].vr == "C":
                        moguca = slobodna_za_pomeranje(polje)
                        for mog in moguca:

                            polja[polje].vr = "*"
                            polja[mog].vr = "C"
                            #tabla(polja)
                            noviminmax = minimax(polja,dubina-1,False,alfa,beta,stejdz)[2]

                            polja[polje].vr = "C"
                            polja[mog].vr = "*"

                            if noviminmax > maxEval:
                                maxEval = noviminmax
                                potez1 = polje
                                potez2 = mog
                            alfa = max(alfa,maxEval)
                            if alfa >= beta:
                                break
                return potez1 , potez2 , maxEval
        else:
            minEval = math.inf
            if stejdz == 1:

                polja_za_igranje = []
                for polje in sva_polja.keys():
                    if sva_polja[polje].vr == "*":
                        polja_za_igranje.append(polje)
                for i in polja_za_igranje:
                    polja[i].vr = "B"
                    if mica(i,polja,"C"):
                        micaje = True
                    else:
                        micaje = False
                        
                    noviminmax = minimax(polja,dubina-1,True,alfa,beta,stejdz)[2]
                    polja[i].vr = "*"
                    if noviminmax < minEval:
                        minEval = noviminmax
                        potez = i

                    beta = min(beta,minEval)
                    if alfa >= beta:
                        break
                #npolja = polja
                #npolja[potez].vr = "B"
                return None,potez,minEval,micaje
            if stejdz == 2:
                for polje in polja.keys():

                    if polja[polje].vr == "B":
                        moguca = slobodna_za_pomeranje(polje)
                        for mog in moguca:
                                
                            polja[polje].vr = "*"
                            polja[mog].vr = "B"

                            noviminmax = minimax(polja,dubina-1,True,alfa,beta,stejdz)[2]
                            polja[polje].vr = "B"
                            polja[mog].vr = "*"
                            if noviminmax < minEval:
                                minEval = noviminmax
                                potez3 = polje
                                potez4 = mog
                            beta = min(beta,minEval)
                            if alfa >= beta:
                                break
                return potez3,potez4, minEval
            
    else:
        m = heuristike("C",polja,stejdz)

        # if ai:
        #     m = heuristike("C",polja,stejdz)
        # else:
        #     m = -(heuristike("B",polja,stejdz))
    return None,None,m,None


def minimaxbrisanje(polja,dubina,ai,alfa,beta,stejdz):

    if dubina != 0:

        if ai:
            maxEval = -math.inf

            if stejdz == 1:
                brisanje = []

                for p in polja.keys():
                    if polja[p].vr == "B":
                        if sva_polja_mice("B",polja):
                            brisanje.append(p)
                        elif not mica(p,polja,"B"):
                            brisanje.append(p)
                
                for b in brisanje:
                    polja[b].vr = "*"

                    novim = minimaxbrisanje(polja,dubina-1,False,alfa,beta,stejdz)[2]

                    polja[b].vr = "B"

                    if novim > maxEval:
                        maxEval = novim
                        potez = b
                        alfa = max(alfa,maxEval)
                        if alfa >= beta:
                            break
                return None,potez,maxEval
        else:
            minEval = math.inf
            if stejdz == 1:
                brisanje = []

                for p in polja.keys():
                    if polja[p].vr == "C":
                
                        if sva_polja_mice("C",polja):
                            brisanje.append(p)
                        elif not mica(p,polja,"C"):
                            brisanje.append(p)
                            
                
                for b in brisanje:
                    polja[b].vr = "*"

                    novim = minimaxbrisanje(polja,dubina-1,True,alfa,beta,stejdz)[2]

                    polja[b].vr = "C"

                    if novim < minEval:
                        minEval = novim
                        potez = b
                        beta = min(beta,minEval)
                        if alfa >= beta:
                            break
                return None,potez,minEval
    else:
       m = heuristike("C",polja,stejdz)
        # if ai:
        #     m = heuristike("C",polja,stejdz)
        # else:
        #     m = -(heuristike("B",polja,stejdz))
    return None,None,m



def igra(sva_polja):
    br_b = 9
    br_c = 9

    # sva_polja["0"].vr = "C"
    # sva_polja["1"].vr = "C"
    # sva_polja["2"].vr = "C"
    # sva_polja["14"].vr = "B"
    # sva_polja["20"].vr = "B"

    # print("SVE U MICI: " + str(sva_polja_mice("B",sva_polja)))

    for i in range(9):
        alfa = float("-inf")
        beta = float("inf")
        tabla(sva_polja)
        slobodna = slobodna_polja()
        print("Polja na koja mozete postaviti figuru su: " + (", ").join(x for x in slobodna) )
        polje = provera_stage1()
        sva_polja[polje].vr = "B"
        if mica(polje,sva_polja,"B"):
            tabla(sva_polja)
            while True:
                polje2 = provera_uklanjanje()
                
                if sva_polja_mice("C",sva_polja):
                    sva_polja[polje2].vr = "*"
                    br_c -= 1
                    break
                elif mica(polje2,sva_polja,"C"):
                    print("Figura koju ste izabrali ne moze biti uklonjena! ")
                else:
                    sva_polja[polje2].vr = "*"
                    br_c -= 1
                    break

        pocetak = time.time()
        potez = minimax(sva_polja,3,True,alfa,beta,1)
        potez1 = potez[1]
        sva_polja[potez1].vr = "C"
        if mica(potez1,sva_polja,"C"):
            bris = minimaxbrisanje(sva_polja,4,True,alfa,beta,1)[1]
            sva_polja[bris].vr = "*"
            br_b -= 1
        kraj = time.time()
        print("Vreme poteza bota: " + str((kraj - pocetak)))

    status = provera_kraja()
    if status == 1:
        print("Nazalost , racunar je pobedio :( ")
        exit()
    if status == -1:
        print("Cestitamo , pobedili ste racunar! ")
        exit()

    # ------------------- STAGE 2 ----------------------
    alfa = float("-inf")
    beta = float("inf")
    while True:
        tabla(sva_polja)
        polje,moguca_za_pomeranje= provera_stage2()
        print("Polja na koja mozete pomeriti figuru su: " + (", ").join(x for x in moguca_za_pomeranje) )

        polje2 = input("Unesite polje na koje zelite da pomerite figuru: ")
        if polje2 not in moguca_za_pomeranje:
            print("Ne mozete da pomerite figuru na polje koje ste izabrali! ")
        else:
            sva_polja[polje].vr = "*"
            sva_polja[polje2].vr = "B"
            hesmapa.setujvr(polje,"*")
            hesmapa.setujvr(polje2,"B")

        if mica(polje2,sva_polja,"B"):
            tabla(sva_polja)
            while True:
                polje3 = provera_uklanjanje()

                if sva_polja_mice("C",sva_polja):
                    sva_polja[polje3].vr = "*"
                    hesmapa.setujvr(polje3,"*")
                    br_b -= 1
                    break
                elif mica(polje3,sva_polja,"C"):
                    print("Figura koju ste izabrali ne moze biti uklonjena! ")
                else:
                    sva_polja[polje3].vr = "*"
                    hesmapa.setujvr(polje3,"*")
                    br_b -= 1
                    break

            status = provera_kraja()
            if status == 1:
                print("Nazalost , racunar je pobedio :( ")
                exit()
            if status == -1:
                print("Cestitamo , pobedili ste racunar! ")
                exit()

        pocetak = time.time()
        potez = minimax(sva_polja,4,True,alfa,beta,2)
        #potez2 = minimax(sva_polja,3,True,alfa,beta,2)[1]
        potez1 = potez[0]
        potez2 = potez[1]
        sva_polja[potez1].vr = "*"
        sva_polja[potez2].vr = "C"
        hesmapa.setujvr(potez1,"*")
        hesmapa.setujvr(potez2,"C")
        if mica(potez2,sva_polja,"C"):
            bris = minimaxbrisanje(sva_polja,3,True,alfa,beta,1)[1]
            sva_polja[bris].vr = "*"
            hesmapa.setujvr(bris,"*")
            br_b -= 1
        kraj = time.time()
        print("Vreme poteza bota: " + str((kraj - pocetak)))
        status = provera_kraja()
        if status == 1:
            print("Nazalost , racunar je pobedio :( ")
            exit()
        if status == -1:
            print("Cestitamo , pobedili ste racunar! ")
            exit()


def igra2(sva_polja):
    br_b = 9
    br_c = 9

    for i in range(9):
        alfa = float("-inf")
        beta = float("inf")

        pocetak = time.time()
        potez = minimax(sva_polja,3,True,alfa,beta,1)
        potez1 = potez[1]
        sva_polja[potez1].vr = "C"
        hesmapa.setujvr(potez1,"C")
        if mica(potez1,sva_polja,"C"):
            bris = minimaxbrisanje(sva_polja,3,True,alfa,beta,1)[1]
            sva_polja[bris].vr = "*"
            hesmapa.setujvr(bris,"*")
            br_b -= 1
        kraj = time.time()
        print("Vreme poteza bota: " + str((kraj - pocetak)))

        tabla(sva_polja)
        slobodna = slobodna_polja()
        print("Polja na koja mozete postaviti figuru su: " + (", ").join(x for x in slobodna) )
        polje = provera_stage1()
        sva_polja[polje].vr = "B"
        hesmapa.setujvr(polje,"B")

        if mica(polje,sva_polja,"B"):
            tabla(sva_polja)
            while True:
                polje2 = provera_uklanjanje()

                if sva_polja_mice("C",sva_polja):
                    sva_polja[polje2].vr = "*"
                    hesmapa.setujvr(polje2,"*")
                    br_c -= 1
                    break
                elif mica(polje2,sva_polja,"C"):
                    print("Figura koju ste izabrali ne moze biti uklonjena! ")
                else:
                    sva_polja[polje2].vr = "*"
                    hesmapa.setujvr(polje2,"*")
                    br_c -= 1
                    break

    status = provera_kraja()
    if status == 1:
        print("Nazalost , racunar je pobedio :( ")
        exit()
    if status == -1:
        print("Cestitamo , pobedili ste racunar! ")
        exit()

    # ------------------- STAGE 2 ----------------------
    alfa = float("-inf")
    beta = float("inf")
    while True:

        pocetak = time.time()
        potez = minimax(sva_polja,4,True,alfa,beta,2)
        potez1 = potez[0]
        potez2 = potez[1]
        sva_polja[potez1].vr = "*"
        sva_polja[potez2].vr = "C"
        hesmapa.setujvr(potez1,"*")
        hesmapa.setujvr(potez2,"C")
        if mica(potez2,sva_polja,"C"):
            bris = minimaxbrisanje(sva_polja,3,True,alfa,beta,1)[1]
            sva_polja[bris].vr = "*"
            hesmapa.setujvr(bris,"*")
            br_b -= 1
        kraj = time.time()
        print("Vreme poteza bota: " + str((kraj - pocetak)))

        tabla(sva_polja)
        polje,moguca_za_pomeranje= provera_stage2()
        print("Polja na koja mozete pomeriti figuru su: " + (", ").join(x for x in moguca_za_pomeranje) )

        polje2 = input("Unesite polje na koje zelite da pomerite figuru: ")
        if polje2 not in moguca_za_pomeranje:
            print("Ne mozete da pomerite figuru na polje koje ste izabrali! ")
        else:
            sva_polja[polje].vr = "*"
            sva_polja[polje2].vr = "B"
            hesmapa.setujvr(polje,"*")
            hesmapa.setujvr(polje2,"B")

        if mica(polje2,sva_polja,"B"):
            tabla(sva_polja)
            while True:
                polje3 = provera_uklanjanje()

                if sva_polja_mice("C",sva_polja):
                    sva_polja[polje3].vr = "*"
                    hesmapa.setujvr(polje2,"*")
                    br_c -= 1
                    break
                elif mica(polje3,sva_polja,"C"):
                    print("Figura koju ste izabrali ne moze biti uklonjena! ")
                else:
                    sva_polja[polje3].vr = "*"
                    hesmapa.setujvr(polje3,"*")
                    br_b -= 1
                    break

            status = provera_kraja()
            if status == 1:
                print("Nazalost , racunar je pobedio :( ")
                exit()
            if status == -1:
                print("Cestitamo , pobedili ste racunar! ")
                exit()
        status = provera_kraja()
        if status == 1:
            print("Nazalost , racunar je pobedio :( ")
            exit()
        if status == -1:
            print("Cestitamo , pobedili ste racunar! ")
            exit()

def izbor():
    print("")
    print("Izaberite jednu od opcija: ")
    print("")
    print("1. Vi igrate prvi")
    print("2. Racunar igra prvi")
    
    while True:
        iz = input(">>> ")
        if iz not in ("1","2"):
            print("Izabrali ste pogresnu opciju. ")
        else:
            break

    if iz == "1":
        igra(sva_polja)
    elif iz == "2":
        igra2(sva_polja)

if __name__ == "__main__":
    izbor()



