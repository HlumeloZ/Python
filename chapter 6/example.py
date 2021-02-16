babys_names = {
'Mac' : ['Steven', 'Max'],
'Katie' : ['Muzi', 'Mike'],
'Zinhle': ['Star', 'Will'],
'Hlumelo' : ['Sergey', 'Dimitri'],
}

for name, babyNames in babys_names.items():
	print(f"\n{name.title()} chose these names:")
	for babyName in babyNames:
		print(f"\t{babyName.title()}")