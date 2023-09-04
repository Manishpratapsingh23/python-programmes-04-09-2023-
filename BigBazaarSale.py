#BIG BAZAAR SALE
amt=int(input("enter the amount: "))
if amt>=25000:
    print("THE CUSTOMER IS OF GOLD CATEGORY")
    amt=amt-((amt*20)/100)
    print("amout to be paid: ",amt)
elif amt<10000:
    print("THE CUSTOMER IS OF BRONZE CATEGORY")
    amt=amt-((amt*5)/100)
    print("amout to be paid: ",amt)
elif amt>=10000&amt<25000:
    print("THE CUSTOMER IS OF SILVER CATEGORY")
    amt=amt-((amt*10)/100)
    print("amout to be paid: ",amt)





#enter the amount: 3000
#THE CUSTOMER IS OF BRONZE CATEGORY
#amout to be paid:  2850.0



#enter the amount: 15000
#THE CUSTOMER IS OF SILVER CATEGORY
#amout to be paid:  13500.0


#enter the amount: 26000
#THE CUSTOMER IS OF GOLD CATEGORY
#amout to be paid:  20800.0


    
