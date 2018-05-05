Python 3.4.2 (default, Oct  8 2014, 10:45:20) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> players = [29, 58, 66, 71, 87]
>>> players[2]
66
>>> players
[29, 58, 66, 71, 87]
>>> players[2] = 68
>>> players
[29, 58, 68, 71, 87]
>>> players + [90, 91, 98]
[29, 58, 68, 71, 87, 90, 91, 98]
>>> players
[29, 58, 68, 71, 87]
>>> players.append(120)	# pripoj na koniec zoznamu nieco
>>> players
[29, 58, 68, 71, 87, 120]
>>> # + operator meni zoznam docasne, append() meni zoznam natrvalo
>>> 
>>> players[:2]
[29, 58]
>>> playe
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    playe
NameError: name 'playe' is not defined
>>> players[:2] = [0, 0]	# zmen prvy a druhy prvok na nuly
>>> players
[0, 0, 68, 71, 87, 120]
>>> players[:2] = []
>>> players
[68, 71, 87, 120]
>>> # hodnoty sa zo zoznamu odstranuju tak, ze priradime prvku '[]'
>>> players[:]	# vymazanie zoznamu
[68, 71, 87, 120]
>>> players[:] = []
>>> players
[]
>>> 
