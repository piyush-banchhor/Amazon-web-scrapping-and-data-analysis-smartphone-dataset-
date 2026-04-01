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
