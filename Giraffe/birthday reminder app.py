dict={}
while True:
    print("--------Birthday App-------")
    print("1.Show birthday")
    print("2.Add to birthday list")
    print("3.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        if len(dict.keys())==0:
            print("Nothing to show")
        else:
            name=input("Enter a name to show birthday")
            birthday=dict.get(name,"No data found")
            print(birthday)

    elif choice==2:
        name=input("enter friend's name:")
        date=input("Enter birthdate:")
        dict[name]=date
        print("birthday added")

    elif choice==3:
        break

    else:
        print("choose a valid option")
