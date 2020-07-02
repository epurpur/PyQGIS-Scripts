import processing

def select_by_location(zone_name):
    """ Selects parcels from all_2019_parcels which are within the spatial boundary of a given zone """

    parameters = { 'INPUT' : 'dbname=\'BRE_2019_Test\' host=localhost port=5432 sslmode=disable key=\'id_1\' srid=2264 type=MultiPolygon checkPrimaryKeyUnicity=\'1\' table=\"public\".\"All_Parcels_2019\" (geom)', 
                'INTERSECT' : f'postgres://dbname=\'BRE_2019_Test\' host=localhost port=5432 sslmode=disable key=\'id_2\' srid=2264 type=MultiPolygon checkPrimaryKeyUnicity=\'1\' table=\"public\".\"{zone_name}\" (geom)', 
                'METHOD' : 0, 
                'PREDICATE' : [6] }

    processing.runAndLoadResults('native:selectbylocation', parameters)
    
select_by_location('Zone1b')
    

#{ 'INPUT' : 'dbname=\'BRE_2019_Test\' host=localhost port=5432 sslmode=disable key=\'id_1\' srid=2264 type=MultiPolygon checkPrimaryKeyUnicity=\'1\' table=\"public\".\"All_Parcels_2019\" (geom)', 
#'INTERSECT' : 'postgres://dbname=\'BRE_2019_Test\' host=localhost port=5432 sslmode=disable key=\'id_2\' srid=2264 type=MultiPolygon checkPrimaryKeyUnicity=\'1\' table=\"public\".\"Zone1b\" (geom)', 
#'METHOD' : 0, 
#'PREDICATE' : [6] }



#Zone (capital Z)
def calculate_attributes():
    """Calculates values for 'Zone' column  after using 'Select By Location'
    to select all parcels from All_2019_parcels that are within each zone area.
    The zone column will label the corresponding columns for each zone as 
    ex: 'Zone1a', 'Zone1b', and so on """

    pass


#'native:selectbylocation'