import pandas as pd
import matplotlib.pyplot as plt

# data
SL = [101, 102, 103, 104, 105]
Name = ["Bran", "Jamie", "Baalish", "Jon", "Arya"]

# dataframe
df = pd.DataFrame({
    "SL": SL,
    "Name": Name
})

print(df)

# plotting
plt.figure()
plt.plot(Name, SL)PROGRAM :
import numpy as np
import pandas as pd

# NumPy Arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Array A:", a)
print("Array B:", b)

print("Addition:", a + b)
print("Multiplication:", a * b)

# Pandas Series
s = pd.Series([100, 200, 300])
print("\nPandas Series:")
print(s)

# Pandas DataFrame
df = pd.DataFrame({
    "Product": ["Pen", "Book", "Bag"],
    "Price": [10, 50, 500]
})

print("\nPandas DataFrame:")
print(df)
plt.title("GoT")
plt.xlabel("Name")
plt.ylabel("Greatness")
plt.show()