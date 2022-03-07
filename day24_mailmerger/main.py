with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

with open("./Input/Names/invited_names.txt") as invited_names:
    name_list = invited_names.read().splitlines()
    for name in name_list:
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="x") as output:
            output.write(letter.replace("[name]", name))
