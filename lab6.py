# Finding Stuff
# You can get the following file with wget
# sudo wget -O text-flie-matrix.txt https://raw.githubusercontent.com/jimTheSTEAMClown/Python-Class-STEAM-Clown/refs/heads/main/text-file-matrix.txt
# sudo wget -O text-file-mail-very-short.txt https://raw.githubusercontent.com/jimTheSTEAMClown/Python-Class-STEAM-Clown/refs/heads/main/text-file-mail-very-short.txt
# sudo wget -O text-file-mail-short.txt https://raw.githubusercontent.com/jimTheSTEAMClown/Python-Class-STEAM-Clown/refs/heads/main/text-file-mail-short.txt
# sudo wget -O text-file-mail-long.txt https://raw.githubusercontent.com/jimTheSTEAMClown/Python-Class-STEAM-Clown/refs/heads/main/text-file-mail-long.txt

print('''
Use the String Methods to find stuff

  1) Can you find all the lines that start with "From:"
  2) What about line that start with "To:"
  3) Find all the lines with an email addresses
    - How would you find them?
    - Hint: split the line into a list of "words" then look for emails
  4) Dates? Can you find the line with the oldest "Date" 'Date: 2008-01-04 11:11:00 -0500 (Fri, 04 Jan 2008)'
    - Same Hint an 3
      
      ''')
xfile = open('text-file-mail-very-short.txt')
linenum = 0
fromlines = []
emails = []
for line in xfile:
    line=line.rstrip()
    linenum += 1
    if line.startswith("From: ") or line.startswith("To: "):
        print(line)
    if "@" in line:
        line = line.split(" ")
        for maybe in line:
            maybe = maybe.replace("<",'')
            maybe = maybe.replace(">",'')
            maybe = maybe.replace(";",'')
            maybe = maybe.replace(")",'')
            if "@" in maybe and maybe not in emails:
                emails.append(maybe)
for email in emails:
    print (email)
  #print(line)
#print("lines", ', '.join(str(num) for num in fromlines), 'start with "From: "')
#print(linenum)
