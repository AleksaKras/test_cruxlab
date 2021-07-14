text_file = "passwords.txt"
passwords = list()
valid = 0

with open(text_file, "r") as file:
    for cur_pass in file:
        count = 0
        symbol = cur_pass[0]

        rule1 = int(cur_pass[2])
        rule2 = int(cur_pass[4])

        password = cur_pass[7:]

        for key in password:
            if key == symbol:
                count += 1
        if rule1 <= count <= rule2:
            valid += 1
print(valid)

with open(text_file, "a") as file:
    file.write("\nValid passwords: " + str(valid))
