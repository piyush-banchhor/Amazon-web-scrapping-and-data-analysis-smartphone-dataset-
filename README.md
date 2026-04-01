# Amazon Smartphone Data Scraping & Analysis

# 📱 Amazon Smartphone Data Scraping & Analysis

## 📌 Project Overview

This project focuses on **web scraping and exploratory data analysis (EDA)** of smartphone listings from Amazon. The goal is to extract meaningful insights such as pricing trends, product popularity, and customer engagement using real-world e-commerce data.

---

## 🚀 Objectives

* Scrape smartphone product data from Amazon HTML page
* Clean and structure raw data into a usable dataset
* Perform exploratory data analysis (EDA)
* Derive insights related to pricing, reviews, and product trends

---

## 🛠️ Tech Stack

* **Python**
* **BeautifulSoup (bs4)** – Web scraping
* **Pandas** – Data manipulation
* **Matplotlib / Seaborn** – Data visualization (EDA)
* **Jupyter Notebook** – Analysis

---

## 📂 Project Structure

```
├── amazon web scrapping.py   # Web scraping script
├── amazon cleaning and EDA.ipynb  # Data cleaning & analysis
├── Amazon_Products.csv       # Extracted dataset
├── README.md                 # Project documentation
```

---

## 🔍 Web Scraping Process

* Parsed HTML using BeautifulSoup
* Extracted:

  * Product Name
  * Product Price
  * Product Reviews
* Stored structured data into a CSV file

📌 Example code snippet:

```
soup = BeautifulSoup(html, "lxml")
divs = soup.find_all("div", class_="puis-list-col-right")
```

Data extraction handled using try-except to manage missing values.

---

## 📊 Exploratory Data Analysis (EDA)

The dataset was analyzed to uncover:

* Price distribution of smartphones
* Relationship between price and reviews
* Most reviewed/popular products
* Data cleaning (handling missing values, formatting)

---

## 📈 Key Insights

* Most smartphones fall within a **mid-range price segment**
* Higher-priced phones do not always have higher reviews
* Some lower-priced phones have **high engagement (reviews)** indicating value-for-money products
* Presence of missing or inconsistent data highlights challenges in real-world scraping

---

## ⚠️ Limitations

* Data collected from static HTML (not live scraping)
* Limited dataset size
* Missing values due to incomplete HTML tags
* Amazon’s dynamic content may restrict full scraping

---

## 🔮 Future Improvements

* Implement live scraping using Selenium
* Add more features (ratings, discounts, brand)
* Build interactive dashboard (Power BI / Streamlit)
* Automate data pipeline

---

## 👨‍💻 Author

**Piyush Banchhor**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!

## ✅ Project Conclusion

This project successfully demonstrated the process of web scraping and data analysis using an Amazon smartphone dataset. By extracting product information such as name, price, and reviews from HTML content using BeautifulSoup, raw and unstructured data was converted into a structured format suitable for analysis.

The exploratory data analysis provided valuable insights into pricing patterns and customer engagement. It was observed that most smartphones fall within the mid-range price category, indicating strong demand in this segment. Additionally, the analysis showed that higher-priced smartphones do not always receive the highest number of reviews, suggesting that affordability and value-for-money play a significant role in customer preference.

The project also highlighted real-world challenges such as missing values and inconsistencies in scraped data, emphasizing the importance of data cleaning and preprocessing before analysis.

Overall, this project offered practical experience in web scraping, data transformation, and exploratory data analysis. It demonstrated how raw e-commerce data can be leveraged to uncover meaningful business insights.

This project can be further enhanced by incorporating additional features such as ratings, discounts, and brand information, as well as building interactive dashboards or predictive models for deeper analysis.

