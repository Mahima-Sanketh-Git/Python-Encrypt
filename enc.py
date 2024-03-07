fo = open("Me\\message.txt", "r")

encrypt_code = {
    "a": "1",
    "b": "2",
    "c": "3",
    "d": "4",
    "e": "5",
    "f": "6",
    "g": "7",
    "h": "8",
    "i": "9",
    "j": "a",
    "k": "b",
    "l": "c",
    "m": "d",
    "n": "e",
    "o": "f",
    "p": "g",
    "q": "h",
    "r": "i",
    "s": "j",
    "t": "k",
    "u": "l",
    "v": "m",
    "w": "n",
    "x": "o",
    "y": "p",
    "z": "q",
    " ": "r",
}
name = str(input("Enter a Name for encrypt file : "))
User_tex = fo.read()
text_list = []
text_list.extend(User_tex)
new = open(f"Me\\{name}.txt", "x")
for i in text_list:
    x = encrypt_code.get(i)
    new.write(x)
