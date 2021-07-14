text_file = "passwords.txt"
valid = 0 #count of valid passwords

with open(text_file, "r") as file:
    for cur_pass in file:
        count = 0 #count of right symbols in the password line
        symbol = cur_pass[0] # key of the line

        rule1 = int(cur_pass[2]) #first rule of pass
        rule2 = int(cur_pass[4]) #second rule of pass

        password = cur_pass[7:] #password line without rules

        for key in password:
            if key == symbol:
                count += 1 #if key is right, count +=1
        if rule1 <= count <= rule2:
            valid += 1
print(valid)#check the valid number in the console

with open(text_file, "a") as file:
    file.write("\nValid passwords: " + str(valid)) #rewrite the file with valid number
