# ------------------------------------------------------------
# Name: Your Name
# Date: October 2025
# Project: Daily Calorie Tracker (CLI Tool)
# ------------------------------------------------------------

# Task 1: Setup & Introduction
print("=======================================")
print("  Welcome to the Daily Calorie Tracker  ")
print("=======================================")
print("This tool helps you log your meals, calculate total calories,")
print("compare them with your daily limit, and optionally save a log file.\n")

# Task 2: Input & Data Collection
meals = []
calories = []

# Ask how many meals user wants to enter
num_meals = int(input("How many meals do you want to log today? "))

for i in range(num_meals):
    print(f"\nMeal {i+1}:")
    meal_name = input("Enter meal name (e.g., Breakfast): ")
    cal = float(input("Enter calories for this meal: "))

    meals.append(meal_name)
    calories.append(cal)

# Task 3: Calorie Calculations
total_calories = sum(calories)
average_calories = total_calories / len(calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))

# Task 4: Exceed Limit Warning System
if total_calories > daily_limit:
    status = "⚠️ Warning: You have exceeded your daily calorie limit!"
else:
    status = "✅ Great job! You are within your daily calorie limit."

# Task 5: Neatly Formatted Output
print("\n=======================================")
print("         Daily Calorie Summary         ")
print("=======================================")
print("Meal Name\tCalories")
print("---------------------------------------")

for i in range(len(meals)):
    print(f"{meals[i]:<15}\t{calories[i]}")

print("---------------------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories:.2f}")
print("---------------------------------------")
print(status)
print("=======================================\n")

# Task 6 (Bonus): Save Session Log to File
save_option = input("Do you want to save this report to a file? (yes/no): ").strip().lower()

if save_option == "yes":
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "calorie_log.txt"

    with open(filename, "w") as file:
        file.write("===== Daily Calorie Tracker Log =====\n")
        file.write(f"Date/Time: {timestamp}\n\n")
        file.write("Meal Name\tCalories\n")
        file.write("---------------------------------------\n")
        for i in range(len(meals)):
            file.write(f"{meals[i]:<15}\t{calories[i]}\n")
        file.write("---------------------------------------\n")
        file.write(f"Total:\t\t{total_calories}\n")
        file.write(f"Average:\t{average_calories:.2f}\n")
        file.write(f"Status: {status}\n")
        file.write("=======================================\n")

    print(f"\n💾 Report saved successfully as '{filename}'.")
else:
    print("\nReport not saved. Goodbye!")

# End of Program
print("\nThank you for using the Daily Calorie Tracker!")