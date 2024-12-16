# Kommentare
# Text, welcher vom Compiler ignoriert wird
# Wird mit einer Raute definiert
import math

# Variable
# Behälter, welcher einen Wert halten kann
# Aufbau: <Name> = <Wert>

x = 5  # Hier wird eine Variable namens x angelegt, und mit dem Wert 5 versehen
# Ab Zeile 10 kann die Variable x im Code verwendet werden

print(x * 2)

# Datentypen
# int: Ganze Zahlen beliebiger Größe
i = 2198836509823156873912758698742173591035234

# float: Kommazahlen beliebiger Größe
f = 2197409214512.218461982480921759217598321598213  # WICHTIG: Kommazahlen IMMER mit Punkt definieren

# str: String, Text beliebiger Länge
s1 = "Hallo Welt"  # Strings müssen immer mit Hochkomma definiert werden
s2 = 'Hallo Welt'  # Alternative: Einzelne Hochkomma (selber Effekt)

# bool: Wahr-/Falschwert
b1 = True
b2 = False

# print: Konsolenausgabe
print(s1)
print(b1)
print(f)

#################################################################

# Stringfunktionen

text = "Das ist Ein Text"

# Der Punkt Operator (.): In eine Variable hineingreifen, und Funktionen dieser Variable benutzen
text.isnumeric()  # Mithilfe von <Variable>.<Funktion> auf Eigenschaften/Funktionen der entsprechende Variable zugreifen
print(text.isnumeric())  # Ist jedes Zeichen von text numerisch?

print(text.capitalize())  # Erzeuge eine Kopie von dem gegebenen Text und schreibe das erste Zeichen groß, den Rest klein

print(text.title())  # Erzeuge eine Kopie von dem gegebenen Text und schreibe das JEDES erste Zeichen groß, den Rest klein

print(text.count("e"))  # Wieviele e's befinden sich in dem Text?

print(text.count("e") + text.count("E"))

print(text.lower())  # Schreibe den gesamten Text in kleinbuchstaben
print(text.upper())  # Schreibe den gesamten Text in GROßBUCHSTABEN

print(text.lower().count("e"))  # Mehrere Funktion aneinanderhängen

#################################################################

# Index
# Ermöglicht, auf bestimmte Elemente innerhalb einer Liste zuzugreifen
# Benötigt eine Zahl und []
# Eckige Klammern: "An der Stelle"

text2 = "Das ist ein Text nochmal"
print(text2[0])  # WICHTIG: In der Programmierung wird mit 0 angefangen zu Zählen

print(text2[0:5])  # Doppelpunkt: Bis-Operator (Von Start bis Ende), Stellen 0, 1, 2, 3, 4

print(text2[-1])  # Minus-Operator: Liste von der anderen Seite angreifen

print(text2[-5:-1])  # chma

print(text2[-5:])  # Von -5 bis zum Ende

print(text2[:5])  # Vom Anfang bis zur Stelle 5

#################################################################

# Arithmetik
# +, -, *, /
# %: Modulo-Operator, Rest einer Division
# **: Potenz-Operator
# //: Ganzzahldivisions-Operator

z1 = 5
z2 = 8

print(z1 + z2)  # Berechne eine Summe, und schreibe diese Summe in die Konsole

# WICHTIG: + ohne = lässt die originalen Variablen unverändert

# Mit += können die Variablen verändert werden
z1 += z2  # Berechne eine Summe, und schreibe diese Summe in z1

# +=, -=, *=, /=, %=, **=, //=

# Divisionen
print(5 / 8)  # 0.625
print(5 // 8)  # 0, schneidet Kommastellen ab
print(5 % 8)  # 5

print(4 % 2)  # 0, gerade
print(5 % 2)  # 1, ungerade

# Strings multiplizieren
print("Das ist ein Text" * 50)