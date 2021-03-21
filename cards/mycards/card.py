import time
import card_shuffle

cards = card_shuffle.Deck()


def start():
    print("Welcome To Random Generator\n\n")
    rounds = int(
        input("Please enter the amount of time you would wish run the shuffle: \n"))
    if rounds < 1:
        print("number can't be less than 1\n")
        quit()
    elif rounds > 10000:
        print("number can't be gerater than 10,000\n")
        quit()


    print("Enter the type of generator you wish to run\n")
    print("Enter 1 for Js random shuffle\n")
    print("Enter 2 for XorShift shuffle\n")
    choice = int(input("Please enter your choice here: "))
    print("\n--------------------------starting generator------------------------------------n")

    if choice == 1:
        start_time = time.time_ns()
        for i in range(rounds ):
            print(cards.shuffle())
        end_time = time.time_ns()
        total = (start_time + end_time)
        performance_interval = (end_time - start_time)

        print("\nstart time {} nanoseconds".format(start_time))
        print("Code ended time is {} nanoseconds".format(end_time))
        print("total time code ran for {} nanoseconds".format(total))
        print("performance_interval time code ran for {} nanoseconds".format(
            performance_interval))

    elif choice == 2:
        pass

    elif choice == 3:
        pass
    else:
        pass


start()
