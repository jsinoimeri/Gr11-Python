from database_generator import *
create_database() # - creates a new database each time
file_name = open("database.txt")

name = []
account_num = []
pin_num = []
account_balance = []
account_type = []
birthday = []
credit_score = []
max_credit = []
salary = []

#searches through the lists
def search(the_list, key):
    '''
    Binary search since the lists are already sorted. Searches the list with the
    key given, if not in the list, it will return False and if found, it will 
    return the position of the key in the list.
    '''
    left = 0
    right = len(the_list)-1
    found = False
    pos = -1
    while left <= right and not found:
        mid = (left + right)/2
        
        if the_list[mid] > key:
            right = mid-1
        
        elif the_list[mid] < key:
            left = mid+1
        
        else:
            found = True
            pos = mid
            return pos
    
    return found
        

# reading from the file
for line in file_name:
    if "<account>" in line:
        account = True
    elif "</account>" in line:
        account = False
        
    if account == True:
        if "<name>" in line:
            line = line.strip()
            line = line.replace("<name>", "").replace("</name>", "")
            name += [line]
        
        if "<birthday>" in line:
            line = line.strip()
            line = line.replace("<birthday> ", "").replace(" </birthday>", "")
            birthday += [line] 
            
        if "<account number>" in line:
            line = line.strip()
            line = line.replace("<account number>", "").replace("</account number>", "")
            account_num += [int(line)]
        
        if "<pin number>" in line:
            line = line.strip()
            line = line.replace("<pin number>", "").replace("</pin number>", "")
            pin_num += [int(line)]
            
        if "<salary>" in line:
            line = line.strip()
            line = line.replace("<salary>", "").replace("</salary>", "").replace("$", "")
            salary += [int(line)]
        
        if "<account balance>" in line:
            line = line.strip()
            line = line.replace("<account balance>", "").replace("</account balance>", "").replace("$", "")
            account_balance += [int(line)]
        
        if "<credit score>" in line:
            line = line.strip()
            line = line.replace("<credit score>", "").replace("</credit score>", "")
            credit_score += [int(line)]        
                
        if "<maximum credit>" in line:
            line = line.strip()
            line = line.replace("<maximum credit>", "").replace("</maximum credit>", "").replace("$", "")
            max_credit += [int(line)]
        
        if "<account type>" in line:
            line = line.strip()
            line = line.replace("<account type>", "").replace("</account type>", "")
            account_type += [line]

file_name.close()
first_menu = "0"

# user menu
while first_menu != "4":
    first_menu = raw_input("\n1. log in\n2. new user\n3. forgot password\n4. Shut down\nYour choice (number please): ")
    
    if first_menu == "1":
        log_in_account = int(raw_input("Username (Account number): "))
        log_in_password = int(raw_input("Password (Pin number): "))
        
        #if account_num.__contains__(log_in_account):
            #pos_account_num = account_num.index(log_in_account)
        
        pos_account_num = search(account_num, log_in_account)
        if pos_account_num == int(pos_account_num):
            
            if pin_num.__contains__(log_in_password):
                pos_pin_num = pin_num.index(log_in_password)
            
            #pos_pin_num = search(pin_num, log_in_password)
            #if pos_pin_num == int(pos_pin_num):
                           
                if pos_account_num == pos_pin_num:
                    print "Welcome %s" %(name[pos_account_num])
                    
                    second_menu = "0"
                    while first_menu == "1" and second_menu != "6":
                        second_menu = raw_input("\n1. Check Balance\n2. Withdraw money\n3. Deposit money\n4. Make payment to someone else\n5. Change password\n6. Log out\nYour choice(number please): ")
                        
                        if second_menu == "1":
                            print "Your account is a%saccount with a balance of $%0.2f" %(account_type[pos_account_num],account_balance[pos_account_num])
                        
                        elif second_menu == "2":
                            confirmation = raw_input("\nYou have chosen to withdraw money. Do you wish to continue (y/n): ")
                            
                            if confirmation == "y" or confirmation == "yes" or confirmation == "Y" or confirmation == "Yes":
                                withdraw = float(raw_input("\nHow much money do you wish to withdraw?: "))
                                
                                if account_balance[pos_account_num] - withdraw < 0.00:
                                    print "\nYou tried to withdraw more money than you have in your account"
                                else:
                                    account_balance[pos_account_num] -= withdraw
                                    print "\nYour new balance is $%0.2f" %(account_balance[pos_account_num])
                        
                        elif second_menu == "3":
                            confirmation = raw_input("\nYou have chosen to deposit money. Do you wish to continue (y/n): ")
                            
                            if confirmation == "y" or confirmation == "yes" or confirmation == "Y" or confirmation == "Yes":
                                deposit = float(raw_input("\nHow much money do you wish to deposit?: "))
                                
                                account_balance[pos_account_num] += deposit
                                print "\nYour new balance is $%0.2f" %(account_balance[pos_account_num])
                        
                        elif second_menu == "4":
                            confirmation = raw_input("\nYou have chosen to make a payment to someone else. Do you wish to continue (y/n): ")
                            
                            if confirmation == "y" or confirmation == "yes" or confirmation == "Y" or confirmation == "Yes":
                                account_num2 = raw_input("\nPlease enter the account number of the person you wish to pay: ")
                                payment = float(raw_input("\nHow much money do you wish to deposit?: "))
                                
                                account_balance[pos_account_num] -= payment
                                print "\nYour new balance is $%0.2f" %(account_balance[pos_account_num])
                                
                                if account_num.__contains__(account_num2):
                                    pos_account_num2 = account_num.index(account_num2)
                                
                                #pos_account_num2 = search(account_num, account_num2)
                                #if pos_account_num2 == int:
                                
                                    account_balance[pos_account_num2] += payment
                                
                        elif second_menu == "5":
                            confirmation = raw_input("\nYou have chosen to change your pin number. Do you wish to continue (y/n): ")
                            
                            if confirmation == "y" or confirmation == "yes" or confirmation == "Y" or confirmation == "Yes":
                                new_pin = int(raw_input("\nEnter a new pin please: "))
                                pin_num[pos_pin_num] = new_pin
                                print "\nYour new pin is %i" %(pin_num[pos_pin_num])
        
        #write_to_file(full_name, birthday, account_num, pin_num, salary, account_balance, credit_score, max_credit, account_type)

# admin menu
    elif first_menu == "2":
        password = int(raw_input("\nThis is an administrator option\nEnter password: "))
        stop = False
        while stop == False:
            if password == 5555:
                done = False
                stop = True
            else:
                password = int(raw_input("\nEnter a valid password: "))
            
        while done == False:
                 
            full_name = raw_input("\nEnter full name: ")
            name += [full_name]
            
            bday = raw_input("\nEnter birthday (mm/dd/yyyy): ")
            birthday += [bday]
           
            account_num += [account_num[-1]+1]
            
            pin = int(raw_input("\nEnter four digit pin number: "))
            pin_num += [pin]
            
            sal = int(raw_input("\nEnter salary$: "))
            salary += [sal]
            
            acc_balance = int(raw_input("\nEnter account balance$: "))
            account_balance += [acc_balance]
            
            credit = int(raw_input("\nEnter credit score: "))
            credit_score += [credit]
            
            if account_balance >= 0:
                account_type += ["Debit"]
                maximum_credit = credit*100 + sal*10 + acc_balance*10
            
            elif account_balance < 0:
                account_type += ["Credit"]
                maximum_credit = credit*100 + sal*10 + acc_balance
                
                if maximum_credit < 0:
                    maximim_credit = 0
            
            max_credit += [maximum_credit]
            done2 = int(raw_input("\nAdd another user?\n1)Yes\n2)No\nAnswer (1-2): "))
            
            if done2 == 2:
                done = True
        
        write_to_file(name, birthday, account_num, pin_num, salary, account_balance, credit_score, max_credit, account_type)

# user menu for lost password
    elif first_menu == "3":
        false = False
        l_p_account_num = int(raw_input("\nUsername (Account number): "))
        l_p_birthday = raw_input("\nBirthday (mm/dd/yyyy): ")
        
        while false == False:

            #if account_num.__contains__(l_p_account_num):
                #pos_account_num = account_num.index(l_p_account_num)
            
            pos_account_num = search(account_num, l_p_account_num)
            if pos_account_num == int(pos_account_num):
                
                for birthdays in birthday:                   
                    if birthdays == l_p_birthday:
                        pos_birthday = birthday.index(l_p_birthday)
                        break
                    
                    else:
                        pos_birthday = -1
                
                #pos_birthday = search(birthday, l_p_birthday)               
                #if pos_birthday == int:
                
                if pos_account_num == pos_birthday:
                    print "\nYour pin is %i" %(pin_num[pos_birthday])
                    false = True
                
                if pos_birthday == -1:
                    l_p_birthday = raw_input("\nEnter a valid birthday (mm/dd/yyyy): ")
            
            else:
                l_p_account_num = int(raw_input("\nEnter a valid username (Account number): "))
