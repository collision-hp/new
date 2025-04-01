import pandas as pd
import matplotlib.pyplot as plt

# Lambda function to convert Celsius to Kelvin
c_to_k=lambda c:c+275.15

# Sample temperature data in Celsius
c_temps = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Convert Celsius to Kelvin using the lambda function
k_temps=list(map(c_to_k,c_temps))

# Create a pandas DataFrame to store the data
data = {
    'C': c_temps,
    'K': k_temps
}
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Plot the data
plt.plot(df['C'], df['K'], marker='o')
plt.title('Celsius to Kelvin Conversion')
plt.xlabel('Celsius')
plt.ylabel('Kelvin')
plt.grid(True)
plt.show()