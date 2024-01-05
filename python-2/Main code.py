import pandas as pd 
import matplotlib.pyplot as plt
from PIL import Image
file_path = r'C:/Users/sarat/OneDrive/Desktop/python-2/GrowLocations.csv'
df = pd.read_csv(file_path)
# Interchange the values in 'Latitude' and 'Longitude' columns

df['LAT'], df['LNG'] = df['Longitude'], df['Latitude']

print("\nDataFrame after interchanging values:")
print(df)

latitude_column = 'LAT'
longitude_column = 'LNG'

# Set boundaries for latitude and longitude values
latitude_lower_bound = 50.681
latitude_upper_bound = 57.985
longitude_lower_bound = -10.592
longitude_upper_bound = 1.6848

# Create a boolean mask to filter rows based on the specified boundaries
mask = (
    (df[latitude_column] >= latitude_lower_bound) & (df[latitude_column] <= latitude_upper_bound) &
    (df[longitude_column] >= longitude_lower_bound) & (df[longitude_column] <= longitude_upper_bound)
)

# Apply the mask to the DataFrame to get a new DataFrame named 'clean_df'
clean_df = df[mask]

# Save 'clean_df' to a new CSV file (optional)
clean_df.to_csv('clean_data.csv', index=False)


# Set up the map image
map_image_path = r'C:/Users/sarat/OneDrive/Desktop/python-2/map7.png'  # Replace with the path to your map image
map_image = plt.imread(map_image_path)

# Plot latitude and longitude points on the map image
fig, ax = plt.subplots(figsize=(10, 8))
ax.imshow(map_image, extent=[ -10,2, 50, 60])

# Scatter plot for latitude and longitude points
ax.scatter(clean_df['LNG'], clean_df['LAT'], color='red', alpha=0.7, label='Cleaned Points')

# Add labels, title, and legend
plt.xlabel('LAT')
plt.ylabel('LNG')
plt.title('Cleaned Latitude and Longitude Points on Map')
plt.legend()

# Save the overlaid map as a PNG file
plt.savefig(r'C:/Users/sarat/OneDrive/Desktop/python-2/overlay_map.png')

# Show the overlaid map
plt.show()


