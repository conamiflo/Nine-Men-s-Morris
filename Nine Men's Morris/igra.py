from polja import *

def igra():
    #----------stage1--------------

    # sva_polja["0"].vr = "B"
    # sva_polja["1"].vr = "B"
    # sva_polja["7"].vr = "B"
    # sva_polja["2"].vr = "B"
    # sva_polja["9"].vr = "B"
    # sva_polja["21"].vr = "B"
    # sva_polja["11"].vr = "B"
    #sva_polja["6"].vr = "C"
    # sva_polja["15"].vr = "C"
    # sva_polja["4"].vr = "B"
    # sva_polja["10"].vr = "B"
    #sva_polja["17"].vr = "C"
    #sva_polja["8"].vr = "C"

    #sva_polja["13"].vr = "C"
    #sva_polja["14"].vr = "C"
    #sva_polja["12"].vr = "C"
    #sva_polja["5"].vr = "C"
    # sva_polja["23"].vr = "B"
    #sva_polja["16"].vr = "C"

    # sva_polja["3"].vr = "B"
    #sva_polja["18"].vr = "C"

    sva_polja = {
    "0": p0 , "1": p1 , "2": p2 , "3": p3 , "4": p4 , "5": p5 , "6": p6 , "7": p7 ,
    "8": p8 , "9": p9 , "10": p10 , "11": p11 , "12": p12 , "13": p13 , "14": p14 , "15": p15,
    "16": p16 , "17": p17 , "18": p18 , "19": p19 , "20": p20 , "21": p21 , "22": p22 , "23": p23
    }


    # # tabla()
    # # print("Broj blokiranih B: " + str(broj_blokiranih("B",sva_polja)))

    # #print(dvice("C",dvice_polja))

    # # ja,protivnik,razlika = trice("B",trice_polja)


    # print("-----------------------------------")
    # ja = trice("B")
    # protivnik = trice("C")
    # razlika = ja - protivnik
    # print("JA 3: " + str(ja))
    # print("PROTIVNIK 3: " + str(protivnik) )
    # print("RAZLIKA 3 : " + str(razlika))

    # print("-----------------------------------")

    # ja2 = dvice("B")
    # protivnik2 = dvice("C")
    # razlika2= ja2 - protivnik2
    # print("JA 2: " + str(ja2))
    # print("PROTIVNIK 2: " + str(protivnik2) )
    # print("RAZLIKA 2 : " + str(razlika2))

    # print("-----------------------------------")

    # ja3 = duple_trice("B")
    # protivnik3 = duple_trice("C")
    # razlika3= ja3 - protivnik3
    # print("JA DUPLE 3: " + str(ja3) )
    # print("PROTIVNIK DUPLE 3: "+ str(protivnik3))
    # print("RAZLIKA DUPLE 3: " + str(razlika3))

    # print("-----------------------------------")

    # print("BLOKIRANE MICE ZA B: " + str(blokirana_mica("B")))
    # print("BLOKIRANE MICE ZA C: " + str(blokirana_mica("C")))

    for i in range(9):

        alfa = float("-inf")
        beta = float("inf")
        tabla()
        slobodna = slobodna_polja()
        print("Polja na koja mozete postaviti figuru su: " + (", ").join(x for x in slobodna) )
        polje = provera_stage1()
        sva_polja[polje].vr = "B"

        if mica(polje,sva_polja,"B"):
            tabla()
            while True:
                polje2 = provera_uklanjanje()

                if mica(polje2,sva_polja,"C"):
                    print("Figura koju ste izabrali ne moze biti uklonjena! ")
                else:
                    sva_polja[polje2].vr = "*"
                    break

        # pocetak = time.time()
        potez_bota = minimax(sva_polja,3,True,alfa,beta,1)
        sva_polja = potez_bota
        tabla()
        # potez bota

        # kraj = time.time()
        # vreme = kraj - pocetak

    status = provera_kraja()
    if status == 1:
        print("Nazalost , racunar je pobedio :( ")
        exit()
    if status == -1:
        print("Cestitamo , pobedili ste racunar! ")
        exit()

    # ------------------- STAGE 2 ----------------------

    while True:
        tabla()
        polje,moguca_za_pomeranje= provera_stage2()
        print("Polja na koja mozete pomeriti figuru su: " + (", ").join(x for x in moguca_za_pomeranje) )

        polje2 = input("Unesite polje na koje zelite da pomerite figuru: ")
        if polje2 not in moguca_za_pomeranje:
            print("Ne mozete da pomerite figuru na polje koje ste izabrali! ")
        else:
            sva_polja[polje].vr = "*"
            sva_polja[polje2].vr = "B"

        if mica(polje2,sva_polja,"B"):
            tabla()
            while True:
                polje3 = provera_uklanjanje()

                if mica(polje3,sva_polja,"C"):
                    print("Figura koju ste izabrali ne moze biti uklonjena! ")
                else:
                    sva_polja[polje3].vr = "*"
                    break

            status = provera_kraja()
            if status == 1:
                print("Nazalost , racunar je pobedio :( ")
                exit()
            if status == -1:
                print("Cestitamo , pobedili ste racunar! ")
                exit()

        # pocetak = time.time()

        # potez bota

        # kraj = time.time()
        # vreme = kraj - pocetak

        status = provera_kraja()
        if status == 1:
            print("Nazalost , racunar je pobedio :( ")
            exit()
        if status == -1:
            print("Cestitamo , pobedili ste racunar! ")
            exit()


if __name__ == "__main__":
    igra()