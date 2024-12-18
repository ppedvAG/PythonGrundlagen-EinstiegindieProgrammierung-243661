# Try-Except
# Fehler behandeln, welche das Programm abstürzen lassen würden
# Das Skript stürzt hierbei nicht ab, und führt stattdessen Fehlerbehandlungscode aus
# Generell sollte eine if verwendet werden, um Fehler zu verhindern (wenn möglich)

try:  # Code, welcher einen Fehler werfen könnte
	eingabe = input("Gib eine Zahl ein: ")
	zahl = int(eingabe)
	
	div = 5 / zahl
except ValueError:  # except: Fehler behandeln
	print("Eingabe ist keine Zahl")
except ZeroDivisionError:
	print("Division durch 0 nicht möglich")
except Exception:  # Alle anderen Fehler fangen, da hier eine Vererbung vorliegt
	print("Anderer Fehler")

# raise: Selbst Fehler verursachen
# Plattformunabhängige Fehler kommunizieren
try:
	raise OSError("Fehler")
except OSError as e:  # as e: Fehler einen Namen geben, um auf die Fehlermeldung zugreifen zu können
	print(e)  # Hier wird jetzt die Fehlermeldung ausgegeben
	# logger.log(e)