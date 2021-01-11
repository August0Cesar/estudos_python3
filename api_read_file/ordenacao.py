############# Ordenação #################
lista = [
    {"name":"Augusto", "idade": 30},
    {"name":"Nayara", "idade": 28},
    {"name":"Dener", "idade": 27},
    {"name":"Fernando", "idade": 22}
]
lista_ordenada = sorted(lista, key=lambda p: p['idade'], reverse=True)
print(lista_ordenada)


############# Paginação #################
lista = [
    {"name":"Augusto", "idade": 30},
    {"name":"Nayara", "idade": 28},
    {"name":"Dener", "idade": 27},
    {"name":"Eron", "idade": 2},
    {"name":"Cecilia", "idade": 3},
    {"name":"Benjamim", "idade": 1},
    {"name":"Joao Pedro", "idade": 10},
    {"name":"Tel", "idade": 4},
    {"name":"Enzo", "idade": 1},
    {"name":"Icaro", "idade": 6},
    {"name":"Fernando", "idade": 22}
]