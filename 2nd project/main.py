def get_int (weight, height) :
    imt = weight / (height * height)

    if imt < 19 :
        print ("У вас перевес")
    elif imt > 25:
        print ("У вас перевес")
    else :
        print ("У вас все нормально")

get_int (56, 1.65)
