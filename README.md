# BMI Calculator in Python

This simple Python script calculates the **Body Mass Index (BMI)** of a person based on their weight and height. It also provides feedback on the BMI category with personalized messages.

---

### **Code Explanation**

1. **Input the Weight and Height**
   ```python
   weight = int(input("Enter the weight in kg: "))
   height = float(input("Enter the height in metres: "))
   ```
   - The script starts by asking the user to input their weight in kilograms (`kg`) and height in meters (`m`).
   - The weight is read as an integer (`int`), and height is read as a floating-point number (`float`).

2. **Calculate BMI**
   ```python
   bmi = weight / (height ** 2)
   ```
   - The BMI is calculated using the formula:
     \[
     \text{BMI} = \frac{\text{weight (kg)}}{\text{height (m)}^2}
     \]
   - The result is stored in the variable `bmi`.

3. **Display the BMI**
   ```python
   print("BMI of the person is:", bmi)
   ```
   - The calculated BMI value is displayed to the user.

4. **Classify the BMI**
   ```python
   if bmi < 18.5:
       print("Sorry!! You have to improve your health. You are underweight!! 🥹")
   elif bmi < 25:
       print("Hurray!! You are normal!! 😊")
   elif bmi < 30:
       print("Ohh Oh!! You have to reduce your weight. You are overweight!! 🙀")
   else:
       print("No way!!! Obesity has surrounded you!! 😭")
   ```
   - Based on the BMI value, the script categorizes the user's health into four ranges:
     - **Underweight**: BMI less than 18.5
     - **Normal**: BMI between 18.5 and 25 (exclusive)
     - **Overweight**: BMI between 25 and 30 (exclusive)
     - **Obesity**: BMI 30 or greater
   - For each category, a corresponding message is printed, including an emoji for a fun and interactive user experience.

---

### **Usage**
1. Run the script in a Python environment.
2. Enter the weight (in kilograms) and height (in meters) when prompted.
3. Read the BMI and the corresponding health feedback.

---

### **Example Run**
```plaintext
Enter the weight in kg: 70
Enter the height in metres: 1.75
BMI of the person is: 22.857142857142858
Hurray!! You are normal!! 😊
```

---

This script is a beginner-friendly project that combines basic Python concepts like input handling, mathematical operations, conditional statements, and string formatting.
