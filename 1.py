#1 (to add bonus-05% to salary if emp has more than 5 year experiaence)
emp_name=str(input("enter the your name:"))
emp_sal=float(input("enter your salary:"))
emp_exp=int(input("how much years you been working for this company:"))
if(emp_exp>5):
    
            emp_sal=emp_sal*(.05)+emp_sal
            print (f"you got 5% bonus in salary :{emp_sal}")
else:
    print (f"your have same salary:{emp_sal}") 
