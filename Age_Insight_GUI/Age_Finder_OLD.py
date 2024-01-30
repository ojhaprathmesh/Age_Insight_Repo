# ====================================Label=====================================

print("                                                             Age Finder by Prathmesh Ojha")
print("Enter The Date In The Form YYYYDDMM.")
print("Suggestion:-Num Lk Keypad Can Be Used.")

# ====================================Input=====================================

bd1 = int(input("Enter The Birth Date:-"))
cd1 = int(input("Enter The Current Date:-"))

# ===============================Main Calculation===============================

bd2 = (bd1 % 100000000) - (bd1 % 10000)
bd2 = bd2 / 10000
cd2 = (cd1 % 100000000) - (cd1 % 10000)
cd2 = cd2 / 10000
y1 = (bd1 % 100000000) - (bd1 % 10000)
y1 = y1 / 10000
y2 = (cd1 % 100000000) - (cd1 % 10000)
y2 = y2 / 10000
m1 = bd1 % 100
m2 = cd1 % 100
d1 = (bd1 % 10000) - (bd1 % 100)
d1 = d1 / 100
d2 = (cd1 % 10000) - (cd1 % 100)
d2 = d2 / 100

# ====================================Logics====================================

while bd2 > cd2:
    print("Please Check The Years And Enter Full Date Again")
    bd1 = int(input("Enter The Birth Date:-"))
    cd1 = int(input("Enter The Current Date:-"))
    bd2 = (bd1 % 100000000) - (bd1 % 10000)
    bd2 = bd2 / 10000
    cd2 = (cd1 % 100000000) - (cd1 % 10000)
    cd2 = cd2 / 10000

while m1 > 12:
    print("Please Check The Birth Month And Enter Full Date Again")

while m2 > 12:
    print("Please Check The Current Month And Enter Full Date Again")

if m1 == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    if m2 == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        while d2 > 31:
            print("Please Check The Current Day And Enter Full Date Again")
            cd1 = int(input("Enter The Current Date:-"))
            d2 = (cd1 % 10000) - (cd1 % 100)
            d2 = d2 / 100
    elif m2 == 4 or 6 or 9 or 11:
        while d2 > 30:
            print("Please Check The Current Day And Enter Full Date Again")
            cd1 = int(input("Enter The Current Date:-"))
            d2 = (cd1 % 10000) - (cd1 % 100)
            d2 = d2 / 100
    elif y2 % 4 == 0 and m2 == 2:
        while d2 > 29:
            print("Please Check The Current Day And Enter Full Date Again")
            cd1 = int(input("Enter The Current Date:-"))
            d2 = (cd1 % 10000) - (cd1 % 100)
            d2 = d2 / 100
    elif y2 % 4 != 0 and m2 == 2:
        while d2 > 28:
            print("Please Check The Current Day And Enter Full Date Again")
            cd1 = int(input("Enter The Current Date:-"))
            d2 = (cd1 % 10000) - (cd1 % 100)
            d2 = d2 / 100

    while d1 > 31:
        print("Please Check The Birth Day And Enter Full Date Again")
        bd1 = int(input("Enter The Birth Date:-"))
        d1 = (bd1 % 10000) - (bd1 % 100)
        d1 = d1 / 100

if m1 == 4 or 6 or 9 or 11:
    if m2 == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        while d2 > 31:
            print("Please Check The Current Day And Enter Full Date Again")
            cd1 = int(input("Enter The Current Date:-"))
            d2 = (cd1 % 10000) - (cd1 % 100)
            d2 = d2 / 100
    elif m2 == 4 or 6 or 9 or 11:
        while d2 > 30:
            print("Please Check The Current Day And Enter Full Date Again")
            cd1 = int(input("Enter The Current Date:-"))
            d2 = (cd1 % 10000) - (cd1 % 100)
            d2 = d2 / 100
    elif y2 % 4 == 0 and m2 == 2:
        while d2 > 29:
            print("Please Check The Current Day And Enter Full Date Again")
            cd1 = int(input("Enter The Current Date:-"))
            d2 = (cd1 % 10000) - (cd1 % 100)
            d2 = d2 / 100
    elif y2 % 4 != 0 and m2 == 2:
        while d2 > 28:
            print("Please Check The Current Day And Enter Full Date Again")
            cd1 = int(input("Enter The Current Date:-"))
            d2 = (cd1 % 10000) - (cd1 % 100)
            d2 = d2 / 100

    while d1 > 30:
        print("Please Check The Birth Day And Enter Full Date Again")
        bd1 = int(input("Enter The Birth Date:-"))
        d1 = (bd1 % 10000) - (bd1 % 100)
        d1 = d1 / 100

if y1 % 4 == 0 and m2 == 2:
    if m2 == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        while d2 > 31:
            print("Please Check The Current Day And Enter Full Date Again")
            cd1 = int(input("Enter The Current Date:-"))
            d2 = (cd1 % 10000) - (cd1 % 100)
            d2 = d2 / 100
    elif m2 == 4 or 6 or 9 or 11:
        while d2 > 30:
            print("Please Check The Current Day And Enter Full Date Again")
            cd1 = int(input("Enter The Current Date:-"))
            d2 = (cd1 % 10000) - (cd1 % 100)
            d2 = d2 / 100
    elif y2 % 4 == 0 and m2 == 2:
        while d2 > 29:
            print("Please Check The Current Day And Enter Full Date Again")
            cd1 = int(input("Enter The Current Date:-"))
            d2 = (cd1 % 10000) - (cd1 % 100)
            d2 = d2 / 100
    elif y2 % 4 != 0 and m2 == 2:
        while d2 > 28:
            print("Please Check The Current Day And Enter Full Date Again")
            cd1 = int(input("Enter The Current Date:-"))
            d2 = (cd1 % 10000) - (cd1 % 100)
            d2 = d2 / 100

    while d1 > 29:
        print("Please Check The Current Day And Enter Full Date Again")
        bd1 = int(input("Enter The Birth Date:-"))
        d1 = (bd1 % 10000) - (bd1 % 100)
        d1 = d1 / 100

if y1 % 4 != 0 and m2 == 2:
    if m2 == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        while d2 > 31:
            print("Please Check The Current Day And Enter Full Date Again")
            cd1 = int(input("Enter The Current Date:-"))
            d2 = (cd1 % 10000) - (cd1 % 100)
            d2 = d2 / 100
    elif m2 == 4 or 6 or 9 or 11:
        while d2 > 30:
            print("Please Check The Current Day And Enter Full Date Again")
            cd1 = int(input("Enter The Current Date:-"))
            d2 = (cd1 % 10000) - (cd1 % 100)
            d2 = d2 / 100
    elif y2 % 4 == 0 and m2 == 2:
        while d2 > 29:
            print("Please Check The Current Day And Enter Full Date Again")
            cd1 = int(input("Enter The Current Date:-"))
            d2 = (cd1 % 10000) - (cd1 % 100)
            d2 = d2 / 100
    elif y2 % 4 != 0 and m2 == 2:
        while d2 > 28:
            print("Please Check The Current Day And Enter Full Date Again")
            cd1 = int(input("Enter The Current Date:-"))
            d2 = (cd1 % 10000) - (cd1 % 100)
            d2 = d2 / 100
    while d1 > 28:
        print("Please Check The Current Day And Enter Full Date Again")
        bd1 = int(input("Enter The Birth Date:-"))
        d1 = (bd1 % 10000) - (bd1 % 100)
        d1 = d1 / 100

ad = d2 - d1

if ad < 0:
    if m2 == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        ad += 31
    if m2 == 2 and y2 % 4 == 0:
        ad += 29
    if m2 == 2 and y2 % 4 != 0:
        ad += 28
    if m2 == 4 or 6 or 9 or 11:
        ad += 30
    m2 -= 1

am = m2 - m1
ay = y2 - y1

if am < 0:
    am += 12
    ay -= 1

if ay == 0:
    print("WISH YOUR BABY A LONG LIFE.")
    if ad == 0 and am != 0:
        if am == 1:
            print("Your Baby Is", am, " Month Old.")
        else:
            print("Your Baby Is", am, " Months Old.")
    elif ad != 0 and am == 0:
        if ad == 1:
            print("Your Baby Is", ad, " Day Old.")
        else:
            print("Your Baby Is", ad, " Day Old.")
    elif ad == 0 and am == 0:
        print("Your Baby Is Born Today.")
    else:
        print("Your Baby Is", ad, " Days, ", am, " Months Old.")
elif ay >= 1:
    if ad == 0 and am != 0:
        if am == 1 and ay != 1:
            print("You Are", am, " Month And", ay, " Years Old.")
        elif am != 1 and ay == 1:
            print("Your Baby Is", am, " Months And", ay, " Year Old.")
        else:
            print("You Are", am, " Months And", ay, " Years Old.")
    elif ad != 0 and am == 0:
        if ad == 1 and ay != 1:
            print("You Are", ad, " Day And", ay, " Years Old.")
        elif ad != 1 and ay == 1:
            print("Your Baby Is", ad, " Days And", ay, " Year Old.")
        else:
            print("You Are", ad, " Days And", ay, " Years Old.")
    elif ad == 0 and am == 0:
        if ay == 1:
            print("Your Baby Is", ay, " Year Old.")
        else:
            print("You Are", ay, " Years Old.")
    else:
        if ad == 1 and am == 1 and ay == 1:
            print("You Are", ad, " Day,", am, " Month And", ay, " Year Old.")
        elif ad == 1 and am == 1 and ay != 1:
            print("You Are", ad, " Day,", am, " Month And", ay, " Years Old.")
        elif ad == 1 and am != 1 and ay == 1:
            print("You Are", ad, " Day,", am, " Months And", ay, " Year Old.")
        elif ad == 1 and am != 1 and ay != 1:
            print("You Are", ad, " Day,", am, " Months And", ay, " Years Old.")
        elif ad != 1 and am == 1 and ay == 1:
            print("You Are", ad, " Days,", am, " Month And", ay, " Year Old.")
        elif ad != 1 and am == 1 and ay != 1:
            print("You Are", ad, " Days,", am, " Month And", ay, " Years Old.")
        elif ad != 1 and am != 1 and ay == 1:
            print("You Are", ad, " Days,", am, " Months And", ay, " Year Old.")
        elif ad != 1 and am != 1 and ay != 1:
            print("You Are", ad, " Days,", am, " Months And", ay, " Years Old.")

print("Thank You For Using This Program.")
choice = int(input("To Continue Press 1\nTo Exit Press 2 :-"))

while choice > 2:
    print("You Entered A Wrong Choice")
    choice = int(input("To Continue Press 1\nTo Exit Press 2 :-"))

while choice == 1:
    bd1 = int(input("Enter The Birth Date:-"))
    cd1 = int(input("Enter The Current Date:-"))
    bd2 = (bd1 % 100000000) - (bd1 % 10000)
    bd2 = bd2 / 10000
    cd2 = (cd1 % 100000000) - (cd1 % 10000)
    cd2 = cd2 / 10000
    y1 = (bd1 % 100000000) - (bd1 % 10000)
    y1 = y1 / 10000
    y2 = (cd1 % 100000000) - (cd1 % 10000)
    y2 = y2 / 10000
    m1 = bd1 % 100
    m2 = cd1 % 100
    d1 = (bd1 % 10000) - (bd1 % 100)
    d1 = d1 / 100
    d2 = (cd1 % 10000) - (cd1 % 100)
    d2 = d2 / 100

    while bd2 > cd2:
        print("Please Check The Years And Enter Full Date Again")
        bd1 = int(input("Enter The Birth Date:-"))
        cd1 = int(input("Enter The Current Date:-"))
        bd2 = (bd1 % 100000000) - (bd1 % 10000)
        bd2 = bd2 / 10000
        cd2 = (cd1 % 100000000) - (cd1 % 10000)
        cd2 = cd2 / 10000
    while m1 > 12:
        print("Please Check The Birth Month And Enter Full Date Again")
    while m2 > 12:
        print("Please Check The Current Month And Enter Full Date Again")
    if m1 == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        if m2 == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            while d2 > 31:
                print("Please Check The Current Day And Enter Full Date Again")
                cd1 = int(input("Enter The Current Date:-"))
                d2 = (cd1 % 10000) - (cd1 % 100)
                d2 = d2 / 100
        elif m2 == 4 or 6 or 9 or 11:
            while d2 > 30:
                print("Please Check The Current Day And Enter Full Date Again")
                cd1 = int(input("Enter The Current Date:-"))
                d2 = (cd1 % 10000) - (cd1 % 100)
                d2 = d2 / 100
        elif y2 % 4 == 0 and m2 == 2:
            while d2 > 29:
                print("Please Check The Current Day And Enter Full Date Again")
                cd1 = int(input("Enter The Current Date:-"))
                d2 = (cd1 % 10000) - (cd1 % 100)
                d2 = d2 / 100
        elif y2 % 4 != 0 and m2 == 2:
            while d2 > 28:
                print("Please Check The Current Day And Enter Full Date Again")
                cd1 = int(input("Enter The Current Date:-"))
                d2 = (cd1 % 10000) - (cd1 % 100)
                d2 = d2 / 100
        while d1 > 31:
            print("Please Check The Birth Day And Enter Full Date Again")
            bd1 = int(input("Enter The Birth Date:-"))
            d1 = (bd1 % 10000) - (bd1 % 100)
            d1 = d1 / 100
    if m1 == 4 or 6 or 9 or 11:
        if m2 == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            while d2 > 31:
                print("Please Check The Current Day And Enter Full Date Again")
                cd1 = int(input("Enter The Current Date:-"))
                d2 = (cd1 % 10000) - (cd1 % 100)
                d2 = d2 / 100
        elif m2 == 4 or 6 or 9 or 11:
            while d2 > 30:
                print("Please Check The Current Day And Enter Full Date Again")
                cd1 = int(input("Enter The Current Date:-"))
                d2 = (cd1 % 10000) - (cd1 % 100)
                d2 = d2 / 100
        elif y2 % 4 == 0 and m2 == 2:
            while d2 > 29:
                print("Please Check The Current Day And Enter Full Date Again")
                cd1 = int(input("Enter The Current Date:-"))
                d2 = (cd1 % 10000) - (cd1 % 100)
                d2 = d2 / 100
        elif y2 % 4 != 0 and m2 == 2:
            while d2 > 28:
                print("Please Check The Current Day And Enter Full Date Again")
                cd1 = int(input("Enter The Current Date:-"))
                d2 = (cd1 % 10000) - (cd1 % 100)
                d2 = d2 / 100
        while d1 > 30:
            print("Please Check The Birth Day And Enter Full Date Again")
            bd1 = int(input("Enter The Birth Date:-"))
            d1 = (bd1 % 10000) - (bd1 % 100)
            d1 = d1 / 100
    if y1 % 4 == 0 and m2 == 2:
        if m2 == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            while d2 > 31:
                print("Please Check The Current Day And Enter Full Date Again")
                cd1 = int(input("Enter The Current Date:-"))
                d2 = (cd1 % 10000) - (cd1 % 100)
                d2 = d2 / 100
        elif m2 == 4 or 6 or 9 or 11:
            while d2 > 30:
                print("Please Check The Current Day And Enter Full Date Again")
                cd1 = int(input("Enter The Current Date:-"))
                d2 = (cd1 % 10000) - (cd1 % 100)
                d2 = d2 / 100
        elif y2 % 4 == 0 and m2 == 2:
            while d2 > 29:
                print("Please Check The Current Day And Enter Full Date Again")
                cd1 = int(input("Enter The Current Date:-"))
                d2 = (cd1 % 10000) - (cd1 % 100)
                d2 = d2 / 100
        elif y2 % 4 != 0 and m2 == 2:
            while d2 > 28:
                print("Please Check The Current Day And Enter Full Date Again")
                cd1 = int(input("Enter The Current Date:-"))
                d2 = (cd1 % 10000) - (cd1 % 100)
                d2 = d2 / 100
        while d1 > 29:
            print("Please Check The Current Day And Enter Full Date Again")
            bd1 = int(input("Enter The Birth Date:-"))
            d1 = (bd1 % 10000) - (bd1 % 100)
            d1 = d1 / 100
    if y1 % 4 != 0 and m2 == 2:
        if m2 == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            while d2 > 31:
                print("Please Check The Current Day And Enter Full Date Again")
                cd1 = int(input("Enter The Current Date:-"))
                d2 = (cd1 % 10000) - (cd1 % 100)
                d2 = d2 / 100
        elif m2 == 4 or 6 or 9 or 11:
            while d2 > 30:
                print("Please Check The Current Day And Enter Full Date Again")
                cd1 = int(input("Enter The Current Date:-"))
                d2 = (cd1 % 10000) - (cd1 % 100)
                d2 = d2 / 100
        elif y2 % 4 == 0 and m2 == 2:
            while d2 > 29:
                print("Please Check The Current Day And Enter Full Date Again")
                cd1 = int(input("Enter The Current Date:-"))
                d2 = (cd1 % 10000) - (cd1 % 100)
                d2 = d2 / 100
        elif y2 % 4 != 0 and m2 == 2:
            while d2 > 28:
                print("Please Check The Current Day And Enter Full Date Again")
                cd1 = int(input("Enter The Current Date:-"))
                d2 = (cd1 % 10000) - (cd1 % 100)
                d2 = d2 / 100
        while d1 > 28:
            print("Please Check The Current Day And Enter Full Date Again")
            bd1 = int(input("Enter The Birth Date:-"))
            d1 = (bd1 % 10000) - (bd1 % 100)
            d1 = d1 / 100
    ad = d2 - d1
    if ad < 0:
        if m2 == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            ad += 31
        if m2 == 2 and y2 % 4 == 0:
            ad += 29
        if m2 == 2 and y2 % 4 != 0:
            ad += 28
        if m2 == 4 or 6 or 9 or 11:
            ad += 30
        m2 -= 1
    am = m2 - m1
    ay = y2 - y1
    if am < 0:
        am += 12
        ay -= 1
    if ay == 0:
        print("WISH YOUR BABY A LONG LIFE.")
        if ad == 0 and am != 0:
            if am == 1:
                print("Your Baby Is", am, " Month Old.")
            else:
                print("Your Baby Is", am, " Months Old.")
        elif ad != 0 and am == 0:
            if ad == 1:
                print("Your Baby Is", ad, " Day Old.")
            else:
                print("Your Baby Is", ad, " Day Old.")
        elif ad == 0 and am == 0:
            print("Your Baby Is Born Today.")
        else:
            print("Your Baby Is", ad, " Days, ", am, " Months Old.")
    elif ay >= 1:
        if ad == 0 and am != 0:
            if am == 1 and ay != 1:
                print("You Are", am, " Month And", ay, " Years Old.")
            elif am != 1 and ay == 1:
                print("Your Baby Is", am, " Months And", ay, " Year Old.")
            else:
                print("You Are", am, " Months And", ay, " Years Old.")
        elif ad != 0 and am == 0:
            if ad == 1 and ay != 1:
                print("You Are", ad, " Day And", ay, " Years Old.")
            elif ad != 1 and ay == 1:
                print("Your Baby Is", ad, " Days And", ay, " Year Old.")
            else:
                print("You Are", ad, " Days And", ay, " Years Old.")
        elif ad == 0 and am == 0:
            if ay == 1:
                print("Your Baby Is", ay, " Year Old.")
            else:
                print("You Are", ay, " Years Old.")
        else:
            if ad == 1 and am == 1 and ay == 1:
                print("You Are", ad, " Day,", am, " Month And", ay, " Year Old.")
            elif ad == 1 and am == 1 and ay != 1:
                print("You Are", ad, " Day,", am, " Month And", ay, " Years Old.")
            elif ad == 1 and am != 1 and ay == 1:
                print("You Are", ad, " Day,", am, " Months And", ay, " Year Old.")
            elif ad == 1 and am != 1 and ay != 1:
                print("You Are", ad, " Day,", am, " Months And", ay, " Years Old.")
            elif ad != 1 and am == 1 and ay == 1:
                print("You Are", ad, " Days,", am, " Month And", ay, " Year Old.")
            elif ad != 1 and am == 1 and ay != 1:
                print("You Are", ad, " Days,", am, " Month And", ay, " Years Old.")
            elif ad != 1 and am != 1 and ay == 1:
                print("You Are", ad, " Days,", am, " Months And", ay, " Year Old.")
            elif ad != 1 and am != 1 and ay != 1:
                print("You Are", ad, " Days,", am, " Months And", ay, " Years Old.")
    print("Thank You For Using This Program.")
    choice = int(input("To Continue Press 1\nTo Exit Press 2 :-"))
    while choice > 2:
        print("You Entered A Wrong Number")
        choice = int(input("To Continue Press 1 :-"))
