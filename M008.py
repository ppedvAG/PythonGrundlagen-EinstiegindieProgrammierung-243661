# Module
# Python Code auf mehrere Skripte aufteilen
# Diese Skripte ineinander laden

# Module importieren
# Zwei Optionen:
# - import
# - from import
# Jeder Import kann mit as <Name> mit einem Alias versehen werden

# import
# Importiert das gesamte File
# -> Alle Klassen und Funktionen aus dem File
import M007  # as ModulSieben

# WICHTIG: Bei einem import/from import wird das gesamte (importierte) Skript ausgeführt
# -> Aller Code sollte in Klassen/Funktionen abgelegt sein

# Beispiel: summiere aus M007 benutzen
summe = M007.summiere(1, 2, 3, 4, 5)  # Hier muss der Name des anderen Skripts angegeben werden
# summe = ModulSieben.summiere(1, 2, 3, 4, 5)

# from import
# Selbiges wie import, aber Klassen/Funktionen werden direkt in unser Skript eingebunden
# Wenn wir die entsprechenden Member verwenden wollen, müssen wir nicht den Namen des anderen Skripts angeben
from M007 import summiere, hallo  # Mehrere Imports gleichzeitig
hallo()  # Hier kein M007.<Name> notwendig
summe2 = summiere(4, 3, 2, 1)

# from <Name> import *
# Importiere alles aus dem anderen Skript und binde alles in diesem Skript ein
# Unterschiedlich zu import <Name>
from M007 import *
addiere(3, 4)

####################################################################

# An welchen Stellen werden Module gesucht?
import sys
print(sys.path)  # Liste mit Pfaden, welche beim Import durchsucht werden

for p in sys.path:
	print(p)

# 4 Pfade
# - Das Projekt selbst
# - In der Python Standard Bibliothek
# - In dem Ordner site-packages in der venv (externe Pakete)
# - Eigene Pfade (sys.path.append)
# Wenn das Modul nicht gefunden wird -> ModuleNotFoundError
sys.path.append("C:\\Users\\lk3\\Desktop")
# import xyz

####################################################################

# Externe Pakete installieren
# Zwei Optionen:

# - Über Python Packages
# -- Name eingeben -> Rechts auf Install klicken

# - Über pip
# -- pip install <Name>
# -- pip uninstall <Name>

# Extern installierte Pakete werden in \venv\site-packages gespeichert
# import numpy

####################################################################

# Die Main-Methode
# Der Startpunkt des gesamten Programms
# Wird immer am Ende des Skript platziert

# __name__
# Der Name des Skripts selbst, wenn es importiert wird
# Wenn das Skript direkt gestartet wird, ist der Name __main__

def main():
	print(__name__)

# Automatisch grünes Dreieck in PyCharm (links daneben)
if __name__ == "__main__":
	main()

####################################################################

# Packages
# Ordner anlegen, um die Skripte im Projekt nochmal besser zu gruppieren
import M008b.M008_Test  # Einzelnes Skript aus dem Ordner importieren
from M008b import *  # Alle Skripte aus dem Ordner importieren

# __init__.py
# Skript, welches ausgeführt wird, wenn ein oder mehrere Skripte aus dem Ordner importiert werden