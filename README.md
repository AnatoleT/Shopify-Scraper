
# Shopify Scraper

Shopify Scraper is a free too that aims to index all the products (and its variants) of a shopify store.


## Requirements

For this tool, you'll just need the "requests" module, and import JSON.
It should work with every python version. If that's not the case, feel free to reach me out.
## How it works

Shopify has a special way to fetch products. For the majority of shopify stores, you just have to add at the end of base URL "products.json" (eg. www.myshopifystore.com/products.json).
If the store has lots of products, we can use the pagination by adding a parameter "?page=X" at the end.
## How to use it ?

You'll just have to modify this var "url_boutique" by the store you want to scrap.
Please, pay attention that the URL should contain the scheme (https://).

Once it's done, just launch this python script and the products will be listed in "products.csv".
Feel free to change the name of the file if you want to bulk the scrap.
## Authors

- [@AnatoleT](https://www.github.com/AnatoleT)

