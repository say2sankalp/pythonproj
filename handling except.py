while True:
    try:
        x=int(raw_input("Please enter a number :"))
        break
    except Valueerr:
        print "Oops! that was no valid number. Try again.."
