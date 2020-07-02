sc = open("script.txt")
sc_fm = open("script_formatted.txt", 'w')

bank = ''
for line in sc.read().split("\n"):
    line = line.strip()
    if line == "": # write
        if bank =='':
            continue
        sc_fm.write((bank+"\n"))
        bank = ''
    else:
        bank += (line + " ")

