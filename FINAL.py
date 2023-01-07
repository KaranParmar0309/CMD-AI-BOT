from ast import pattern
import webbrowser;
import re;
class Committees: 
    def askUser(self):
        x = input("\nPress 1 to Go back or Enter any other input to exit: ")
        if(x == "1"):
            return x
        else:
            print("\nThank you for visting!\n")
            quit()
            
    def nm_committee(self,comm):
        if(comm == 1):
            print("\nStudent's Council :")
            webbrowser.open("https://nmcollege.in/students-council")
            if(s.askUser() == "1"):        #calling to line 5
                s.comList()        #calling to line 574
            
        elif(comm == 2):
            print("\nCultural Committee :")
            webbrowser.open("https://nmcollege.in/cultural-society-2")
            if(s.askUser() == "1"):        #calling to line 5
                s.comList()        #calling to line 574
          
        elif(comm == 3):
            print("\nSports Committee :")
            webbrowser.open("https://nmcollege.in/gymkhana")
            webbrowser.open("https://nmcollege.in/demos/shop-demos/sport-shop")            
            print("Follow:  \n")
            if(s.askUser() == "1"):        #calling to line 5
                s.comList()        #calling to line 574
  
        elif(comm == 4):
            print("\nWomen Development Cell :")
            webbrowser.open("https://nmcollege.in/women-development-cell")
            print("Follow:   \n")
            if(s.askUser() == "1"):        #calling to line 5
                s.comList()        #calling to line 574

        elif(comm == 5):
            print("\nRotaract Club :")
            webbrowser.open("https://nmcollege.in/rotaract-club-of-nm")
            webbrowser.open("https://www.instagram.com/rc_nm/?hl=en")
            if(s.askUser() == "1"):        #calling to line 5
                s.comList()        #calling to line 574

        elif(comm == 6):
            s.giveOptions()        #calling to line 662
            
class courseInformation(Committees):
    def optionSelction(self):
        print('''        1. Syllabus.
        2. Faculty.
        3. Go Back
        ''')

        selectedOption = int(input("Please Enter number: "))
        try:
            if(selectedOption > 3 or selectedOption < 1):
                raise Exception
        except Exception:
            print("\nPlease Enter Valid Number within 1 and 3 only")
            return
        else:
            return selectedOption

    def firstBscIt(self):
        act = s.optionSelction()        #calling to line 282
        s.printLine()        #calling to line 475
        print("Bachelor of Science (Information Technlogy).")
        s.printLine()        #calling to line 475

        if(act == 1):
            print("First Year Syllabus: ")
            webbrowser.open("https://nmcollege.in/wp-content/uploads/2022/05/3.-Revised-Syllabus-FY-BSC-IT-Under-Autonomy.pdf")
            print("\nSecond Year Syllabus: ")
            webbrowser.open("https://nmcollege.in/wp-content/uploads/2021/06/3.-Syllabus-SY-BSC-IT-Under-Autonomy.pdf")
            print("\nThird Year Syllabus: ")
            webbrowser.open("https://nmcollege.in/wp-content/uploads/2022/05/3.3-Syllabus-TY-BSC-IT-Under-Autonomy-1.pdf")
            
            if(s.askUser() == "1"):        #calling to line 5
                s.secondCourse()        #calling to line 490

        elif(act == 2):
            print("Please Open below Link to see faculty member, you will be directed to collge official website!")
            webbrowser.open("https://nmcollege.in/bsc-it/")

            if(s.askUser() == "1"):        #calling to line 5
                s.secondCourse()        #calling to line 490

        elif(act == 3):
            s.secondCourse()        #calling to line 490

        else:
            print("Please Enter Valid Number between 1 and 3 only")
            s.firstBscIt()        #calling to line 298

            if(s.askUser() == "1"):        #calling to line 5
                s.optionSelction()        #calling to line 282
        
    def secondBMS(self):
        act = s.optionSelction()        #calling to line 282
        s.printLine()        #calling to line 475
        print("Bachelor of Mangement Studies.")
        s.printLine()        #calling to line 475

        if(act == 1):
            print("First Year Syllabus: ")
            webbrowser.open("https://nmcollege.in/wp-content/uploads/2021/06/FYBMS-SEM-I-SYLLABUS-1.pdf")
            print("\nSecond Year Syllabus: ")
            webbrowser.open("https://nmcollege.in/wp-content/uploads/2021/06/SYBMS-SEM-III-SYLLABUS-1.pdf")
            print("\nThird Year Syllabus: ")
            webbrowser.open("https://nmcollege.in/wp-content/uploads/2021/06/TYBMS-SEM-V-SYLLABUS-1.pdf")

            if(s.askUser() == "1"):        #calling to line 5
                s.secondCourse()         #calling to line 490 

        elif(act == 2):
            print("Please Open below Link to see faculty member, you will be directed to collge official website!")
            webbrowser.open("https://nmcollege.in/bachelor-of-management-studies/")

            if(s.askUser() == "1"):        #calling to line 5
                s.secondCourse()         #calling to line 490 
                 
        elif(act == 3):
            s.secondCourse()        #calling to line 490
 
        else:
            print("Please Enter Valid Number between 1 and 3 only")
            s.secondBMS()        #calling to line 332
            
            if(s.askUser() == "1"):        #calling to line 5
                s.optionSelction()        #calling to line 282  

    def thirdBMM(self):
        act = s.optionSelction()        #calling to line 282
        s.printLine()        #calling to line 475
        print("BAF (Bachelor of Accounting and Finance).")
        s.printLine()        #calling to line 475

        if(act == 1):
            print("Full Course Syllabus: ")
            webbrowser.open("https://nmcollege.in/wp-content/uploads/2022/06/FYBAF-Syllabus-AY-2022-23-.pdf")
            webbrowser.open("https://nmcollege.in/wp-content/uploads/2021/06/SYBAF-Syllabus-AY-2021-22.pdf")
            webbrowser.open("https://nmcollege.in/wp-content/uploads/2022/06/TYBAF-Revised-Syllabus-AY-2022-23-V2-1.pdf")

            if(s.askUser() == "1"):        #calling to line 5
                s.secondCourse()        #calling to line 490
                             
        elif(act == 2):
            print("Please Open below Link to see faculty member, you will be directed to collge official website!")
            webbrowser.open("https://nmcollege.in/baf/")
            
            if(s.askUser() == "1"):        #calling to line 5
                s.secondCourse()        #calling to line 490
                 
        elif(act == 3):
            s.secondCourse()        #calling to line 490

        else:
            print("Please Enter Valid Number between 1 and 3 only")
            s.thirdBMM()        #calling to line 366
            
            if(s.askUser() == "1"):        #calling to line 5
                s.optionSelction()         #calling to line 282 
    #BFM             
    def fourthMscIt(self):
        act = s.optionSelction()        #calling to line 282
        s.printLine()        #calling to line 475
        print("Bachelor of Financial Markets(BFM).")
        s.printLine()        #calling to line 475

        if(act == 1):
            print("First Year Syllabus: ")
            webbrowser.open("https://nmcollege.in/wp-content/uploads/2022/06/FYBFM-SYLLABUS-2022-23.pdf")
            print("\nSecond Year Syllabus: ")
            webbrowser.open("https://nmcollege.in/wp-content/uploads/2022/06/SYBFM-SYLLABUS-2022-23.pdf")
            print("\nThird Year Syllabus: ")
            webbrowser.open("https://nmcollege.in/wp-content/uploads/2022/06/TYBFM-SYLLABUS-2022-23.pdf")
            
 
            if(s.askUser() == "1"):        #calling to line 5
                s.secondCourse()         #calling to line 490
                            
        elif(act == 2):
            print("Please Open below Link to see faculty member, you will be directed to collge official website!")
            webbrowser.open("https://nmcollege.in/bfm")

            if(s.askUser() == "1"):        #calling to line 5
                s.secondCourse()         #calling to line 490
                 
        elif(act == 3):
            s.secondCourse()        #calling to line 490

        else:
            print("Please Enter Valid Number between 1 and 3 only")
            s.fourthMscIt()        #calling to line 396

            if(s.askUser() == "1"):        #calling to line 5
                s.optionSelction()        #calling to line 282  
    #BCOM             
    def fifthMA(self):
        act = s.optionSelction()        #calling to line 282
        s.printLine()        #calling to line 475
        print("Bachelor of Commerce(BCOM)")
        s.printLine()        #calling to line 475

        if(act == 1):
            print("Full Course Syllabus: ")
            webbrowser.open("https://nmcollege.in/bachelor-of-commerce")

            if(s.askUser() == "1"):        #calling to line 5
                s.secondCourse()        #calling to line 490

            if(s.askUser() == "1"):        #calling to line 5
                s.secondCourse()        #calling to line 490
                 
        elif(act == 3):
            s.secondCourse()        #calling to line 490
                          
        else:
            print("Please Enter Valid Number between 1 and 3 only")
            s.fifthMA()        #calling to line 428
        
            if(s.askUser() == "1"):        #calling to line 5
                s.optionSelction()         #calling to line 282 
                 
    def selectedOptionAction2(self, option):
        s.printLine()        #calling to line 475

        if(option == 1):
            s.firstBscIt()        #calling to line 298
        elif(option == 2):
            s.secondBMS()        #calling to line 332
        elif(option == 3):
            s.thirdBMM()        #calling to line 366
        elif(option == 4):
            s.fourthMscIt()        #calling to line 396
        elif(option == 5):
            s.fifthMA()        #calling to line 428
        else:
            s.giveOptions()        #calling to line 662
            
class chatbotFunction(courseInformation):
    def printLine(self):
        print("---------------------------------------------------------")

    def firstAboutnm(self):
        s.printLine()        #calling to line 475
        print("About College")
        s.printLine()        #calling to line 475

        print("\nNarsee Monjee College of Commerce & Economics is a leading college affiliated to Mumbai University, is a college in Vile Parle, Mumbai, India. \nNM College is a branch of the SVKM Group Shri Vile Parle Kelavani Mandal.")
        print("\nThe College was established by Shri Vile Parle Kelavani Mandal in 1964.\nSince its inception in 2003, Narsee Monjee College has introduced many courses. \nThe college has introduced un-aided courses like, \n\n1) Bachelors in Management Studies (BMS), \n2) Bachelor of Science (Information Technlogy) (BSc.IT), \n3) Bachelor of Accounting and Finance (BAF) and \n4)  Bachelor of Financial Markets (BFM). \n5) Bachelor of Commerce(BCOM)).")
        webbrowser.open("https://nmcollege.in")
        
        if(s.askUser() == "1"):        #calling to line 5
            s.giveOptions()        #calling to line 662
            
    def secondCourse(self):
        s.printLine()        #calling to line 475
        print("With which course I can help you?")
        print('''        1. Bachelor of Science (Information Technlogy).
        2. Bachelor of Mangement Studies.
        3. BAF (Bachelor of Accounting and Finance).
        4. BFM (Bachelor of Financial Markets).
        5. BCOM (Bachelor of Commerce).
        6. Go Back
        ''')

        action2 = int(input("Please select one of the option: "))
        try:
            if(action2 > 6 or action2 < 1):
                raise Exception
        except Exception:
            print("\nPlease Enter Valid Number within 1 and 6 only")
            s.secondCourse()        #Recalling Itself (line 487)
        else:
            s.selectedOptionAction2(action2)        #calling to line 455

    def thirdAdmission(self):
        s.printLine()        #calling to line 475
        print("New Admission Details")
        s.printLine()        #calling to line 475
        print("\nPlease Open below Link, you will be directed to collge official website!\nYou will find all the necessary details about admission eligibilty, process and fee structure.")
        webbrowser.open("https://nmcollege.in/admission-procedure/#:~:text=The%20student%20will%20have%20to%20fill%20the%20form%20online.,form%20and%20follow%20the%20procedure.")

        if(s.askUser() == "1"):        #calling to line 5
            s.giveOptions()        #calling to line 662

    def fourthNoticeBoard(self):
        s.printLine()        #calling to line 475
        print("Notice Board")
        s.printLine()        #calling to line 475
        print("\nPlease Open below Link, you will be directed to collge official website!")
        webbrowser.open("https://nmcollege.in/nm-home")
        print("\nYou will find all the necessary details from this notice board.")

        if(s.askUser() == "1"):        #calling to line 5
            s.giveOptions()        #calling to line 662

    def fifthContactUs(self):
        s.printLine()        #calling to line 475
        print("Contact Us")
        s.printLine()        #calling to line 475

        e = int(input("Press 1 to fill Enquiry Form or \nPress 2 for College Contact Details: "))
        if(e == 1):
            s.printLine()        #calling to line 475
            print("Conatct Us Form")
            s.printLine()        #calling to line 475
            name=input("Enter your name: ")
            num='[6-9][0-9]{9}'
            phoneNumber=input("Enter your phone number: ")
            if re.search(num,phoneNumber):
                print('valid number');
            else:
                print('Enter valid number');
            pattern='^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
            emailId=input("Enter your Email Id: ")
            if re.search(pattern,emailId):
                print('valid Email ID');
            else:
                print('Enter valid Email ID');
            q=input("What is your query?\n")

            fp = open("C:\\Users\\karan\\Desktop\\New folder\\ContactUsForm.txt", "a")
            fp.write("\n\nName: "+ name)
            fp.write("\nPhone number: "+ phoneNumber)
            fp.write("\nEmail Id: "+ emailId)
            fp.write("\nQuery: "+ q)
            fp.close()

            print("\nThank you for your interest!\nCollege will contact you as soon as possible!")

            if(s.askUser() == "1"):        #calling to line 5
                s.giveOptions()        #calling to line 662

        elif(e == 2):
            print("\nShri Vile Parle Kelavani Mandal's\nNarsee Monjee College of Commerce and Economics,\nSwami Bhakti Vedanta Swami Marg,\nBhagubai Mafatlal Complex,Opp.Cooper Hospital Vile Parle (West),\nMumbai 400 056.\nMaharashtra, India")
            print("\nContact No:  022 42338000 / 022 42338001")
            print("\nEmail Id: nmcollege@nmcce.ac.in ")
            
            if(s.askUser() == "1"):        #calling to line 5
                s.giveOptions()        #calling to line 662
        
        else:
            print("Please Enter Valid Input")
            s.fifthContactUs();        #calling to line 534

    def comList(self):
        s.printLine()
        print("Committees")
        s.printLine()
        print('''        1. Student's Council
        2. Cultural Committee
        3. Sports Committee
        4. Women Development Cell
        5. Rotaract Club
        6. Go back  
        ''') 
    
        enter1 = int(input("Please select one of the option: "))
        try:
            if(enter1>14 or enter1<1):        #calling to line 5
                raise Exception
        except Exception:
            print("Enter a valid number between 1 to 14 only")
            s.comList()         #Recalling itself (line 571)
        else:
            s.nm_committee(enter1)         #calling to line 13

    def fullExit(self):
        print("\nThank you for visting!")
        quit()

    def selectedOptionAction1(self, option):
        if(option == 1):
            s.firstAboutnm()        #calling to line 478
        elif(option == 2):
            s.secondCourse()         #calling to line 490
        elif(option == 3):
            s.thirdAdmission()       #calling to line 511
        elif(option == 4):
            s.fourthNoticeBoard()    #calling to line 523
        elif(option == 5):
            s.fifthContactUs()       #calling to line 534
        elif(option == 6):
            s.comList()              #calling to line 574
        elif(option == 7):
            s.fullExit()             #calling to line 631

#Chatbot will start from here
class startChatbot(chatbotFunction):
    def startBot(self):
        print("\n")
        s.printLine()                 #calling to line 475
        print("Welcome to SVKM's Narsee Monjee College of Mangement\n\nI am Skyra, your assistant.")
        s.printLine()                 #calling to line 475
        s.giveOptions()               #calling to line 662

    def giveOptions(self):
        print("\nHow can I help you?:")
        print('''        1. About College
        2. Courses
        3. New Admission Details.
        4. Notice Board.
        5. Contact us.
        6. Committee.
        7. Exit.
        ''')
        
        action1 = int(input("Please select one of the option: "))
        try:
            if(action1 > 7 or action1 < 1):
                raise Exception
        except Exception:
            print("\nPlease Enter Valid Number within 1 and 8 only")
            s.giveOptions()                 #Recalling itself for valid number  (line 662)
        else:
            s.selectedOptionAction1(action1)        #calling to line 635

s = startChatbot()         #Creating object of class startChatbot()
s.startBot()           #Triggering the event
## ------Group Members------
##  
##  45207200031  - Karan Parmar
##  45207200020  - Harsh Poyekar
##  45207200047  - Shruti Tawde
##  45207200007  - Dimple Trivedi