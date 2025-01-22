# Read file: r (read) is used to read the files

"""with open('Resources/caperucita.txt', 'r') as file: 
    for lines in file:
        print(lines.strip())"""


# readlines() method is used to read all the lines of the file but storage in a list

"""with open('Resources/caperucita.txt', 'r') as file:
    lines = file.readlines()
    print(lines)"""


#Adding lines to the file: a (append)

"""with open('Resources/caperucita.txt', 'a') as file:
    file.write("\n\nBy: ChatGPT")"""


#Writing (rewrite!!!) the file: w

"""with open('Resources/caperucita.txt', 'w') as file:
    file.write("\n\nThis method rewrite the whole file")""" #you MUST be carefull when use this method, when you use "w" you will REWRITE THE WHOLE FILE.


# counting the number of lines of the file

with open('Resources/caperucita.txt', 'r') as file:
    line_count = len(file.readlines())
    print(f"Number of lines is:", {line_count})