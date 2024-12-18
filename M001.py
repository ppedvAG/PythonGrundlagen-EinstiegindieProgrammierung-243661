print("Hello World")

def countCase(wort: str):
	klein, gross, sonder = 0, 0, 0
	for b in wort:
		if b.islower():
			klein += 1
		elif b.isupper():
			gross += 1
		else:
			sonder += 1
	print(f"Sonderzeichen: {sonder}, Großbuchstaben: {gross}, Kleinbuchstaben: {klein}")

countCase("Das ist ein Text!")

########################################################

def listNamen(*namen: str):
	if len(namen) == 0:
		print("Keine Namen angegeben")
	elif len(namen) == 1:
		print(namen[0])
	elif len(namen) == 2:
		print(f"{namen[0]} und {namen[1]}")
	else:
		gesamt = ""
		for n in namen[0:-1]:
			gesamt += n + ", "
		gesamt = gesamt.rstrip(", ")
		gesamt += " und " + namen[-1]
		print(gesamt)

listNamen()
listNamen("T1")
listNamen("T1", "T2")
listNamen("T1", "T2", "T3", "T4", "T5")