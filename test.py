# msg = input("entrer votre messages \n")
# for letter in msg:
#     print(letter)
def test ():
    message = {1:"test",2:"test2"}
    for items in message.items():
        for truc in items:
            print(truc)
def fonction_test ():
    pass


def main ():
    while True:
        range_size = int(input("\nEnter un nombre\n"))
        new_list = [x for x in range(range_size) if x%3==0]
        print (new_list)




if __name__=="__main__":
    main()