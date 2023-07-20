import requests
import csv

# Store URL
url_boutique = "https://myjoliecandle.com/"

# Prepare the CSV file
with open('produits.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Header of CSV
    writer.writerow(["Nom du Produit", "ID du Produit", "Nom de la Variante", "ID de la Variante", "Prix", "Disponible"])
    
    page = 1
    while True:
        # Get the data
        try:
            response = requests.get(f"{url_boutique}/products.json?page={page}")
            data = response.json()
        except:
            print(f'NUMERO DE PAGE >> {page}')

        # If no products, break the loop
        if not data['products']:
            break

        # For each product
        for product in data['products']:
            # Get the variants
            for variant in product['variants']:
                # Write in the CSV file
                writer.writerow([product['title'], product['id'], variant['title'], variant['id'], variant['price'], variant['available']])
                
        # Go the next page
        page += 1
