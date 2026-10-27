import pandas as pd

df = pd.read_excel("Maths.xlsx")
df.to_csv("Maths.csv", index=False, encoding="utf-8-sig")

dff = pd.read_excel("Portuguese.xlsx")
dff.to_csv("Portuguese.csv", index=False, encoding="utf-8-sig")
