

import os
import requests
import pandas as pd


# define the filepath for the later downloaded geojson data
file_path ='{0}/{1}'.format('C:\python_proj','lambay_island_dataset.csv')


# define a Function to download using the Url and save it to the defined path
def data_download(data, url, Destination_folder):
    # if the folder data doesn't exist, it will be created

    if not os.path.exists(data):
        os.mkdir(data)

    # sends a request to get a URL
    web_request = requests.get(url)
    # opens the file and saves it to the destination folder , wb indicates, that the file is in binary
    with open(Destination_folder, 'wb') as write_file:
        write_file.write(web_request.content)

    # returns a list containing the names of the entries in the directory given by path
    os.listdir(data)


# execute function with variables
data_download('data', 'https://storage.googleapis.com/surveying/lambay_island_dataset.csv', 'Destination_folder')

from shapely.geometry import Polygon, LineString, Point
from shapely.geometry import Point
import matplotlib as plt
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

data ='C:\pyenvs\lambay_island_dataset.csv'
pdf = pd.read_csv(data)
pdf.info()

geometry = [Point(xyz) for xyz in zip(pdf.longitude, pdf.latitude)]
gdf = gpd.GeoDataFrame(pdf, crs="EPSG:4326", geometry=geometry)
gdf.info()