print("Hello World")

print([i + 12 for i in range(1, 31) if i % 6 == 0])

text = "Ich bin ein Text"
print([b.upper() for b in text if b.islower()])

split = text.split(" ")
print([w[0].upper() for w in split])

print([w for w in split if len(w) <= 3])