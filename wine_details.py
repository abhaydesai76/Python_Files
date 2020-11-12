import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

df = pd.read_csv("C:\ChatBot\winemag-data-130k-v2.csv", index_col=0)

df.head()

print("There are {} observations and {} features in this dataset. \n".format(df.shape[0],df.shape[1]))

print("There are {} types of wine in this dataset such as {}... \n".format(len(df.variety.unique()),
                                                                           ", ".join(df.variety.unique()[0:5])))

print("There are {} countries producing wine in this dataset such as {}... \n".format(len(df.country.unique()),
                                                                                      ", ".join(df.country.unique()[0:5])))

print(df[["country", "description", "points"]].head())

country = df.groupby("country")
# print(country.describe().head())
#
# print(country.mean().sort_values(by="points",ascending=False).head())

# plt.figure(figsize=(10,10))
# country.size().sort_values(ascending=False).plot.bar()
# plt.xticks(rotation=50)
# plt.xlabel("Country of Origin")
# plt.ylabel("Number of Wines")
# plt.show()

# plt.figure(figsize=(10,10))
# country.max().sort_values(by="points",ascending=False)["points"].plot.bar()
# plt.xticks(rotation=50)
# plt.xlabel("Country of Origin")
# plt.ylabel("Highest point of Wines")
# plt.show()

# text = df.description[0]
#
# wordcloud = WordCloud(max_words=100,background_color='white').generate(text)
# plt.figure()
# plt.imshow(wordcloud, interpolation='nearest')
# plt.axis("off")
# plt.show()
#
# wordcloud.to_file("first_review.png")

# text = "".join(review for review in df.description)
# # print ("There are {} words in the combination of all review.".format(len(text)))

stopwords = set(STOPWORDS)
stopwords.update(["drink", "now", "wine", "flavor", "flavors"])

# wordcloud = WordCloud(stopwords=stopwords, background_color= "white").generate(text)
# plt.figure(figsize=(15,10))
# plt.imshow(wordcloud, interpolation='nearest')
# plt.axis("off")
# plt.show()

# wine_mask = np.array(Image.open("wine_glass.png"))
# # print(wine_mask)
#
# wc = WordCloud(background_color="white",max_words=1000,mask=wine_mask,stopwords=stopwords, contour_width=3, contour_color="firebrick")
# wc.generate(text)
#
# wc.to_file("wine.png")
#
# plt.figure(figsize=[20,10])
# plt.imshow(wc, interpolation='nearest')
# plt.axis("off")
# plt.show()

print(country.size().sort_values(ascending=False))
print(df[df["country"]=="India"].description)

india = "".join(review for review in df[df["country"]=="India"].description)
mask_india = np.array(Image.open("india_flag.png"))
wordcloud_india = WordCloud(stopwords=stopwords,background_color="white",mode="RGBA",max_words=1000,mask=mask_india).generate(india)

image_colors = ImageColorGenerator(mask_india)
plt.figure(figsize=[10,10])
plt.imshow(wordcloud_india.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.savefig("india_wine.png", format = "png")
plt.show()
