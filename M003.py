# Listentypen
# Variablen die mehrere Werte halten können

# List
# Standardtyp für eine Auflistung von Elementen
# Kann beliebige Elemente enthalten
# Wird mit [ ] definiert

l = [1, 4, 2, 9, 3]
print(l)

# Index
print(l[0])
print(l[2:4])

# Länge der Liste
print(len(l))  # 5

# Listenfunktionen
# list.append(Wert): Neues Element hinzufügen
l.append(123)
print(l)

# list.sort(): Sortiert die Liste
l.sort()
print(l)

l.sort(reverse=True)  # Absteigend sortieren
print(l)

# list.pop(Index): Wert am gegebenen Index entfernen
l.pop(1)
print(l)

# list.remove(Wert): Sucht das erste Vorkommen des Wertes, und wirft diesen hinaus
l.remove(3)
print(l)

# Zwei Listen zusammenhängen
l1 = [1, 2, 3]
l2 = [4, 5, 6]

l1.append(l2)  # Hier wird die zweite Liste in die erste Liste hineingeschrieben
print(l1)

l1.remove(l2)

# list.extend(Liste): Hängt die Elemente aus der gegebenen Liste an die angegebene Liste an
l1.extend(l2)
print(l1)

l1 += l2  # += ist eine Alternative zu extend
print(l1)

#################################################################

# Tupel
# Funktioniert wie List, ist aber nicht veränderbar
# Hat einen Index
# Kann beliebige Elemente enthalten
# Wird mit ( ) definiert
t = (1, 2, 3, 4)
print(t)

# Tupel verändern
# Über Umweg
print(type(t))
print(type(l))

# Konvertierungen
# Den Typen einer Variable zu einem anderen Typen ändern
# Syntax: Zieltyp(Variable)
# z.B.: Tupel <-> List
umweg = list(t)
umweg.append(5)
t = tuple(umweg)
print(t)

# Andere Konvertierungen
eingabe = "50"
eingabe = int(eingabe)  # Wenn keine Konvertierung: 50 * 2 = 5050
print("Deine Zahl mal Zwei ist: " + str(eingabe * 2))  # Mit Konvertierung: 50 * 2 = 100

b = bool(1)
print(b)

b = bool(0)
print(b)

# Unpacking
# Zerlegung von Listen in einzelne Variablen
# Beispiel: t in 5 einzelne Variablen zerlegen

# (1, 2, 3, 4, 5)
a, b, c, d, e = t

print(a)
print(b)
print(c)

#################################################################

# range
# Bereich von X bis Y
r = range(100)  # Range ist nur ein Generator, dieser muss "gestartet" werden
print(r)

print(list(r))  # Hier muss der Generator gestartet werden

r2 = range(50, 100, 10)  # Range mit Untergrenze und Schrittgröße
print(list(r2))

#################################################################

# set
# Liste von EINDEUTIGEN Werten
# Wenn ein Duplikat in das Set kommen würde, wird es verworfen
# Wird mit { } definiert
s = {1, 2, 3, 4}
print(s)

# Deduplizieren mithilfe des Sets
duplikate = [1, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
print(set(duplikate))

#################################################################

# dict
# Funktioniert wie Set, aber jeder Wert hat einen Namen
# person = {"Lukas", 26, 75}  # Nicht sonderlich Aussagekräftig

person = {
	"Vorname": "Lukas",
	"Alter": 26,
	"Gewicht": 75
}

# Elemente im Dictionary werden mittels String-Index angegriffen
print(person["Alter"])

# Inhalte des Dictionaries angeben
print(person.keys())
print(person.values())
print(person.items())

# Neue Werte hinzufügen
person["Höhe"] = 180

print(person)