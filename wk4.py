import fiona
from zipfile import ZipFile

with ZipFile("C:\\Users\\user\\Downloads\\counties2011.zip", 'r') as zObject:

    zObject.extractall(
        path="C:\\Users\\user\\Downloads\\pythonProject"
    )
shape = fiona.open("C:\\Users\\user\\Downloads\\pythonProject\\counties2011.shp")
print(len(shape))
print(shape.crs['init'])


