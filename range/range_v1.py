def rounds():
    global num, total
    while True:
                        try:
                         
                                    num = int(input("\nPlease enter the number of questions you would like to answer between 1-10: "))
                                    print("continues to quiz")
                                    break
                        except:
                                    print("\n=========================\nPlease enter numbers only\n=========================")
                                    total = num
rounds()
