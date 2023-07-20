
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt



db = pd.read_csv("C:/Users/Frian/Desktop/Portfolio/WSP2023/WSP2023.csv")
db['growthRate'] = db['growthRate'] * 100
db['city_country'] = db["City"] + " (" + db["Country"] + ")"

asia_color = 'lightseagreen'

africa_color = 'orange'
america_color = 'cornflowerblue'
south_america_color = 'forestgreen'
db.head(5)


df = db.loc[:, ["growthRate", "Continent"]]

sns.barplot(x="Continent", y="growthRate", data=db, color= africa_color, errorbar=None)
sns.set(rc={"figure.figsize": (10, 6)})
plt.title("Rising popularity of continents" )
plt.text(2.4, -0.5, "(On this graph we see that in 2023 the popularity of Africa among tourists is significant)", fontsize=9, ha='center')
plt.show()


africa_top = db.query("Continent == 'Africa'").sort_values("growthRate", ascending=False).head()
sns.barplot(x="city_country", y="growthRate", data=africa_top,  color= africa_color)
plt.title("Top 5 most popular cities in Africa")
plt.show()



sorted_top = db.sort_values("growthRate",  ascending=False).head()
colors = [africa_color if i in [0, 1, 3] 
          else asia_color
          for i in range(len(sorted_top))]


sns.barplot(x= "city_country", y="growthRate", data=sorted_top, palette = colors)
sns.set(rc={"figure.figsize": (10, 6)})
plt.title("Cities with the highest growth in popularity")
plt.text(2, -0.8, "Among the top 5 emerging cities 3 are in Africa", fontsize=9, ha='center')
plt.show()


sorted_outtop = db.sort_values("growthRate",  ascending=True).head()


colors1 = [america_color if i in [0, 1, 2, 4] 
          else asia_color
          for i in range(len(sorted_outtop))]

sns.barplot(x= "city_country", y="growthRate", data=sorted_outtop, palette = colors1)
sns.set(rc={"figure.figsize": (13, 6)}) 
plt.title("Cities with the greatest decline in popularity")
plt.text(2, -4.1, "Among the top 5 losing popularity cities 4 are in America", fontsize=9, ha='center')
plt.show()


pop2022 = db["Pop2022"].sum()
pop2023 = db["Pop2023"].sum()
Table = {"Year": [2022, 2023], "Travelers": [pop2022 ,pop2023]}
Table = pd.DataFrame(Table)
sns.barplot(x="Year", y="Travelers", data=Table, color = africa_color)
sns.set(rc={"figure.figsize": (13, 6)})
plt.title("Tourism growth")
plt.text(0.5, 30, f"Increase in tourists per year reaches {round(db['growthRate'].mean(), ndigits=2)}%", fontsize=9, ha='center')
plt.show()



top_cities = db.sort_values("Pop2023", ascending=False).head()
сolors3 = [south_america_color if i in [4]
          else asia_color
          for i in range(len(top_cities))]
sns.barplot(x="Country", y="Pop2023", data=top_cities,  palette = сolors3)
plt.title("The most popular countries in 2023")
plt.text(0.5, -3, "On this graph, we can see that in 2023 the majority of the most popular countries for tourism are located in Asia", fontsize=9, ha='center')
plt.show()



south_america_top = db.query("Continent == 'South America'").sort_values("Pop2023", ascending=False).head()
south_america_out = db.query("Continent == 'South America'").sort_values("Pop2023", ascending=True).head()
sns.barplot(x="city_country", y="Pop2023", data=south_america_top,  color= south_america_color)
plt.title("The most popular cities in South America in 2023")
plt.show()



sns.barplot(x="city_country", y="Pop2023", data=south_america_out,  color= south_america_color)
plt.title("The most unpopular cities in South America in 2023 (in this sourse)")
plt.show()
