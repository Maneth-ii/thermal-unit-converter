F_or_C = input("Enter You Want eg:'F to C' or 'C to F' or 'C to K' or 'K to C': ")



if F_or_C == "F to C":
    F = float(input("Enter Farenhite Value: "))
    C = (F-32)*5/9
    print(C,"Celcius")

elif F_or_C == "C to F":
    C = float(input("Enter Celsius Value: "))
    F = (9/5*C)+32
    print(F,"Farenhite")

elif F_or_C == "C to K":
    C = float(input("Enter Celcius Value: "))
    K = C + 273
    print(K, "Kelvin")


elif F_or_C == "K to C":
    K = float(input("Enter Kelvin Value: "))
    C = K - 273
    print(C, "Celsius")

input()