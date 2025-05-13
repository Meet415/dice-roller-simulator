import random
import time

ans_list = []


def roller():
    count  = 0
    ans = 0
    while True:

        boolq = input("Do you want to roll dice (Y/N) :: ").lower()

        if boolq == 'n':
            msg1= "You have rolled dice " + str(count) + " times"
            msg2= "exiting....."
            for i in msg1:
                print(i,end = "" , flush=True)
                time.sleep(0.05)                
            print("")
            for i in msg2:
                print(i,end = "" , flush=True)
                time.sleep(0.05)                
            print("")
            break

        elif boolq == 'y':
            choice2 = int(input("How many times you want to roll the dice?? :: "))
            while choice2 > 0:
                    ans = random.randint(1,6)
                    ans_list.append(ans)
                    choice2 -= 1
            ans = tuple(ans_list)
            print(ans)
            count+=1
        else:
            print("Invalid input.")


def main():

    roller()
if __name__ == "__main__":
    main()  
