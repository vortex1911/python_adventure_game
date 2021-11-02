from fwrk import user_input


def open_seat_belt():
    print("You press the seatbelt unlock button but nothing happens. You try pulling but it doesnt budge")
    print("""What do you do?"
            1. Try to reach the glove compartment of your car
            2. Try to loosen the seatbelt of your car so that you can crawl out
                  """)

    answer = user_input()

    if answer == "1":
        print("""You try your best to reach the glove compartment. After a bit of struggle you are able to open it. 
        Inside you find a gun and a knife. You cut yourself """)

def search_pockets():
    print("TODO")


def start():
    print("""You open your eyes and realise you had an accident. You are inside a car which has fallen upside down, 
    probably from a huge cliff. Thankfully you're not hurt. """)

    print("""What do you do?
    1. Free yourself from your seatbelt.
    2. Search your pockets for any belongings.
    3. Look around your surroundings.

    --Enter the number corresponding to your input--
    """)

    answer = user_input()

    if answer == "1":
        open_seat_belt()
    elif answer == "2":
        search_pockets()
    else:
        print("""You look around the car. You are surrounded by the forest. In the distance you hear howling. You pray "
              that its not a pack of wolves""")
        print("""What do you do?
            1. Free yourself from your seatbelt""")

        answer = user_input()
        if answer == "1":
            open_seat_belt()
