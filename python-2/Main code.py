#importing libraries
import pandas as pd 
import matplotlib.pyplot as plt
from PIL import Image
#Reading data into a data frame df
file_path = r'C:/Users/sarat/OneDrive/Desktop/python-2/GrowLocations.csv'
df = pd.read_csv(file_path)

#Altering dataset to correct the column values
#The values in 'Latitude' and 'Longitude' columns are interchanged so created 
#copies of those columns named LATITUDE, LONGITUDE which stand for correct values of Latitude and Longitude respectively.
df['LATITUDE'], df['LONGITUDE'] = df['Longitude'], df['Latitude']

#dropping wrong columns 'Latitude' and 'Longitude' from data frame
df.drop(columns=['Latitude','Longitude'], inplace=True)
print("\nDataFrame after interchanging values:")
print(df)

latitude_column = 'LATITUDE'
longitude_column = 'LONGITUDE'
#Removing wrong and unwanted values
#Setting boundaries for latitude and longitude values
latitude_lower_bound = 50.681
latitude_upper_bound = 57.985
longitude_lower_bound = -10.592
longitude_upper_bound = 1.6848

# Creating a boolean mask to filter rows based on the specified boundaries
mask = (
    (df[latitude_column] >= latitude_lower_bound) & (df[latitude_column] <= latitude_upper_bound) &
    (df[longitude_column] >= longitude_lower_bound) & (df[longitude_column] <= longitude_upper_bound)
)

# Applying the above mask to the DataFrame 'df' to get a new DataFrame named 'clean_df'
clean_df = df[mask]

#Saving 'clean_df' to a new CSV file
clean_df.to_csv('clean_data.csv', index=False)

# Setting up the map image
map_image_path = r'C:/Users/sarat/OneDrive/Desktop/python-2/map7.png'  
map_image = plt.imread(map_image_path)

# Plotting the correct latitude and longitude points on the map image
fig, ax = plt.subplots(figsize=(10, 8))
ax.imshow(map_image, extent=[ -10.592,1.6848, 50.681, 57.985])

# Scatter plot for latitude and longitude points
ax.scatter(clean_df['LONGITUDE'], clean_df['LATITUDE'], color='red', alpha=0.7, label='Sensor Locations')

# Adding labels, title and legend
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('Grow Locations Scatter-Plot')
plt.legend()

# Saving the overlaid map as a new PNG file
plt.savefig(r'C:/Users/sarat/OneDrive/Desktop/python-2/output_map.png')

# Output map
plt.show()

#REFERENCES
# https://www.mapsofworld.com/lat_long/united-kingdom-lat-long.html 
# https://books.goalkicker.com/PythonBook/
