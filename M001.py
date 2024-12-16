print("Hello World")

list1 = [1, 2, 3, 4, 10]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7, 8]
gesamt = list1 + list2 + list3

if 3 in gesamt or 7 in gesamt or 10 in gesamt:
	print()

gesamt = set(gesamt)
if len(gesamt.intersection([3, 7, 10])) > 0:
	print()

l = 0
if len(list1) > len(list2):
	l = list1
if len(list2) > len(list3):
	l = list2
if len(list3) > len(list1):
	l = list3

laengen = [len(list1), len(list2), len(list3)]  # [5, 5, 4]
laengste = max(laengen)  # 5
# laengen.sort()  # [4, 5, 5]
# laengste = laengen[-1]  # 5
if len(list1) == laengste:
	print("list1 ist die längste Liste")
if len(list2) == laengste:
	print("list2 ist die längste Liste")
if len(list3) == laengste:
	print("list3 ist die längste Liste")