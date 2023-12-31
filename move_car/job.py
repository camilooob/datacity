from get_db import execute_query

# Querys

update_ubicacion_people_1 = "UPDATE cityopeen.people SET y = 6 WHERE idp = 2"
update_ubicacion_people_2 = "UPDATE cityopeen.people SET y = 6 WHERE idp = 1"
update_query_map_1 = "UPDATE cityopeen.layer_map SET `9` = '=R1O2' WHERE id = 6"
update_query_map_2 = "UPDATE cityopeen.layer_map SET `9` = 'V' WHERE id = 4"
update_query_map_3 = "UPDATE cityopeen.layer_map SET `9` = 'V' WHERE id = 5"
update_query_object_1 = "UPDATE cityopeen.objects SET y = 6 WHERE ido = 1"

query_list = [update_ubicacion_people_1, update_ubicacion_people_2, update_query_map_1, update_query_map_2, update_query_map_3, update_query_object_1]
for query in query_list:
    execute_query(query)
# Ejecutando querys

print("Querys ejecutados correctamente")







