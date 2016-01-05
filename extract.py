import re

file = open("list_emails.txt")
for line in file.readlines():
    file_row=line[0:-1];
    s = file_row #"Name Last <namelast@mail.com>"
    s = s.replace(",","")
    email = re.search('<?([^<>]+)>?$',s).group(0)
    email = email.replace("<","")
    email = email.replace(">","")

    #email = ''.join([e for e in s.split() if '@' in e])[1:-1]
    print email
file.close()
