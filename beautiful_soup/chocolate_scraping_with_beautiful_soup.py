import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1–4. Load webpage and parse HTML
chocolate = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")
soup = BeautifulSoup(chocolate.content, "html.parser")

# 5–8. Extract ratings
rating_tags = soup.find_all(attrs={"class": "Rating"})
ratings = []

for rating in rating_tags[1:]:     # skip header
    rate_text = rating.get_text()
    rate_score = float(rate_text)
    ratings.append(rate_score)

# Plot ratings histogram
plt.hist(ratings)
plt.show()

# 9–12. Extract company names
company_tags = soup.select(".Company")
company = []

for com in company_tags[1:]:       # skip header
    company.append(com.get_text())

# Create DataFrame
cacao_df = pd.DataFrame({
    "Company": company,
    "Ratings": ratings
})

# 13. Top 10 companies by rating
mean_ratings = cacao_df.groupby("Company").Ratings.mean()
ten_best = mean_ratings.nlargest(10)
print("Top 10 Chocolate Companies:\n", ten_best)

# Plot histogram again (Codecademy style)
plt.hist(ratings)
plt.show()
plt.clf()

# 14. Extract cocoa percentages
cocoa_percent_tags = soup.select(".CocoaPercent")
cocoa_percents = []

for coco in cocoa_percent_tags[1:]:    # skip header
    percent = float(coco.get_text().strip("%"))
    cocoa_percents.append(percent)

# 15. Add Cocoa Percentage column
cacao_df["CocoaPercentage"] = cocoa_percents

# 16. Scatter plot
plt.scatter(cacao_df.CocoaPercentage, cacao_df.Ratings)
plt.show()
plt.clf()

# 17. Line of best fit
plt.scatter(cacao_df.CocoaPercentage, cacao_df.Ratings)
z = np.polyfit(cacao_df.CocoaPercentage, cacao_df.Ratings, 1)
line_function = np.poly1d(z)
plt.plot(cacao_df.CocoaPercentage, line_function(cacao_df.CocoaPercentage), "r-")
plt.show()

# EXTRA EXPLORATION (Step 18)
# Bean origin analysis
origin_tags = soup.select(".BroadBeanOrigin")
origin = []

for ori in origin_tags[1:]:
    origin.append(ori.get_text())

beans_df = pd.DataFrame({
    "BeanOrigin": origin,
    "CocoaPercentage": cocoa_percents
})

mean_cocoa_percents = beans_df.groupby("BeanOrigin").CocoaPercentage.mean()
best_cocoa = mean_cocoa_percents.nlargest(10)
print("\nTop 10 Bean Origins by Avg Cocoa %:\n", best_cocoa)

# Country ratings analysis
country_tags = soup.select(".CompanyLocation")
countries = []

for c in country_tags[1:]:
    countries.append(c.get_text())

country_df = pd.DataFrame({
    "Country": countries,
    "Ratings": ratings
})

mean_rat = country_df.groupby("Country").Ratings.mean()
top_ten = mean_rat.nlargest(10)
print("\nTop 10 Countries by Rating:\n", top_ten)
