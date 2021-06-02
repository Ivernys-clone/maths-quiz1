import random
def rounds():
            global num, total
            while True:
                        try:
                         
                                    num = int(input("\nPlease enter the number of questions you would like to answer between 1-10: "))
                                    if 0<num<=10:
                                        print("continues to quiz")
                                        break
                                    else:
                                                print("\n==============================\nPlease enter numbers 1-10 only\n==============================")
                        except:
                                    
                                    print("\n=========================\nPlease Enter Only Numbers\n=========================")
                                   

            total = num
rounds()
