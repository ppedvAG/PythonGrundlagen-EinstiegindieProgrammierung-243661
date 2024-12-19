# Input/Output

# print
# Konsolenausgaben
# Kann auch mehrere Werte getrennt mit einem gegebenen Separator ausgeben
print(1, 2, 3, sep=", ", end="Ende")

# input
# Usereingaben verlangen
# Bei Input kann auch eine Frage gestellt werden (an den Benutzer)
def inputTest():
	print()
	name = input("Gib deinen Namen ein: ")  # Wenn der User Enter drückt, wird die Eingabe in name hineingeschrieben
	print(f"Dein Name ist: {name}")

	x = input("Gib eine Zahl ein: ")
	y = input("Gib eine Zahl ein: ")

	x = int(x)
	y = int(y)
	print(f"{x} + {y} = {x + y}")

##################################################################

# open
# Mit externen Resourcen interagieren (Dateien, Datenbank, Webschnittstelle, ...)
file = open("File.txt", "w")
file.write("Hallo File\n")  # File wird hier nicht direkt beschrieben, sondern es wird zuerst ein Buffer beschrieben
file.write("Hallo File\n")
file.write("Hallo File")
file.flush()  # Inhalt des Buffers in das File hineinschreiben
file.close()  # Stream schließen (wenn ein Stream nicht geschlossen wird, bleibt die Resource [das File] belegt/unangreifbar)

##################################################################

# Escape-Sequenzen
# Undruckbare Zeichen in einem String einbetten
# u.a. Zeilenumbruch, Tabulator
# https://learn.microsoft.com/en-us/cpp/c-language/escape-sequences?view=msvc-170

# Wichtigste:
# \n: Zeilenumbruch
# \t: Tabulator
# \\: Backslash
pfad = "C:\\Users"  # Zwei Backslashes benötigt, weil sonst eine Escape-Sequenz erkannt wird

##################################################################

# with-Statement
# Das with-Statement ermöglicht, automatisch ein close am Ende des Blocks zu machen
# Sollte generell immer verwendet werden, beim Arbeiten mit Files
with open("File.txt", "r") as file:
	lines = file.readlines()  # Gesamtes File als Liste einlesen
	print(lines)
	# file.close() # Automatisch

##################################################################

# rstring
# raw string
# String, welcher Escape-Sequenzen ignoriert
# d.h. \n, \, \t können im String einfach verwendet werden
pfadR = r"C:\Users\n"