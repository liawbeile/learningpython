# 'r' - read
# 'w' - write
# 'a' - append

#Reading a File and Printing its Content
# context manager (with)
# Good Practice
with open('random.txt', 'r') as f:
    while True:
        line=f.readline()
        if line:
            print(line)
        else:
            break

# Bad Practice. Never Use!
text_file=open('random.txt', 'r')

while True:
    line=text_file.readline()
    
    if line:
        print(line)
    else:
        break

text_file.close()

# Read All lines at once. Prefered Way
with open('random.txt', 'r') as fp:
    lines=fp.readlines()
    for line in lines:
        print(line)

# Write to a File
print('Writing to File')
list_of_countries=['Singapore', 'India', 'China', 'Japan']
with open('country_list.txt', 'w') as f:
    for country in list_of_countries:
        f.write(country)
        f.write('\n')
print('Done Writing to File')

#Appending another country
with open('country_list.txt', 'a') as f:
    f.write('USA')