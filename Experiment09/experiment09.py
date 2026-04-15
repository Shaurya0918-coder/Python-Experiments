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
plt.plot(Name, SL)
plt.title("GoT")
plt.xlabel("Name")
plt.ylabel("Greatness")
plt.show()
