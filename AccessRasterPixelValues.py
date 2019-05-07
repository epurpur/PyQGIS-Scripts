layer = iface.activeLayer()
print("Active Layer: ", layer.name())
provider = layer.dataProvider()
extent = layer.extent()
stats = provider.bandStatistics(1, QgsRasterBandStats.All) 

rows = layer.height()
columns = layer.width()

block = provider.block(1, extent, columns, rows)

values= []
for row in range(rows):
    values.append([])
print("Values: ", values)

for row in range(rows):                   #iterates through each row
    for column in range(columns):         #iterates through each column
        values[row].append(block.value(row, column))   #appends the block.value to each position in values lists
print(f"Values: {values}")

flattened_list = []              #flattens values lists into one list
for list in values:
    for element in list:
        flattened_list.append(element)


unique_values = []
for item in flattened_list:
    if item not in unique_values:
        unique_values.append(item)
print("Unique Values:", unique_values)


for item in unique_values:
    count = 0

    for element in flattened_list:
        if element == item:
            count += 1

    print ("value: ", item, "count: ", count)