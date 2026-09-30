import pandas as pd

data = pd.read_csv("students.csv")

data["Total"] = data[["Python", "Maths", "DBMS"]].sum(axis=1)

data["Average"] = data["Total"] / 3

data["Result"] = data["Average"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

print(data)

print("\nHighest Mark:", data["Total"].max())
print("Lowest Mark:", data["Total"].min())
print("Class Average:", data["Average"].mean())
