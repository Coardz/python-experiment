toggle = True

while toggle:
    ide = input("Editor:")

    if ide.lower() == "visual studio code":
        print("an execellent choice")
        toggle = False
    elif ide.lower() == "word" or ide.lower == "notepad":
        print("awful")
    else:
        print("not good")
    