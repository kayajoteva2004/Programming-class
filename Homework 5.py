# Map challenge
map_line_1 = [" ", " ", " "]
map_line_2 = [" ", " ", " "]
map_line_3 = [" ", " ", " "]
map = [map_line_1, map_line_2, map_line_3]

print(f"{map[0]}\n{map[1]}\n{map[2]}")
print("Select A, B or C for row and 1, 2 or 3 for column")


choice = input("Which column and row do you choose? ")

if choice[0] == "A":
    row = 0
elif choice[0] == "B":
    row = 1
elif choice[0] == "C":
    row = 2
else:
    print("Invalid row choice")
    exit()


column = int(choice[1]) - 1


map[row][column] = "X"


print()
print(f"{map[0]}\n{map[1]}\n{map[2]}")
