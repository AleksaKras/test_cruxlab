text_file = "passwords.txt"
valid_passwords = 0  # count of valid passwords
log = ''  # variable for logging of process
with open(text_file, "r") as file:
    for line_of_passwords in file:
        log += line_of_passwords  # save a line of passwords for logging of process

        count_of_same_symbols = 0  # count of same symbols in the password line
        main_symbol_of_line = line_of_passwords[0]  # main symbol of the password

        rule1 = int(line_of_passwords[2])  # first rule of password
        rule2 = int(line_of_passwords[4])  # second rule of password

        password = line_of_passwords[7:]

        for symbol in password:
            if symbol == main_symbol_of_line:
                count_of_same_symbols += 1  # if symbol is equal, count_of_same_symbols += 1

        if rule1 <= count_of_same_symbols <= rule2:
            valid_passwords += 1

print(valid_passwords)  # check the valid passwords in the console

with open("valid_passwords.txt", "a") as file:
    file.write(str(log) + "\nValid passwords: " + str(valid_passwords) + "\n \n")  # write in a new file count of valid passwords
