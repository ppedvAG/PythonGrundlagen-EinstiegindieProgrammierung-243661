# Funktionen
# Code speichern, um diesen bei Bedarf verwenden zu können
# Funktionen können Parameter (Daten) empfangen
# Funktionen können Ergebnisse zurückgeben (Rückgabeparameter)

# Funktionen werden mit def definiert
# Syntax: def <Name der Funktion>(<Par1>, <Par2>, ...)
def hallo():
	print("Hallo Welt")

# Verwendung/Ausführung der Funktion
# Ab Zeile 10 kann die Funktion verwendet werden
hallo()

# Funktion mit Parameter
def addiere(x, y):
	print(f"{x} + {y} = {x + y}")

addiere(4, 5)
addiere(2, 8)
addiere(1, 3)

# Funktion mit return
# Wenn return ausgeführt wird, wird die Funktion an dieser Stelle beendet
def addiere(x, y):
	print(f"{x} + {y} = {x + y}")
	return x + y  # Sobald diese Zeile ausgeführt wird, kann das Ergebnis in eine Variable geschrieben werden

summe = addiere(4, 9)
print(summe)

# Parameter in Funktionen können alles sein
# Möglicherweise nicht im Sinne des Entwicklers
addiere("Hallo", "Welt")
addiere([1, 2, 3], [4, 5, 6])
# addiere(1, "Hallo")  # Funktioniert nicht, PyCharm sagt nichts

####################################################################

# Typen "empfehlen"
# Variablen/Parameter/Rückgabewerte in Python können beliebige Werte enthalten (Any)
def addiere2(x: int, y: int) -> float:
	print(f"{x} + {y} = {x + y}")
	return x + y

addiere2(4, 8)
addiere2("Hallo", "Welt")  # Nur eine Empfehlung, Code funktioniert

# Typen "erzwingen"
# Mittels Typvergleich prüfen, welche Typen bei den Parametern hineinkommen
def addiere3(x: int | float, y: int | float) -> int | float:  # Mehrere Empfehlungen mittels |
	if type(x) in [int, float] and type(y) in [int, float]:
		print(f"{x} + {y} = {x + y}")
		return x + y
	else:
		raise TypeError("Die Parameter müssen numerisch sein!")  # raise: Programm abstürzen lassen

addiere3(3, 7)
addiere3(3.5, 5)
# addiere3("Hallo", "Welt")

####################################################################

# Standardwerte bei Parametern
# Der User kann den Wert überschreiben
# Wenn der Wert nicht überschrieben wird, wird der Standardwert genommen
# Verwendung: Konfiguration von Funktionen

# Beispiel: Pandas read_csv
# Hat 30+ Parameter, wir können nur die Parameter setzen, die wir auch wirklich benötigen
# z.B. Tausendertrennzeichen und Dezimalzeichen
# pandas.read_csv(filepath_or_buffer, *, sep=<no_default>, delimiter=None, header='infer', names=<no_default>, index_col=None, usecols=None, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=<no_default>, skip_blank_lines=True, parse_dates=None, infer_datetime_format=<no_default>, keep_date_col=<no_default>, date_parser=<no_default>, date_format=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, encoding_errors='strict', dialect=None, on_bad_lines='error', delim_whitespace=<no_default>, low_memory=True, memory_map=False, float_precision=None, storage_options=None, dtype_backend=<no_default>)

def addiere(x = 0, y = 0, z = 0):
	return x + y + z

addiere()
addiere(1)
addiere(5, 2)
addiere(5, 2, 9)

# Jetzt können die Parameter per <Parameter>=<Wert> gesetzt werden
addiere(x=3, z=8)
# read_csv("File.csv", thousands=".", decimal=",")

####################################################################

# Arbitrary Arguments
# Beliebig viele Parameter übergeben
# Wird mit *<Name> definiert
# Kann nur einmal pro Funktion definiert werden
def summiere(*zahlen):
	ergebnis = 0
	for x in zahlen:
		ergebnis += x
	print(ergebnis)

summiere()
summiere(3)
summiere(3, 8)
summiere(3, 8, 4, 1, 9)
summiere(3, 8, 4, 1, 9, 6, 2, 3, 2)

# Arbitrary Keyword Arguments
# Beliebig viele BENANNTE Parameter übergeben
# Wird mit **<Name> definiert
# Kann nur einmal pro Funktion definiert werden
def listTeilnehmer(**tn):
	for kv in tn.items():
		print(f"{kv[0]}: {kv[1]}")

listTeilnehmer(Trainer = "Lukas", T2= "Tobias", T3= "Mykola", T4= "Antje", T5= "Claudia")

# Unpacking Operator
# Zerlegen von Listen/Dictionaries, damit diese in eine Funktion mit * oder ** Parameter hineinpassen
summiere(*[1, 2, 3])
tn = {
	"Trainer": "Lukas",
	"T2": "Tobias",
	"T3": "Mykola",
	"T4": "Antje",
	"T5": "Claudia"
}
listTeilnehmer(**tn)