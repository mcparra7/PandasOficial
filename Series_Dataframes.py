# Importamos la biblioteca Pandas y la llamamos pd
import pandas as pd
# Creamos una serie de Pandas que es como una lista con etiquetas
# los valores son nombres de jugadores PSG
# el indice especifíca el número de camiseta del jugador

psg_players = pd.Series(
['Navas', 'Mbape', 'Neymar', 'Messi'], # Lista de jugadores
#   index = [1, 7, 10, 30] # lista de camisetas
)
# Creamos un diccionario que asocia número de camisetas con nombres de jugadores 
psg_dict = {1: 'Navas', 7: 'Mbape', 10: 'Neymar', 30: 'Messi'}
    

# Creamos una Serie de Pandas usando el diccionario
psg_players_dict =pd.Series(psg_dict)

# Imprimimos la Serie a partir del diccionario
print(psg_players_dict)

#imprimimos el valor en la posición (indice) 7 de la Serie creada a partir del diccionario
print(psg_players_dict[7])
print(psg_players_dict[0:4])

# Diccionario con datos de jugadores
dict ={'jugador', ['Navas', 'Mbape', 'Neymar', 'Messi'],
    'Altura': [183.0, 170.0, 170.0, 165.0],
    'Goles' : [2, 200, 150, 200]}

# Creamos un Dataframe con el diccionario e indices personalizados
df =pd.DataFrame(dict, index= [1, 7, 10, 30])

# imprimimos el Dataframe
# print (df)








