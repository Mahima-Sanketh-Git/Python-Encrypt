nameenc = str(input("Enter Name of encrypt file : "))
fo = open(f"Me\\{nameenc}.txt", "r")


encrypt_code = {
    "1": "a",
    "2": "b",
    "3": "c",
    "4": "d",
    "5": "e",
    "6": "f",
    "7": "g",
    "8": "h",
    "9": "i",
    "a": "j",
    "b": "k",
    "c": "l",
    "d": "m",
    "e": "n",
    "f": "o",
    "g": "p",
    "h": "q",
    "i": "r",
    "j": "s",
    "k": "t",
    "l": "u",
    "m": "v",
    "n": "w",
    "o": "x",
    "p": "y",
    "q": "z",
    "r": " ",
}
name = str(input("Enter A Name for decrypt file : "))
User_tex = fo.read()
text_list = []
text_list.extend(User_tex)
new = open(f"Me\\{name}.txt", "x")

for i in text_list:
    x = encrypt_code.get(i)
    new.write(x)
