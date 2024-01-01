from get_db import execute_query
from get_db import select_query
import random
# Iniciar Carro Carretera
#usuario 1 camilo
camilo = 1
#Verifico Ubicacion usuario
query = "SELECT x, y FROM cityopeen.people WHERE idp = {}".format(camilo)
ubicacion = select_query(query)
print(ubicacion)
cx = ubicacion[0][0]
cy = ubicacion[0][1]


#Verifico si en la ubicacion tiene carro con el mismo dueño y en la misma ubicacion
query = "SELECT x, y FROM cityopeen.objects WHERE idp = {} and type = 'car' and x = {} and y = {}".format(camilo,cx, cy)
print(query)
car_avalible = select_query(query)
print(car_avalible)
if car_avalible == []:
    print("No hay carros disponibles")
if car_avalible != []:
    print("Hay un carro disponible de la misma persona")
if car_avalible == ubicacion:
    print("El carro esta en la misma ubicacion se puede usar")
    owner_id = camilo
#Verifico si existen mas personas en esa ubicacion
query = "SELECT idp FROM cityopeen.people WHERE x = {} and y = {}".format(cx, cy)
pasajeros = select_query(query)
#print("Pasajeros")
pasaj_id_1 = pasajeros[0][0]
pasaj_id_2 = pasajeros[1][0]

#verifico cual es carretera mas cercana para el vehiculo
map_x = cx
map_y = cy
#Verifico Mapa ubicacion actual
query = ("SELECT x{} FROM cityopeen.layer_map WHERE y = {}").format(map_x, map_y)
mapa_actual = select_query(query)
#print("Mapa actual")
mapa_act = str(mapa_actual[0][0])
mapa_act = mapa_act[1:]

#carretera abajo
cy_try_1 = map_y + 1
query = "SELECT {} FROM cityopeen.layer_map WHERE y = {} and x9 = '='".format(map_x, cy_try_1)
carretera_1 = select_query(query)
ubicacion_carretera_1 = [map_x, cy_try_1]
#print(query)
#print("carretera abajo")
#print(carretera_1)
#carretera arriba
cy_try_2 = map_y - 1
query = "SELECT {} FROM cityopeen.layer_map WHERE y = {} and x9 = '='".format(cx, cy_try_2)
carretera_2 = select_query(query)
ubicacion_carretera_2 = [cx, cy_try_2]
#print(query)
#print("carretera arriba")
#print(carretera_2)
#carretera izquierda
cx_try_3 = cx - 1
query = "SELECT x{} FROM cityopeen.layer_map WHERE y = {} and {} = '='".format(cx_try_3, cy, cx_try_3)
carretera_3 = select_query(query)
ubicacion_carretera_3 = [cx_try_3, cy]
#print(query)
#print("carretera izquierda")
#print(carretera_3)
#carretera derecha
cx_try_4 = cx + 1
query = "SELECT x{} FROM cityopeen.layer_map WHERE y = {} and {} = '='".format(cx_try_4, cy, cx_try_4)
carretera_4 = select_query(query)
ubicacion_carretera_4 = [cx_try_4, cy]
#print(query)
#print("carretera derecha")
#print(carretera_4)

#verifico opciones de carreteras
list_carretera = []
if carretera_1 != []:
    list_carretera.append(ubicacion_carretera_1)
if carretera_2 != []:
    list_carretera.append(ubicacion_carretera_2)
if carretera_3 != []:
    list_carretera.append(ubicacion_carretera_3)
if carretera_4 != []:
    list_carretera.append(ubicacion_carretera_4)
#print(list_carretera)

carretera_choice = random.choice(list_carretera)

x_new = carretera_choice[0]
y_new = carretera_choice[1]
print(x_new)
print(y_new)
if owner_id > 0:
    #Resultado
    update_ubicacion_people_1 = "UPDATE cityopeen.people SET y = {}, x = {} WHERE idp = 2".format(y_new,x_new,pasaj_id_1)
    update_ubicacion_people_2 = "UPDATE cityopeen.people SET y = {}, x = {} WHERE idp = 1".format(y_new,x_new,pasaj_id_2)
    update_query_map_1 = "UPDATE cityopeen.layer_map SET x{} = '={}' WHERE y = {}".format(x_new,mapa_act,y_new)
    update_query_map_2 = "UPDATE cityopeen.layer_map SET x{} = 'V' WHERE y = {}".format(cx, cy)
    update_query_map_3 = "UPDATE cityopeen.layer_map SET x{} = 'V' WHERE y = {}".format(cx, cy)
    update_query_object_1 = "UPDATE cityopeen.objects SET y = {}, x = {} WHERE idp = {}  and type = 'car'".format(y_new, x_new, owner_id)


    query_list = [update_ubicacion_people_1, update_ubicacion_people_2, update_query_map_1, update_query_map_2, update_query_map_3, update_query_object_1]
    for query in query_list:
        #execute_query(query)
        print(query)

# Ejecutando querys

print("Querys ejecutados correctamente")







