# Opening File Handles and reading data from files
print('''
This Lab is about opening a file handle, and reading 
the file, line by line using the file method: 
- file_handle = open(file_name) method
      ''')
# Challenges
print('''
Challenge #1 & #2
----------------------------------------------------
#1 - Edit the code below to count each line, 
     and print the total out at the end
      
#2 - Edit the code below to open the text-file-mail-short.txt file
---
''')
# -------------------------------------------------
print('''Answer to Challenges
-------------------------------------------------''')
# -----------------------------
fhand = open('text-file-mail-very-short.txt')
john = 0
for line in fhand:
    john += 1
    print(line.rstrip())
print('Line Count:', john)
print('''
-------------------------------------------------''')
