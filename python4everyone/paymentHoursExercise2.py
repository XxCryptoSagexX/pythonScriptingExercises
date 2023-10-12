# Current conditions not set for OT
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
fhours = float(hours)
frate =  float(rate)

if fhours > 40:
    #print("Overtime")
    rgpay = fhours * frate
    otpay = (fhours - 40.0) * (frate * 0.5)
    #print(rgpay,pay)
    pay = rgpay + otpay
else:
   #print("Regular")
    pay = fhours * frate
print('Total Pay:',pay)