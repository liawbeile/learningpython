# Prac 1
# Read all lines in a text file

with open('random.txt','r') as f:
    while True:
        lines = f.readline()
        if lines:
            print(lines)
        else:
            break

# with opening of the random.txt file, to read, as f
# while the file is open
# set variable 'lines' = read one line in the text file
# if lines i.e. if able to read one line in the text file, then print the line
# else, break




# Prac 2
# Read first n lines of a file 

#Using readlines()
number = int(input('Number:'))
i=0
with open('random.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        i+=1
        if i<=number:
            print(line)

# find n from user
# set i=0
# opening of the text file & to read, set as f
# set 'lines' variable to read all lines in the file
# for every line in all the lines
# i + 1 every time it goes to a new line
# if lines are being read and i<= user input n, print the line 


#Alternative solution using readline():
number = int(input('Number:'))
i=0
with open('random.txt','r') as f:
    while True:
        lines = f.readline()
        if lines and i<number:
            i += 1
            print(lines)
        else:
            break

# find n from user
# set i=0
# opening of the text file & to read, set as f
#while text file is open
# set 'lines' variable to read line by line in the file
# i + 1 every time it goes to a new line
# if i < user input n, print the line 



# Prac 3
# Append text to a file and display the text

sentence = "This is a new sentence"

with open('random.txt','a') as f:
    lines=f.write("\n")
    lines=f.write(sentence)

#when file is open and we want to append
#append "next line"
#append the new sentence




# Prac 4
# Read all lines

with open('random.txt','r') as f:
    lines = f.readlines()
    for line in lines:
            print(line)

# opening of the text file & to read, set as f
# set 'lines' variable to all lines in the file
# for every line in lines
# print the line