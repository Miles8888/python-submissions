Rivers = {'yellow river': 'india', 'mississippi river': 'north america', 'yangtse river': 'china'}

for river, location in Rivers.items():
    print("The {} flows through {}.".format(river.title(), location.title()))