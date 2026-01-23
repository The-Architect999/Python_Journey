#SIP CALCULATOR
cap = input("what is the amount you'll be investing monthly?")
avg_roi = input("what is the interest rate you're expecting (%)")

#value conversions
cap0 = int(cap)
avg_roi0 = int(avg_roi)
avg_roi_multiple = (avg_roi0 / 100) + 1
yearly = cap0 * 12

#base values
bank = 0
interest = 0
year_counter = 0

#To do or not to do that is the question
while True:
    carry_on = input("do you wish to know more? [y/n]")
    if carry_on == "n":
        print("okay, stay POOR🤮 i guess")
        break
    else:
        #the math
        year_counter += 1
        bank += yearly
        new_total = bank * avg_roi_multiple
        interest = new_total - bank
        bank = new_total
        
        print(f""" for year {year_counter},
              so far you have invested: {yearly * year_counter},
              the interest you earned was: {round(interest, 2)},
              year {year_counter} Total wealth: {round(bank, 2)}""")

    

    
    
