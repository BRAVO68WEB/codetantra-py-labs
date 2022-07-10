def lf(f, l):
    file = open(f, 'r')
    text = file.read()
    return text.count(l)


f = input("Enter the filename: ")
l = input("Enter the character to be searched: ")
# dont ask me why I have to put the print statement here
