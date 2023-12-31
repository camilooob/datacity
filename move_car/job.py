from get_db import execute_query

# Querys generados por datagrip.
update_ubicacion_people_1 = "UPDATE cityopeen.people SET y = 6 WHERE idp = 2"
update_ubicacion_people_2 = "UPDATE cityopeen.people SET y = 6 WHERE idp = 1"
update_query_map_1 = "UPDATE cityopeen.layer_map SET `9` = '=R1O2' WHERE id = 6"
update_query_map_2 = "UPDATE cityopeen.layer_map SET `9` = 'V' WHERE id = 4"
update_query_map_3 = "UPDATE cityopeen.layer_map SET `9` = 'V' WHERE id = 5"
update_query_object_1 = "UPDATE cityopeen.objects SET y = 6 WHERE ido = 1"

# Ejecutando querys

r = execute_query(update_ubicacion_people_1)
execute_query(update_ubicacion_people_2)
execute_query(update_query_map_1)
execute_query(update_query_map_2)
execute_query(update_query_map_3)
execute_query(update_query_object_1)

print(r)
print("Querys ejecutados correctamente")







