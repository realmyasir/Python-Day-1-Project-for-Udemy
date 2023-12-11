print('WellCome to our bill distribution ')
bill=float(input('Enter Your Bill ?$'))
# print(bill)
tip=int(input('Enter percentage ? 10 12 15$'))
people= int(input('Each People Distribution$'))
bill_percentage=tip/100
total_tip_amount=bill*bill_percentage
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people
final_amount="{:.2f}".format(bill_per_person)
final_amount=round(bill_per_person,2)
print(f'Each Person Shount Pay $ {final_amount}')



# print(bill_percentage)150

# people_dist=people/bill_percentage


