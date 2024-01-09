# Practicing python for CSE 111

age = int(input("What is your age? "))

heart_rate = 220 - age

# This could also be set up with the following:
# heart_rate = 220
# heart_rate -= age

min_heart_rate = .65 * heart_rate
max_heart_rate = .85 * heart_rate

print("When you exercise to strengthen your heart, you should")
print(f"keep your heart rate between {min_heart_rate:.0f} and {max_heart_rate:.0f} beats per minute.")