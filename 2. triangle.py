a = float(input("Bitte geben Sie die Länge a ein: "))
b = float(input("Bitte geben Sie die Länge b ein: "))
c = float(input("Bitte geben Sie die Länge c ein: "))
if a+b>c and a+c>b and b+c>a:
    print("Das Dreieck lässt sich konstruieren :)")
else:
    print("Das Dreieck lässt sich nicht konstruieren :(")
