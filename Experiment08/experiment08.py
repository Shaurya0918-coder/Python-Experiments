import re

# 1. match()
device = "IOT_4589"
r = re.match("IOT", device)
if r:
    print("Valid IOT device ID")
else:
    print("Invalid Device")


# 2. search()
p = "JAIN UNIVERSITY"
r = re.search("A", p)
if r:
    print("Letter found in string")
else:
    print("Letter not found")


# 3. findall()
data = "temp:24 , Humidity:60 , Pressure:1012"
r = re.findall("[0-9]+", data)

print(r)


# 4. finditer()
text = "cat bat mat cat rat"
pattern = "cat"
matches = re.finditer(pattern, text)

for m in matches:
    print("Match:", m.group(),
            "Start Position:",m.start(),
            "End Position",m.end())


# 5. split()
sensors = "Temp , Humidity , Pressure"
r = re.split(",", sensors)
print(r)


# 6. sub()
text2 = "The network will upgrade from 54 soon"
r = re.sub("54","64",text2)
print(r)


#7.fullmatch()
date = input("Enter Date(DD/MM/YYYY):")

pattern = r'^\d{2}/\d{2}/\d{4}$'

if re.fullmatch(pattern,date):
    print("Valid Date Format")
else:
    print("Invalid Date Format")
