import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv("data/indian_food_nutrition.csv")
print(df.head())

plt.figure(figsize=(10,6))
sns.histplot(df["Calories (kcal)"], kde=True)
plt.title("Calorie Distribution")
plt.savefig("images/calories.png")
plt.show()

plt.figure(figsize=(8,6))
sns.scatterplot(x="Protein (g)", y="Carbohydrates (g)", data=df)
plt.title("Protein vs Carbohydrates")
plt.savefig("images/protein_vs_carbs.png")
plt.show()

top10 = df.sort_values("Calories (kcal)", ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x="Calories (kcal)", y="Name", data=top10)
plt.title("Top 10 High Calorie Foods")
plt.savefig("images/top10_calories.png")
plt.show()

fig = px.scatter(df, x="Fat (g)", y="Calories (kcal)", color="Protein (g)")
fig.show()
