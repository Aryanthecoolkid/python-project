import sys



#if __name__ == "__main__":
#    print ("heelo")

#Enter no of numbers : 10 X
#Enter number 1: 34 
#Enter number 2: 45 
#....
#Enter number to search (type Q to quit)
total_no=int(raw_input("Enter no of number to store:"))
#make a list with size of total number
my_list = []
if total_no > 0:
    for i in  range(total_no):
        my_list.append(int(raw_input("Enter number [{0}] : ".format(i))))
else:
    print("number should be greater than 0")
    sys.exit(1)
#where we have collected my_list
while 1==1 :
    search_string=raw_input("Enter the number to search(Q to exit)")
    if search_string.upper()=="Q":
        print "Exiting the program you entered {0} :=".format(search_string)
        break
    else:
        search_int=int(search_string)
        if search_int in my_list:
            print "{0} Number found ".format(search_int)
        else:
            print "{0} Number not found ".format(search_int)