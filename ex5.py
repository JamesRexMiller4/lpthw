name = 'Zed A. Shaw'
age = 35.00 # not a lie
height = 74.00 # inches
weight = 180.00 # pounds
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# Inches to cm conversion = 1 in : 2.54 cm
# Pounds to kg conversion = 1 lb : .453592
# Years to dog years conversion = 1 yr : 7 yr

height_in_cm = 74.00 * 2.54
weight_in_kg = 180.00 * .453592
dog_years = 35.00 * 7

print(f"In centimeters that is, {height_in_cm}" )
print(f"In kilograms that is, {weight_in_kg}" )
print(f"In dog years that is, {dog_years}" )
