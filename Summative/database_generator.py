import random

def write_to_file(full_name, birthday, account_num, pin_num, salary, balance, credit_score, maximum_credit, account_type):
    '''
    Writes to the database.txt file
    '''
    database_file = open("database.txt","w")
    for t in range(len(full_name)):   
        print >>database_file, "<account>"
        print >>database_file, "<name> %s </name>" %(full_name[t])
        print >>database_file, "<birthday> %s </birthday>" %(birthday[t])
        print >>database_file, "<account number> %s </account number>" %(account_num[t])
        print >>database_file, "<pin number> %s </pin number>" %(pin_num[t])
        print >>database_file, "<salary> $%i </salary>" %(salary[t])
        print >>database_file, "<account balance> $%i </account balance>" %(balance[t])
        print >>database_file, "<credit score> %i </credit score>" %(credit_score[t])
        print >>database_file, "<maximum credit> $%i </maximum credit>" %(maximum_credit[t])
        print >>database_file, "<account type> %s </account type>" %(account_type[t])
        print >>database_file, "</account>"
        print >>database_file, ""
        print >>database_file, ""
    database_file.close()
    return

def create_database():
    '''
    Creates the database, by randomly generating: names, account balances
    account types, credit scores, pin numbers, birthdays, salaries, and max credit
    It then outputs the info to "write_to_file()"
    '''
    account = 355000000
    
    f_names = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Charles", "Joseph", "Thomas", "Christopher", "Daniel", "Paul", "Mark", "Donald", "George", "Kenneth", "Steven", "Edward", "Brian", "Ronald", "Anthony", "Kevin", "Jason", "Jeff", "Mary", "Patricia", "Linda", "Barbara", "Elizabeth", "Jennifer", "Maria", "Susan", "Margaret", "Dorothy", "Lisa", "Nancy", "Karen", "Betty", "Helen", "Sandra", "Donna", "Carol", "Ruth", "Sharon", "Michelle", "Laura", "Sarah", "Kimberly", "Deborah"]


    l_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins"]
    
    birthday = []
    full_name = []
    pin_num = []
    balance = []
    credit_score = []
    salary = []
    account_type = []
    maximum_credit = []
    account_num = []

    for i in range(0,1000):
        
        x = random.randint(0,49)
        y = random.randint(0,49)
        full_name += [f_names[x]+" "+l_names[y]]
        
        month = random.randint(1,12)
        
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            day = random.randint(1,31)
        
        elif month == 2:
            day = random.randint(1,28)
        
        elif month == 4 or month == 6 or month == 9 or month == 11:
            day = random.randint(1,30)
    
        year = random.randint(1939, 1991)
        birthday += ["%0.2i/%0.2i/%i" %(month, day, year)]
        
        if i == 0:
            account_num += [account + 1]
        else:
            account_num += [account_num[i-1] + 1]
        
        pin = ""
    
        for counter in range(0,4):
            p = random.randint(0,9)
            pin += str(p)
        pin_num += [pin]
        
        balance += [random.randint(0, 11500)-1500]
        credit_score += [random.randint(0,500)]
    
        if i > 990 and i <= 1000:
            salary += [random.randint(100000, 250000)]
        
        elif i <= 990 and i >= 0:
            salary += [random.randint(11500,100000)]
        
        if balance[i] >= 0:
            account_type += ["Debit"]
            maximum_credit += [credit_score[i]*100 + salary[i]*10 + balance[i]*10]
        
        elif balance[i] < 0:
            account_type += ["Credit"]
            maximum_credit += [credit_score[i]*100 + salary[i]*10 + balance[i]]
            if maximum_credit[i] < 0:
                maximim_credit += 0
    
    write_to_file(full_name, birthday, account_num, pin_num, salary, balance, credit_score, maximum_credit, account_type)
    return
