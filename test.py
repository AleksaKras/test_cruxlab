text_file = "passwords.txt"
count_of_valid_passwords = 0
log = ''  # variable for logging of process
with open(text_file, "r") as file:
    for line_of_passwords in file:
        log += line_of_passwords  # save a line of passwords for logging of process

        required_symbol_of_line = line_of_passwords[0]  # required symbol of the password

        min_quantity_of_repetition = int(line_of_passwords[2])  # first rule of password
        max_quantity_of_repetition = int(line_of_passwords[4])  # second rule of password

        password = line_of_passwords[7:]

        count_of_same_symbols = password.count(required_symbol_of_line)

        if min_quantity_of_repetition <= count_of_same_symbols <= max_quantity_of_repetition:
            count_of_valid_passwords += 1

print(count_of_valid_passwords)  # check the valid passwords in the console
log += "\nValid passwords: " + str(count_of_valid_passwords) + "\n \n"
with open("valid_passwords.txt", "a") as file:
    file.write(log)
