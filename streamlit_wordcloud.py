import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = ' ABHAY , MERN , ABHAY , AWS , CSM , Python , ABHAY , ITIL , PMP , ABHAY , MCSD , ABHAY , Data Analysis , Python '

wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

st.pyplot()
