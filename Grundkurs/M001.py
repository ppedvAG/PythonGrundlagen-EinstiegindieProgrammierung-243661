class Fahrzeug:
	def __init__(self, name: str, preis: float, maxV: int, aktV: int, motorzustand: bool):
		self.name = name
		self.preis = preis
		self.maxV = maxV
		
		if motorzustand == True:
			if aktV > maxV:
				self.aktV = maxV
			else:
				self.aktV = aktV
		else:
			self.aktV = 0
		self.motorzustand = motorzustand

	def starteMotor(self):
		if not self.motorzustand:
			print("Motor gestartet")
			self.motorzustand = True
		else:
			print("Motor läuft bereits")

	def stoppeMotor(self):
		if self.motorzustand and self.aktV <= 0:
			print("Motor gestoppt")
			self.motorzustand = False
		else:
			print("Motor ist bereits aus")

	def beschleunigen(self, a: int):
		if not self.motorzustand:
			print("Motor ist aus")
			return  # Wenn der Motor aus ist, beende die Funktion
		
		if a + self.aktV > self.maxV:
			print("MaxV würde überschritten werden")
			return

		if a + self.aktV < 0:
			print("MaxV würde unterschritten werden")
			return

		self.aktV += a
		print(f"Das Auto fährt jetzt {self.aktV}km/h")

	def beschreibung(self):
		return f"Das Fahrzeug {self.name} kostet {self.preis} ..."

fzg = Fahrzeug("VW", 20000, 200, 0, False)
fzg.starteMotor()
fzg.beschleunigen(50)
fzg.beschleunigen(500)
fzg.beschleunigen(-50)
fzg.stoppeMotor()