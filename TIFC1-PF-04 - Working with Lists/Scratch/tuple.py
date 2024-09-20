plants = ('cacti', 'pothos', 'eucalyptus')  #   Parenthesis bracket is use . is free element.
                                            # but cant change element in list but recreate a tuple again 
for plant in plants:
    print(plant)

plants = ('palm', 'tree', 'lily pad')
for plant in plants:
    print(plant)
   
print(plants)

###########################
plants_tuple = ('daffodil', 'pothos', 'eucalyptus')
plants_list = list(plants_tuple)
print(plants_list)
plants_list[0] = 'Crocus'
print(plants_list)
print(plants_tuple)

##########################
plants_tuple = ('daffodil', 'pothos', 'eucalyptus')
sliced_plant_tuple = plants_tuple[1:2]
print(sliced_plant_tuple)
plants_list = list(plants_tuple)
print(plants_list)
plants_list[0] = 'Crocus'
print(plants_list)
print(plants_tuple)