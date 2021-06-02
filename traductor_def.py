import msvcrt

# GUI
print("Selecciona el modo que quieras ejectuar el programa")
print("1 - Numeros a Texto")
print("2 - Texto a Numeros")
ans = input("> ")

if (ans == "1"):
    n = input("Numeros > ")
    n = n.split()

    # Cantidad de caracteres iguales
    n2 = n.count("2")
    n22 = n.count("22")
    n222 = n.count("222")
    n3 = n.count("3")
    n33 = n.count("33")
    n333 = n.count("333")
    n4 = n.count("4")
    n44 = n.count("44")
    n444 = n.count("444")
    n5 = n.count("5")
    n55 = n.count("55")
    n555 = n.count("555")
    n6 = n.count("6")
    n66 = n.count("66")
    n666 = n.count("666")
    n7 = n.count("7")
    n77 = n.count("77")
    n777 = n.count("777")
    n7777 = n.count("7777")
    n8 = n.count("8")
    n88 = n.count("88")
    n888 = n.count("888")
    n9 = n.count("9")
    n99 = n.count("99")
    n999 = n.count("999")
    n9999 = n.count("9999")
    n0 = n.count("0")

    # " "
    x = 0
    while(x < n0):
        x = x+1
        x0 = n.index("0")
        x0 = int(x0)
        del(n[x0])
        n.insert(x0, " ")

    # A
    x = 0
    while(x < n2):
        x = x+1
        x2 = n.index("2")
        x2 = int(x2)
        del(n[x2])
        n.insert(x2, "a")

    # B
    x = 0
    while(x < n22):
        x = x+1
        x22 = n.index("22")
        x22 = int(x22)
        del(n[x22])
        n.insert(x22, "b")

    # C
    x = 0
    while(x < n222):
        x = x+1
        x222 = n.index("222")
        x222 = int(x222)
        del(n[x222])
        n.insert(x222, "c")

    # D
    x = 0
    while(x < n3):
        x = x+1
        x3 = n.index("3")
        x3 = int(x3)
        del(n[x3])
        n.insert(x3, "d")

    # E
    x = 0
    while(x < n33):
        x = x+1
        x33 = n.index("33")
        x33 = int(x33)
        del(n[x33])
        n.insert(x33, "e")

    # F
    x = 0
    while(x < n333):
        x = x+1
        x333 = n.index("333")
        x333 = int(x333)
        del(n[x333])
        n.insert(x333, "f")

    # G
    x = 0
    while(x < n4):
        x = x+1
        x4 = n.index("4")
        x4 = int(x4)
        del(n[x4])
        n.insert(x4, "g")

    # H
    x = 0
    while(x < n44):
        x = x+1
        x44 = n.index("44")
        x44 = int(x44)
        del(n[x44])
        n.insert(x44, "h")

    # I
    x = 0
    while(x < n444):
        x = x+1
        x444 = n.index("444")
        x444 = int(x444)
        del(n[x444])
        n.insert(x444, "i")

    # J
    x = 0
    while(x < n5):
        x = x+1
        x5 = n.index("5")
        x5 = int(x5)
        del(n[x5])
        n.insert(x5, "j")

    # K
    x = 0
    while(x < n55):
        x = x+1
        x55 = n.index("55")
        x55 = int(x55)
        del(n[x55])
        n.insert(x55, "k")

    # L
    x = 0
    while(x < n555):
        x = x+1
        x555 = n.index("555")
        x555 = int(x555)
        del(n[x555])
        n.insert(x555, "l")

    # M
    x = 0
    while(x < n6):
        x = x+1
        x6 = n.index("6")
        x6 = int(x6)
        del(n[x6])
        n.insert(x6, "m")

    # N
    x = 0
    while(x < n66):
        x = x+1
        x66 = n.index("66")
        x66 = int(x66)
        del(n[x66])
        n.insert(x66, "n")

    # O
    x = 0
    while(x < n666):
        x = x+1
        x666 = n.index("666")
        x666 = int(x666)
        del(n[x666])
        n.insert(x666, "o")

    # P
    x = 0
    while(x < n7):
        x = x+1
        x7 = n.index("7")
        x7 = int(x7)
        del(n[x7])
        n.insert(x7, "p")

    # Q
    x = 0
    while(x < n77):
        x = x+1
        x77 = n.index("77")
        x77 = int(x77)
        del(n[x77])
        n.insert(x77, "q")

    # R
    x = 0
    while(x < n777):
        x = x+1
        x777 = n.index("777")
        x777 = int(x777)
        del(n[x777])
        n.insert(x777, "r")

    # S
    x = 0
    while(x < n7777):
        x = x+1
        x7777 = n.index("7777")
        x7777 = int(x7777)
        del(n[x7777])
        n.insert(x7777, "s")

    # T
    x = 0
    while(x < n8):
        x = x+1
        x8 = n.index("8")
        x8 = int(x8)
        del(n[x8])
        n.insert(x8, "t")

    # U
    x = 0
    while(x < n88):
        x = x+1
        x88 = n.index("88")
        x88 = int(x88)
        del(n[x88])
        n.insert(x88, "u")

    # V
    x = 0
    while(x < n888):
        x = x+1
        x888 = n.index("888")
        x888 = int(x888)
        del(n[x888])
        n.insert(x888, "v")

    # W
    x = 0
    while(x < n9):
        x = x+1
        x9 = n.index("9")
        x9 = int(x9)
        del(n[x9])
        n.insert(x9, "w")

    # X
    x = 0
    while(x < n99):
        x = x+1
        x99 = n.index("99")
        x99 = int(x99)
        del(n[x99])
        n.insert(x99, "x")

    # Y
    x = 0
    while(x < n999):
        x = x+1
        x999 = n.index("999")
        x999 = int(x999)
        del(n[x999])
        n.insert(x999, "y")

    # Z
    x = 0
    while(x < n9999):
        x = x+1
        x9999 = n.index("9999")
        x9999 = int(x9999)
        del(n[x9999])
        n.insert(x9999, "z")

if (ans == "2"):
    n = input("Texto > ")
    n = list(n)

    # Cantidad de caracteres iguales
    n2 = n.count("a")
    n22 = n.count("b")
    n222 = n.count("c")
    n3 = n.count("d")
    n33 = n.count("e")
    n333 = n.count("f")
    n4 = n.count("g")
    n44 = n.count("h")
    n444 = n.count("i")
    n5 = n.count("j")
    n55 = n.count("k")
    n555 = n.count("l")
    n6 = n.count("m")
    n66 = n.count("n")
    n666 = n.count("o")
    n7 = n.count("p")
    n77 = n.count("q")
    n777 = n.count("r")
    n7777 = n.count("s")
    n8 = n.count("t")
    n88 = n.count("u")
    n888 = n.count("v")
    n9 = n.count("w")
    n99 = n.count("x")
    n999 = n.count("y")
    n9999 = n.count("z")
    n0 = n.count(" ")

    # " "
    x = 0
    while(x<n0):
        x = x+1
        x0 = n.index(" ")
        x0 = int(x0)
        del(n[x0])
        n.insert(x0, "0 ")

    # A
    x = 0
    while(x<n2):
        x = x+1
        x2 = n.index("a")
        x2 = int(x2)
        del(n[x2])
        n.insert(x2, "2 ")

    # B
    x = 0
    while(x<n22):
        x = x+1
        x22 = n.index("b")
        x22 = int(x22)
        del(n[x22])
        n.insert(x22, "22 ")

    # C
    x = 0
    while(x<n222):
        x = x+1
        x222 = n.index("c")
        x222 = int(x222)
        del(n[x222])
        n.insert(x222, "222 ")

    # D
    x = 0
    while(x<n3):
        x = x+1
        x3 = n.index("d")
        x3 = int(x3)
        del(n[x3])
        n.insert(x3, "3 ")

    # E
    x = 0
    while(x<n33):
        x = x+1
        x33 = n.index("e")
        x33 = int(x33)
        del(n[x33])
        n.insert(x33, "33 ")

    # F
    x = 0
    while(x<n333):
        x = x+1
        x333 = n.index("f")
        x333 = int(x333)
        del(n[x333])
        n.insert(x333, "333 ")

    # G
    x = 0
    while(x<n4):
        x = x+1
        x4 = n.index("g")
        x4 = int(x4)
        del(n[x4])
        n.insert(x4, "4 ")

    # H
    x = 0
    while(x<n44):
        x = x+1
        x44 = n.index("h")
        x44 = int(x44)
        del(n[x44])
        n.insert(x44, "44 ")

    # I
    x = 0
    while(x<n444):
        x = x+1
        x444 = n.index("i")
        x444 = int(x444)
        del(n[x444])
        n.insert(x444, "444 ")

    # J
    x = 0
    while(x<n5):
        x = x+1
        x5 = n.index("j")
        x5 = int(x5)
        del(n[x5])
        n.insert(x5, "5 ")

    # K
    x = 0
    while(x<n55):
        x = x+1
        x55 = n.index("k")
        x55 = int(x55)
        del(n[x55])
        n.insert(x55, "55 ")

    # L
    x = 0
    while(x<n555):
        x = x+1
        x555 = n.index("l")
        x555 = int(x555)
        del(n[x555])
        n.insert(x555, "555 ")

    # M
    x = 0
    while(x<n6):
        x = x+1
        x6 = n.index("m")
        x6 = int(x6)
        del(n[x6])
        n.insert(x6, "6 ")

    # N
    x = 0
    while(x<n66):
        x = x+1
        x66 = n.index("n")
        x66 = int(x66)
        del(n[x66])
        n.insert(x66, "66 ")

    # O
    x = 0
    while(x<n666):
        x = x+1
        x666 = n.index("o")
        x666 = int(x666)
        del(n[x666])
        n.insert(x666, "666 ")

    # P
    x = 0
    while(x<n7):
        x = x+1
        x7 = n.index("p")
        x7 = int(x7)
        del(n[x7])
        n.insert(x7, "7 ")

    # Q
    x = 0
    while(x<n77):
        x = x+1
        x77 = n.index("q")
        x77 = int(x77)
        del(n[x77])
        n.insert(x77, "77 ")

    # R
    x = 0
    while(x<n777):
        x = x+1
        x777 = n.index("r")
        x777 = int(x777)
        del(n[x777])
        n.insert(x777, "777 ")

    # S
    x = 0
    while(x<n7777):
        x = x+1
        x7777 = n.index("s")
        x7777 = int(x7777)
        del(n[x7777])
        n.insert(x7777, "7777 ")

    # T
    x = 0
    while(x<n8):
        x = x+1
        x8 = n.index("t")
        x8 = int(x8)
        del(n[x8])
        n.insert(x8, "8 ")

    # U
    x = 0
    while(x<n88):
        x = x+1
        x88 = n.index("u")
        x88 = int(x88)
        del(n[x88])
        n.insert(x88, "88 ")

    # V
    x = 0
    while(x<n888):
        x = x+1
        x888 = n.index("v")
        x888 = int(x888)
        del(n[x888])
        n.insert(x888, "888 ")

    # W
    x = 0
    while(x<n9):
        x = x+1
        x9 = n.index("w")
        x9 = int(x9)
        del(n[x9])
        n.insert(x9, "9 ")

    # X
    x = 0
    while(x<n99):
        x = x+1
        x99 = n.index("x")
        x99 = int(x99)
        del(n[x99])
        n.insert(x99, "99 ")

    # Y
    x = 0
    while(x<n999):
        x = x+1
        x999 = n.index("y")
        x999 = int(x999)
        del(n[x999])
        n.insert(x999, "999 ")

    # Z
    x = 0
    while(x<n9999):
        x = x+1
        x9999 = n.index("z")
        x9999 = int(x9999)
        del(n[x9999])
        n.insert(x9999, "9999 ")

# Print traduccion
strN = "".join(n)
print(strN)
msvcrt.getch()