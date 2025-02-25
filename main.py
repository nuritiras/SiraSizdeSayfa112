def yildiz_ucgen_ciz(satirSayisi):
    print( str(satirSayisi) + " satırlık yıldız üçgen çiziliyor:")
    for satir in range(0,satirSayisi):
        print ("*" * satir+" "*(satirSayisi-satir)*2+"*" * satir)

    for satir in range(satirSayisi,0,-1):
        print ("*" * satir+" "*(satirSayisi-satir)*2+"*" * satir)


yildiz_ucgen_ciz(8)