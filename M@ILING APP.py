import smtplib,webbrowser
import getpass




#method to get valid user id.

def Get_ID():
    AllDomains=['gmail','yahoo','hotmail','outlook']

    while True:                
        User_ID = str(input("E-Mail ID : "))
        if '@' and '.com' in User_ID:
            sym_position = User_ID.find('@')
            com_position = User_ID.find('.com')
            Domain_Name = User_ID[sym_position+1 : com_position]


            if Domain_Name in AllDomains:
                return User_ID,Domain_Name
                break
            else:
                print ("Service not avilable for " + str(Domain_Name) + " Domain Name..!!")
                continue
         
        else:
            print("Invalid E-Mail ID Provide it again !!")
            continue


""" 1)____Gmail____
Address : smtp.gmail.com
Port : 465 / 587
Security/Connection Type: ssl
AuthMode : login

    2)____Yahoo____
Address : smtp.mail.yahoo.com
Port : 465 / 587
Security/Connection Type: ssl
AuthMode : login

    3)____Live/Hotmail/Outlook____
Address : smtp-mail.outlook.com
Port : 587
Security/Connection Type: tls
AuthMode : login """

def smtp_domain(domain_name):
    if(domain_name=='gmail'):
        return 'smtp.gmail.com'
    elif(domain_name=='yahoo'):
        return 'smtp.yahoo.com'
    elif(domain_name=='hotmail' or 'outlook'):
        return 'smtp-mail.outlook.com'



print ("WELCOME __/\__ \n")
User_ID,Domain_Name=Get_ID()
Password=str(getpass.getpass(prompt='Password: ',stream=None))


while True:
    try:                                                   #For secure connection to server.
        SMTPDomain=smtp_domain(Domain_Name)
        server=smtplib.SMTP(SMTPDomain,465)
        server.ehlo()
        print("Please Wait !\n")
        server.starttls()
        server.login(User_ID,Password)


        '''
            For more details read documentation
            https://docs.python.org/3/library/smtplib.html
        '''

        
##    except smtplib.SMTPServerDisconnected:
##        print("Dissconnected from server,please try again !")

##
##    except (NameError ) as error:
##        
##        print(error)

##    except smtplib.SMTPAuthenticationError as e:
##        print("Invalid USERNAME/PASSWORD !,plaese try again ! \n")
##        User_ID,Domain_Name=Get_ID()
##        Password=str(input('Password: '))
##        continue
        
##
##    except SMTPConnectError:
##        print("Error occoured while connecting to server !")
##    except EOFError:
##        print("ERROR OCCOURED !")




    except :
        
        if(Domain_Name=='gmail'):
               print("Login Failed !!! \n 1) Your UserName/Password is Wrong \n 2) Please 'Enable' Gmail's security option 'ALLOW LESS SECURE APP' \n\nDo you want to open web page ?\n")
               Ans=str(input('y/n: '))
               if(Ans=='y'):                   
                   webbrowser.open('https://myaccount.google.com/lesssecureapps')
               else:
                   print("Okay,you may go to 'https://myaccount.google.com/lesssecureapps' and change it through your browser \n")
                   print("Re-enter your User-ID and Password again \n\n")
                   User_ID,Domain_Name=Get_ID()
                   Password=str(getpass.getpass(prompt='Password: ',stream=None))
                   continue
            
        
        else:
            print("Login Successfull !!")
            break
   
print("Enter Reciver's E-Mail ID\n")
Reciver_ID,Reciver_Domain=Get_ID()
print("\n\nTO: "+str(Reciver_ID)+"\n")
Subject=str(input("Subject: "))
Message=str(input("Message: "))
server.sendmail(User_ID,Reciver_ID,('Subject: ' + str(Subject)+ '\n\n' + str(Message)))

while True:
    repeat=str(input("Do you want to send another mail ?\n y/n: "))
    repeat=repeat.lower()
    if repeat=='y':
        print("Enter Reciver's E-Mail ID\n")
        Reciver_ID,Reciver_Domain=Get_ID()
        print("\nTO: "+str(Reciver_ID)+"\n")
        Subject=str(input("Subject: "))
        Message=str(input("Message: "))
        server.sendmail(User_ID,Reciver_ID,('Subject: ' + str(Subject)+ '\n\n' + str(Message)))
    else:
        print("Thank You :)")
        #server.close()
        server.quit()
