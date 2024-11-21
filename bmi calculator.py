weight=int(input("Enter the weight in kg:"))
height=float(input("Enter the height in metres:"))

bmi=weight/(height**2)

print("BMI of the person is:",bmi)

if bmi<18.5:
    print("Sorry!!You have to improve your health. You are underweight!!🥹")
elif bmi<25:
    print("Hurray!!You are normal!!😊")
elif bmi<30:
    print("Ohh Oh!!You have to reduce your weight. You are overweight!!🙀")
else:
    print("No way!!! Obesity has surrounded you!!😭")
