

print('''                  ✦•················•»——————⋆◦★◦⋆——————«•··················•✦
                         »»-----------<:~ 『CURAXIN』 ~:>-----------««
                                   ❈────────•✦•❅•✦•───────❈             ''')






import random
import re
import mysql.connector
import datetime
con=mysql.connector.connect(host="localhost",
                            user="root",
                            password="12345",
                            database='sam')
cur=con.cursor()
flag=0
MNAME="KIM-JONG-UN"
while flag<=0:
    A=int(input("\nPRESS 1 TO LOG IN TO YOUR ACCOUNT \
             \nPRESS 2 TO JOIN US TODAY\
             \nPRESS 3 TO LOG IN AS ADMIN\n"))
    if A==1:
        D=input("ENTER YOUR E-MAIL ID: ")
        query="select USERNAME from PERSONAL_PROFILE where EMAIL = '%s'"%(D)
        cur.execute(query)
        data=cur.fetchall()
        if data == [] :
            print("Incorrect Email_ID\
                \nJOIN NOW SIGN UP WITH US TODAY:)")
            flag-=1
        else:
            print("Correct Email_ID :)")
            UPAS=input("ENTER YOUR PASSWORD: ")
            PASS="select PASSWORD from PERSONAL_PROFILE where EMAIL = '%s'"%(D)
            cur.execute(PASS)
            Data=cur.fetchall()
            for i in Data:
                def convert(i):
                    t= ''.join(i)
                    return t
            UPASS=convert(i)
            if UPASS!= str(UPAS):
                print("Incorrect Password\
                \nJOIN NOW SIGN UP WITH US TODAY:)")
                flag-=1
            else:
                flag+=1
                print("Correct Password:)")
                for i in data:
                    def convert(i):
                        t= ''.join(i)
                        return t
                s = convert(i)
                S = s
                print (S,"Welcome to CURAXIN")
    elif A==2:
         p=0
         R=int(random.randrange(9999999))
         print(R)
         RR=R
         while p>=0:
             N=input("ENTER YOUR NAME:- ")
             if str(N) == str(MNAME):
                 p+=1
                 print("LOGIN USING ADMIN PORTAL Mr.KIM-JONG-UN")
                 break
             else:
                 print("VALID USERNAME")
                 p-=1
             PN=int(input("ENTER YOUR Phone no.:-"))
             if len(str(PN))!=8:
                 print("Invalid Phone number")
                 p+=0
             else:
                 EA=input("ENTER YOUR Email Address:-")
                 SEA= ( r'\b[a-z0-9._%+-]+@[a-z0-9]+\.[a-z]{2,}\b')
                 def check(EA):
                     if (re.fullmatch(SEA,EA)):
                         print("Valid Email ID")
                         PW=input("ENTER YOUR NEW PASSWORD(\nONLY 8 CHARACTER\
                                          \nAt least 1 number or digit between [0-9]\
                                          \nAt least 1 character from [ _ or @ or $ or &]")
                         password = PW
                         if(len(password)<8)and\
                             not re.search("[0-9]", password) and\
                             not re.search("[_@$&]", password) and\
                             not re.search("\s", password):
                             p+=0
                             print("Not a Valid Password")
                         else:
                             print("Valid Password")
                             CYP=input("JOIN US NOW WITH(ENTER Rs AND THE PRICE ONLY)\
                                      \nJOIN CURAXIN FOR 1 MONTH AT Rs399\-\
                                      \nJOIN CURAXIN FOR 2 MONTH AT Rs799\-\
                                      \nJOIN CURAXIN FOR 3 MONTH AT Rs999\-\
                                      \nJOIN CURAXIN FOR 6 MONTH AT Rs1550\-\
                                      \nJOIN CURAXIN FOR ANNUAL MEMBERSHIP AT Rs2749\-")
                             query=("Insert into Personal_Profile values({},'{}',{},'{}','{}','{}')".format(N,PW,PN,EA,'Milan',CYP))
                             cur.execute(query)
                             con.commit()
                             print(N,"Welcome to CURAXIN")
                     else:
                         print("Invalid Email ID")
                 check(EA)
    elif A==3:
        ANAME=input("Enter your name:")
        if str(ANAME) != str(MNAME):
            print ("INCORRECT USERNAME")
            flag-=1
            break
        else:
            AEMAIL=input("ENTER YOUR EMAIL ADDRESS")
            ADEMAIL="select EMAIL from PERSONAL_PROFILE where USERNAME = '%s'"%(ANAME)
            cur.execute(ADEMAIL)
            DaTa=cur.fetchall()
            print(DaTa)
            for i in DaTa:
                def convert(i):
                    t= ''.join(i)
                    return t
                ADMAIL = convert(i)
                print(ADMAIL)
                    
            if AEMAIL !=str(ADMAIL) :
                print("Incorrect Email_ID")
                flag-=1
                break
            else:
                print("Correct Email_ID")
                ADPASS=input("ENTER YOUR PASSWORD--")
                ADPAS="select PASSWORD from PERSONAL_PROFILE where EMAIL = '%s'"%(AEMAIL)
                cur.execute(ADPAS)
                dAtA=cur.fetchall()
                for i in dAtA:
                    def convert(i):
                        t= ''.join(i)
                        return t
                    SS = convert(i)
                if SS != str(ADPASS):
                    print("Inorrect Password")
                    flag-=1
                    break
                else:
                    flag+=1
                    print("Correct Password")
                    print (MNAME,"Welcome to CURAXIN")



                    k=0
                    while k<=0:
                        Y=int(input("CHOOSE THE FOLLOWING OPTIONS:\
                                    \nADD DRUGS= 1  REMOVE DRUGS= 2\
                                    \nVEIW ALL = 3  REMOVE USER PROFILE= 4\n"))
                        if Y==1:
                            MedID=random.randrange(999999)
                            MN=input("ENTER MEDICINE NAME:")
                            MID=input("ENTER THE MEDICINE ID:")
                            DM=input("DESC OF MEDICINE:")
                            TM=input("ENTER THE TYPE OF MEDICINE:")
                            MD=float(input("ENTER THE MANUFACTURER OF THE DRUGS:"))

                            PQ=str(datetime.date(YR,MR,DR))
                            AM="insert into MEDICINE values({},'{}','{}','{}','{}',{},'{}',{})".format(MedIDID,MN,MID,DM,TM,MD,PQ,AM)
                            cur.execute(AM)
                            con.commit()
                            print("MEDICINE ADDED SUCCESSFULLY :)")
                            k+=0
                        elif Y==2:
                            MN=input("ENTER MEDICINE WHICH YOU WANT TO REMOVE:")
                            DM="delete FROM movies where movies name ={}".format(MN)
                            cur.execute(DM)
                            print("MEDICINE REMOVED SUCCESSFULLY :)")
                        elif Y==3:
                            VU="select * from profile"
                            cur.execute(VU)
                            OP=cur.fetchmany()
                            print(OP)
                        elif Y==4:
                            UID=input("ENTER USER ID")
                            RU="delete from profiles where User_ID={}".format(UID)
                            cur.execute(RU)
                        
    else:
        print("CHOOSE AN OPTION")
        flag-=1


f=0
while f<=0:
    x=int(input("\nEnter number to choose the options\
                 \nOur Partner Manufacturers=1\
                 \nMedicine Type=2\
                 \nView Your Profile=3\
                 \nSearch by Medicine name=4\
                 \nSearch by Med ID=5\n"))

    if x==1:
           C=input("Alkem, Apollo, Astellas, Abbott\
                   \nAmgen, AstraZeneca, Aventis, Biocon\
                   \nBiogen,Bristol-Myers Squibb, Cadila,,Cipla\
                   \nDivi's Lab, Dr.Reddy's, Eli Lilly, GlaxoSmithKline\
                   \nJohnson and Johnson, Novo Nordisk, Novartis, Pfizer\
                   \nPiramal, Roche, Schering-Plough, Sinopharm\
                   \nSun Pharma,Takeda, Teva, Torrent\n")
           SC="select * from Inventory where MANUFACTURER = '{}'".format(C)
           cur.execute(SC)
           SBC=cur.fetchall()
           for BC in SBC:
               print(BC)

    elif x==2:
        R=input(" | Ayurveda | Capsule | Drops | Drugs |\
             \n | Homoeopathy | Inhalers | Injections | Liquid |\
             \n | Patches | Suppositories | Tablet |")
        SC="select * from Inventory where MED_TYPE = '{}'".format(R)
        cur.execute(SC)
        SBC=cur.fetchall()
        for BC in SBC:
            print(BC)

    elif x==3:
        q=0
        while q>=0:
            PRO=int(input("1--EDIT USER DATA\
                         \n2--VIEW  USER PROFILE"))
            if PRO==1:
                UpdatePROF=int(input("What would you like to change: 1--NAME\
                                                                     \n2--PHONENUMBER\
                                                                     \n3--EMAIL\
                                                                     \n4--PASSWORD\
                                                                     \n5--Membership\n"))
                if UpdatePROF==1:
                    CNAME=input("ENTER YOUR CURRENT NAME:")
                    NNAME=input("ENTER YOUR NEW NAME:")
                    PROF="update PERSONAL_PROFILE set USERNAME='{}'where USERNAME='{}'".format(NNAME,CNAME)
                    cur.execute(PROF)
                    con.commit()
                    print("NAME UPDATED")
                elif UpdatePROF==2:
                    CPN=input("ENTER YOUR CURRENT PHONENUMBER:")
                    NPN=input("ENTER YOUR NEW PHONENUMBER:")
                    if len(str(PN))!=10:
                        print("Invalid Phone number")
                        q+=0
                    else:
                        q-=0
                        print("Valid Phone number")
                        PHONE="update PERSONAL_PROFILE set PHONE_NUMB={}where PHONE_NUMB={}".format(NPN,CPN)
                        cur.execute(PHONE)
                        con.commit()
                        print("PHONENUMBER UPDATED")
                elif UpdatePROF==3:
                    CEA=input("ENTER YOUR CURRENT EMAIL ADDRESS:")
                    NEA=input("ENTER YOUR NEW EMAIL ADDRESS:")
                    def check(NEA):
                        SEA= (r'\b[a-z0-9._%+-]+@[a-z0-9]+\.[a-z]{2,}\b')
                        if (re.fullmatch(SEA,NEA)):
                            print("Valid Email ID")
                            q-=0
                            EADD="update PERSONAL_PROFILE set  EMAIL={}where  EMAIL={}".format(NEA,CEA)
                            cur.execute(EADD)
                            con.commit()
                            print("EMAIL ADDRESS UPDATED")
                        else:
                            print("Invalid Email ID")
                            q+=0
                    check(NEA)    
                    
                elif UpdatePROF==4:
                    CPASS=input("ENTER YOUR CURRENT PASSWORD:")
                    EPASS=input("ENTER YOUR NEW PASSWORD(\nONLY 8 CHARACTER\
                                          \nAt least 1 number or digit between [0-9]\
                                          \nAt least 1 character from [ _ or @ or $ or &]:- ")
                    if(len(EPASS)<8)and\
                        not re.search("[0-9]", EPASS) and\
                        not re.search("[_@$&]", EPASS) and\
                        not re.search("\s", EPASS):
                        q+=0
                        print("Not a Valid Password")
                    else:
                        q-=0
                        print("Valid Password")
                    PAS="update PERSONAL_PROFILE set PASSWORD='{}'where PASSWORD='{}'".format(NPASS,CPASS)
                    cur.execute(PAS)
                    con.commit()
                    print("PASSWORD UPDATED")
                elif UpdatePROF==5:
                    q-=0
                    CP=input("ENTER YOUR PLAN NAME:")
                    NP=input("CHOOSE YOUR PLAN(ENTER Rs AND THE PRICE ONLY)\
                                      \nJOIN CURAXIN FOR 1 MONTH AT Rs399\-\
                                      \nJOIN CURAXIN FOR 2 MONTH AT Rs799\-\
                                      \nJOIN CURAXIN FOR 3 MONTH AT Rs999\-\
                                      \nJOIN CURAXIN FOR 6 MONTH AT Rs1550\-\
                                      \nJOIN CURAXIN FOR ANNUAL MEMBERSHIP AT Rs2749\-")
                    PLAN="update PERSONAL_PROFILE YourPlan='{}'where YourPlan='{}'".format(NP,CP)
                    cur.execute(PLAN)
                    con.commit()
                    print("PLAN UPDATED")
                else:
                    print("CHOOSE AN OPTION")
            elif PRO==2:
                q-=0
                if A==1:
                    q-=0
                    PROF="select * from PERSONAL_PROFILE where USERNAME = '%s'"%(S)
                    cur.execute(PROF)
                    PROFILE=cur.fetchall()
                    for i in PROFILE:
                        print(i)
                        
                elif A==2:
                    q-=0
                    PROF="select * from PERSONAL_PROFILE where USERNAME = '%s'"%(N)
                    cur.execute(PROF)
                    PROFILE=cur.fetchall()
                    for i in PROFILE:
                        print(i)

            elif PRO==3:
                 f+=0
                 
            else:
                q+=0
                print("CHOOSE AN OPTION")
                    
 
    elif x==4:
        search=input("Search a MEDICINE")
        FE=(search+"%")
        F=("select * from inventory where MED_NAME LIKE '{}'".format(FE))
        cur.execute(F)
        FU=cur.fetchall()
        for FUu in FU :
            print(FUu)
        
        
    elif x==5:
        search=input("Search MEDICINE_id")
        FE=(search+"%")
        F=("select * from inventory where MED_ID LIKE '{}'".format(FE))
        cur.execute(F)
        FU=cur.fetchall()
        for FUu in FU :
            print(FUu)
   
