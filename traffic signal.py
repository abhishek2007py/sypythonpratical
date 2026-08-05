print("*********Traffic signal*********")

signal=input("Enter the color of traffic signal : ").lower()

if signal=="red":
    print("action:🔴 Stop")
elif signal=="yellow":
    print("action:🟡 Get ready")
    
elif signal=="green":
    print("action:🟢 Go")

else:

    print("Invalid signal ")
