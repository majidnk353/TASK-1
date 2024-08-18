#4 discount amount
cost=100
qnt=int(input("enter the quantity of the item ,which has 100 ruppees per item:"))
if(qnt>10):
        cost=(cost*qnt)-(cost*0.10)
        print(f"total cost of the item after discount is:{cost}")
else:
    print(f"total cost :{cost*qnt}(you cant claim discount)")
