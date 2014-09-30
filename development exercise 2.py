#Brandon Dickson
#Develpment exercise 2
#30-09-2014

temperature=int(input("Temperature of water in centigrade:"))

if temperature == 100:
    print("The water is boiling.")

elif temperature <= 0:
    print("The water is frozen.")

else:
    print("The water is neither boiling or frozen.")
