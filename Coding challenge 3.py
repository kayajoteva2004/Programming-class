# Love score
my_name = input("Enter your name: ")
name_of_crush = input("Enter your crush's name: ")
combined_names = my_name + name_of_crush

variable_count = 0
if "l" in combined_names:
    variable_count += 1
if "o" in combined_names:
    variable_count += 1
if "v" in combined_names:
    variable_count += 1
if "e" in combined_names:
    variable_count += 1


if variable_count < 1:
    print("No love between you.")
elif variable_count <= 2:
    print("You are somewhat okay.")
else:
    print("You are meant to be together.")


