filmes = {"Smurfs": 2011, "Carros": 2005, "Harry Potter: RdM 1": 2010}

for item in sorted(filmes, key = filmes.get):
    print (filmes[item])