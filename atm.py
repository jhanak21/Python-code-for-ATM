import random

for i in range (0,999999999):
     print("\n welcom to atm\n")
     op=int(input("1 for existing user\n 2 to create acc\n"))
     if op==1 :
         fp=open("atmdata.txt",'r')
         cd=input("enter card no\n")
         cd=str(cd)
         cd=cd+"\n"
         pn=input("enter four digit pin no\n")
         pn=str(pn)
         pn=pn+"\n"
         l1=fp.readlines()
         i=len(l1)/4
         j=0
         fp.close()
         while (i):
             #print(l1[j])
             if (l1[j])==cd:
                 if (l1[j+1]==pn):
                      j=j-1
                      print("successful")
                      fp=open("atmdata.txt",'r')
                      lines=fp.readlines()
                      print("name ",lines[j+3])
                      print("balance ",lines[j+4])
                      #j=j-4
                      fp.close()
                      opt=int(input(" 1 to deposit\n 2 to withdraw\n 3 to change pin\n"))   
                      if opt==1:
                          fp=open("atmdata.txt",'r')
                          lines=fp.readlines()
                          bal=(lines[j+4])
                          print("current balance ",bal)
                          bal=(int(bal))
                          bal1=int(input("enter amount\n"))
                          bal=bal1+bal
                          bal=(str(bal))
                          print("final balance ",bal)
                          lines[j+4]=bal+"\n"
                          fp=open("atmdata.txt",'w')
                          fp.writelines(lines)
                          fp.close()
                          print("thank you \n")
                          
                          
                      if opt==2:
                          fp=open("atmdata.txt",'r')
                          lines=fp.readlines()
                          bal=(lines[j+4])
                          print("current balance ",bal)
                          bal=(int(bal))
                          bal1=int(input("enter amount\n"))
                          bal=bal-bal1
                          bal=(str(bal))
                          print("final balance ", bal)
                          lines[j+4]=bal+"\n"
                          fp=open("atmdata.txt",'w')
                          fp.writelines(lines)
                          fp.close()
                          print("thank you \n")
                          
                      if opt==3:
                          fp=open("atmdata.txt",'r')
                          lines=fp.readlines()
                          pin=(lines[j+2])
                          print("current pin ",pin)
                          pin=(int(pin))
                          pin1=int(input("enter new pin\n"))
                          pin1=(str(pin1))
                          print(pin1)
                          lines[j+2]=pin1 +"\n"
                          fp=open("atmdata.txt",'w')
                          fp.writelines(lines)
                          fp.close()
                          print("pin changed successfully")
                          
             #     else  : 
             #          print("wrong pinn\n")
             #          break
             # else :
             #    print("user not found\n")
             #    break
                      
             j=j+4
             i=i-1
                 # if  i==0 :
                 #    print("not found\n")
                 
     if op==2 :
                   name=input("enter name\n")
                   pin=input("enter four digit no\n")
                   print("account created successfully")
                   print(name)
                   print(pin)
                   n1=random.randint(100000,999999)
                   print("card no",n1)
                   n1=(str(n1))
                   bal=(str(00))
                   f=open("atmdata.txt",'a')
                   f.write(n1 +'\n')
                   f.write(pin +'\n')
                   f.write(name + '\n')
                   f.write(bal + '\n')
                   f.close()
                   print(" thank you\n")
                   
     else :
         print("select a valid option\n")
         
                   

                                              
