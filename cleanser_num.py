def Read_File(name):
    try:
        file = open(name, "rt")#, encoding="ISO-8859-1")
        return file
    except:
        print("Error: Couldn't open file")
        exit(1)


English_numbers = {
    "zero" : 0,
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "eight" : 8,
    "nine" : 9,
    "ten" : 10,
    "eleven" : 11,
    "fourteen" : 14,
    "sixteen" : 16,
    "twenty" : 20, 
    "twenty-one" : 21, 
    "twenty-two" : 22, 
}

French_numbers = {
    "un" : 1,
    "trois" : 3,
    "quatorze" : 4,
    "sept" : 7,
    "huit" : 8,
    "neuf" : 9,
    "onze" : 11,
    "douze" : 12,
    "quinze" : 15,
    "seize" : 16,
    "dix-huit" : 18,
    "vingt" : 20,
}

German_numbers = {
    "null" : 0,
    "eins" : 1,
    "zwei" : 2,
    "drei" : 3,
    "vier" : 4,
    "funf" : 5,
    "sechs" : 6,
    "acht" : 8,
    "neun" : 9,
    "vierzehn" : 14,
    "sechzehn" : 16,
    "einundzwanzig" : 21, 
}

file = Read_File("Sample2.txt")
Lines = file.readlines()

valid_sets = list()
invalid_sets = list()

for line in Lines:
    line = line.replace('“', '').replace('”', '').replace('\n', '').replace(" ", "")
    members = line.split(",")
    valid_members = list()
    invalid_members = list()
    for i in range(len(members)):
        try:
            valid_members.append(int(members[i]))
        except:
            invalid_members.append(members[i])
    print()
    valid_sets.append(valid_members) if len(valid_members) > 1 else print("no")
    invalid_sets.append(invalid_members) if len(valid_members) > 1 else print("no")

print(valid_sets)
print(invalid_sets)
file.close()