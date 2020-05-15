class Health:

    import datetime
    timing=(datetime.datetime.now())

    def name(self):
        print("1-harsh")
        print("2-ayshi")
        print("3-ronaldo")
        print("4-back")

        choice2=input("chose a name")

        if (choice2=="1"):
            harsh.work("harsh")

        elif(choice2=="2"):
            harsh.work("ayushi")

        elif(choice2=="3"):
            harsh.work("ronaldo")

        elif(choice2=="4"):
            pass

        else:
            print("Not a valid option...plz select a valid option")


    def work(self,aname):
        print("select option")
        print("1-exercise")
        print("2-diet")
        print("3-back")

        choice4=input()

        if(choice4=="1"):
            harsh.ex(aname)

        elif(choice4=="2"):
            harsh.diet(aname)

        elif(choice4=="3"):
            harsh.name()

        else:
            print("type a valid key")



    def ex(self,aname):
        if choice1=="1":

            print(f"enter the name of exercise {aname}")
            ex_name=input()
            f=open(aname+"ex.txt","a")
            f.write(f"exercise-> {ex_name} -{self.timing}\n" )
            f.close()
            print("..Exercise is successfully added...\n")

        elif choice1=="2":

            try:
                print("this is ur data of exercise\n")
                f = open(aname+"ex.txt", "r")
                b = f.read()
                print(b)
                f.close()

            except:
                print("not any information found\n")


    def diet(self,aname):

        if choice1 == "1":
            dname = input("name of meal")
            f = open(aname+"diet.txt", "a")
            f.write(f"diet name-> {dname} -{self.timing}\n  ")
            f.close()
            print("your meel is successfully added")

        elif choice1 == "2":

            try:
                print("this is data of meel\n")
                f = open(aname+"diet.txt", "r")
                b = f.read()
                print(b)
                f.close()

            except:
                print("not any information found\n")


harsh = Health()


while(True):
    print("welcome")
    print(".....Be healthy , Be fit..................")
    print("1-enter data")
    print("2-check data")
    print("q to quite..")

    choice = input("\nenter your choice_____")
    choice1=choice.capitalize()

    if choice1=="1":
        harsh.name()

    elif choice1=="2":
        harsh.name()

    elif choice1=="Q":
        exit()

    else:
        print("plz....choose a valid option")








