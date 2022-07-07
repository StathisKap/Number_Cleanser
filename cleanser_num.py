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
    "nineteen" : 20, 
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

def Read_File(name):
    try:
        file = open(name, "rt")
        return file
    except:
        print("Error: Couldn't open file")
        exit(1)

def Translate(list_in):
    valid_sets = list()
    invalid_sets = list()

    for small_list in list_in:
        valid_members = list()
        for member in small_list:
            if member.lower() in English_numbers:
                valid_members.append(English_numbers[member.lower()])

            elif member.lower() in French_numbers:
                valid_members.append(French_numbers[member.lower()])

            elif member.lower() in German_numbers:
                valid_members.append(German_numbers[member.lower()])
            else:
                invalid_sets.append(small_list)

        valid_sets.append(valid_members)
    return invalid_sets , valid_sets


def Num_and_Text(filename): 
    file = Read_File("Sample2.txt")
    Lines = file.readlines()

    valid_sets = list()
    text_sets = list()

    for line in Lines:
        line = line.replace('“', '').replace('”', '').replace('\n', '').replace(" ", "")
        members = line.split(",")
        valid_members = list()
        text_members = list()
        for i in range(len(members)):
            if len(members[i]) > 0:
                if members[i][0].isalpha():
                    text_members.append(members[i])
                elif len(members[i]):
                    valid_members.append(int(members[i]))
            else:
                text_members.append(members[i])



        if len(valid_members) > 1:
            valid_sets.append(valid_members)

        if len(text_members) > 1:
            text_sets.append(text_members)
    file.close()
    return valid_sets, text_sets




valid_sets, text_sets = Num_and_Text("Sample2.txt")
invalid_sets , sets = Translate(text_sets)
valid_sets.append(sets)

print(invalid_sets)
print()
print(valid_sets)

