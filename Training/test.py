word = "word"
many = (*word, "s")

# print(many)



pets_list = {   'muffin' : "cat",
                'pupuce' : "cat",
                'pouchon' : "cat"   }

pets_list['mai'] = 'puppy'
del(pets_list['pupuce'])

# print(pets_list)



pets = ("muffin", "pouchon", "mai")
# On transforme une liste en un dictionnaire
# dict.fromkeys(list, value)
list_pets = dict.fromkeys(pets, None)

# print(list_pets)



# list() retourne le dictionnaire dans l'ordre d'insertion
# print(list(pets_list))
# sorted() retourne le dictionnaire dans l'ordre alphabétique
# print(sorted(pets_list))




# .items() retourne un iterrable avec un index et une valeur, il est donc possible de créer une boucle
pets_list.items()
# for name, race in pets_list.items():
    # print(name, ":", race)

pets_list.keys()
pets_list.values()
# .keys() et .values() fonctionnent sur le même principe que .items



# Pour fussioner deux dictionnaires, on utilisera une des méthodes suivantes
dict1 = {'a' : 1, 'b' : 2}
dict2 = {'c' : 3, 'd' : 4}

merged = {**dict1, **dict2}
# print(merged)
# ou
alternative = dict1 | dict2
# print(alternative)


dict3 = dict1 = {'a' : 1, 'b' : 2}
dict4 = {'d' : 4, 'c' : 3}
# Pour comparer deux dictionnaires
# print(dict1 == dict2) # False
# print(dict1 == dict3) # True
# print(dict2 == dict4) # True, l'ordre des clés n'a pas d'incidence pourvu qu'elles soient les mêmes



