from bs4 import BeautifulSoup
import pandas as pd

# Read the HTML file
with open("Amazon.html", "r", encoding="utf-8") as f:
    html = f.read()

# Parse with BeautifulSoup
soup = BeautifulSoup(html, "lxml")

# Find all required divs
divs = soup.find_all(
    "div",
    class_="puisg-col puisg-col-4-of-4 puisg-col-4-of-8 puisg-col-8-of-12 "
           "puisg-col-8-of-16 puisg-col-12-of-20 puisg-col-12-of-24 "
           "puis-list-col-right"
)

products = []

for div in divs:

    # Product Name
    try:
        Product_Name = div.find(
            "h2",
            class_="a-size-medium a-spacing-none a-color-base a-text-normal"
        ).get_text(strip=True)
    except:
        Product_Name = " "

    # Product Price
    try:
        Product_Price = div.find(
            "span",
            class_="a-price-whole"
        ).get_text(strip=True)
    except:
        Product_Price = " "

    # Product Reviews
    try:
        Product_Reviews = div.find(
            "span",
            class_="a-size-small a-color-base",
            attrs={"aria-hidden": "true"}
        ).get_text(strip=True)
    except:
        Product_Reviews = " "

    products.append([Product_Name, Product_Price, Product_Reviews])

# Create DataFrame
df = pd.DataFrame(
    products,
    columns=["Product_Name", "Product_Price", "Product_Reviews"]
)

# Write to Excel
df.to_csv("Amazon_Products.csv", index=False, encoding="utf-8")

print("Amazon_Products.xlsx file created successfully")
