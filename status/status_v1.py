while True:
    shutdown = input("\nDo you wish to play this quiz?  \na)Yes\nb)no\nEnter here:")
    if shutdown == "YES" or shutdown == "Y" or shutdown == "A" or shutdown == "":
        print("Continues to quiz")
      break
    else:
        print("\nThank you please play the quiz again")
        exit()
