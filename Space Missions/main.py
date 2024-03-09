
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_excel("ucs_satellite_database/UCS-Satellite-Database.xlsx")

# Data preprocessing
data['launch_date'] = pd.to_datetime(data['launch_date'], errors='coerce')
data['launch_year'] = data['launch_date'].dt.year

# Analyze mission outcomes
plt.figure(figsize=(12, 6))
outcome_counts = data['Purpose'].value_counts().head(10)
outcome_counts.plot(kind='bar')
plt.title('Top 10 Mission Purposes')
plt.xlabel('Mission Purpose')
plt.ylabel('Number of Missions')
plt.show()

# Analyze countries' involvement
plt.figure(figsize=(12, 6))
country_counts = data['Country of Operator/Owner'].value_counts().head(10)
country_counts.plot(kind='bar')
plt.title('Top 10 Countries with Most Space Missions')
plt.xlabel('Country')
plt.ylabel('Number of Missions')
plt.show()

# Analyze mission types
plt.figure(figsize=(12, 6))
orbit_counts = data['Class of Orbit'].value_counts()
orbit_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribution of Mission Orbits')
plt.ylabel('')
plt.show()

# Number of missions
missions_per_year = data.groupby('launch_year').size()

plt.figure(figsize=(10, 6))
missions_per_year.plot(kind='line')
plt.title('Number of Space Missions Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Missions')
plt.grid(True)
plt.show()

