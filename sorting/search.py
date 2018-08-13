import sys

def search():
    search_string=raw_input("Enter the number to search(R to Leave the Program)")
    if search_string.upper()=="R":
        menu()
    else:
        search_int=int(search_string)
        if search_int in alist:
            print "{0} Number found ".format(search_int)
        else:
            print "{0} Number not found ".format(search_int)

def menu():
    to_start = raw_input(" (Q)Search For Numbers or (E)Leave Program :")
    if to_start.upper()=="E":
        print "Exiting the program you entered {0} :=".format(search_string)
        sys.exit(1)
    elif to_start.upper()=="Q":
        search()
    else:
      print ("Invalid Input")

def valid(number):
    if str(number).isdigit():
        return True
    else:
        return False

def get_total_number():
    total_numbers = int(raw_input("Enter number of variables wanted in list:"))
    if total_numbers > 0:
        return total_numbers
    else:
        print ("invalid")
        get_total_number()

if __name__=="__main__":
    total_numbers = get_total_number()
    alist = []
    for index in range(total_numbers):
            while True:
                enter_number = raw_input("Choose a number for your list [{0}]".format(index))
                if valid(enter_number):
                    alist.append(int(enter_number))
                    break
                else:
                    print("its not valid,enter again")

    while True :
        search_string=raw_input("Enter the number to search(R to Go To Menu)")
        if search_string.upper()=="R":
            menu()
        else:
            try:
                search_int=int(search_string)
                if search_int in alist:
                    print "{0} Number found ".format(search_int)   
                elif search_int not in alist:
                    print "{0} Number not found ".format(search_int)
            except (ValueError):
                print ("invalid input")

