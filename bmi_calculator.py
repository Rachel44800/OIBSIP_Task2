def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi <= 16:
        return "Very underweight"
    elif bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    else:
        return "Very overweight"

h = float(input("Enter your height in meters: "))
w = float(input("Enter your weight in kilograms: "))

bmi = calculate_bmi(w, h)
category = classify_bmi(bmi)

print(f"BMI Calculated is: {bmi:.2f}")
print(f"You are classified as: {category}")
