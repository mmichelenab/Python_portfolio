#importeverythingrelevant

import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#get the URL
url = "https://content.codecademy.com/courses/beautifulsoup/cacao/index.html"
request = requests.get(url)
soup = BeautifulSoup(request.content, 'html.parser')
#print(soup)


 #obten la infomacion relevante
#ratings
rtgs = soup.find_all(attrs={"class": "Rating"})
ratings = []
for rtg in rtgs[1:]:
  ratings.append(float(rtg.get_text()))
#companies
companies = soup.find_all(attrs={"class": "Company"})
companies_names = []
for companie in companies[1:]:
  companies_names.append(companie.get_text())
#cocoapercentage
cocoa_percents = []
cocoa_percent_tags = soup.select(".CocoaPercent")
for td in cocoa_percent_tags[1:]:
  percent = float(td.get_text().strip('%'))
  percent = int(percent)
  cocoa_percents.append(percent)

#crear el data frame
d = {"Company": companies_names, "Rating": ratings, "CocoaPercentage": cocoa_percents}
df = pd.DataFrame.from_dict(d)

#groupby
meanvalues = df.groupby("Company").Rating.mean()
ten_best = meanvalues.nlargest(10)
print(ten_best)

#visualization of ratings
plt.hist(ratings)
plt.show()
plt.clf()

#scatterplot ratings
plt.scatter(df.CocoaPercentage, df.Rating)
z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")