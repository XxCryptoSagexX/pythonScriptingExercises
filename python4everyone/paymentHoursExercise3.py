hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
try:
    fhours = float(hours)
except:
    fhours = -1
try:
    frate = float(rate)
except:
    frate = -2
if fhours and frate < 0:
    print("Error, please enter numeric input")
elif fhours > 40:
    #print("Overtime")
    rgpay = fhours * frate
    otpay = (fhours - 40.0) * (frate * 0.5)
    #print(rgpay,pay)
    pay = rgpay + otpay
    print('Total Pay:',pay)
else:
   #print("Regular")
    pay = fhours * frate
    print('Total Pay:',pay)
    
