import requests
import pandas as pd
from bs4 import BeautifulSoup

# Send a GET request to the Flipkart search page
uurl = "https://www.flipkart.com/search?sid=tyy%2C4io&p%5B%5D=facets.network_type%255B%255D%3D5G&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_1_5.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_92P8Y0U07S00_wp3&fm=neo%2Fmerchandising&iid=M_65cd8e01-08f1-4bdc-a05d-719ed0a8711e_5.92P8Y0U07S00&ppt=clp&ppn=mobile-phones-store&ssid=5enoi73xfk0000001685030864756&sort=price_asc&page="
products = []



pages = int(input("How many pages data u want\n"))
urls = []

for i in range(1,pages+1):
    urls.append(uurl+str(i))

for url in urls:
    response = requests.get(url)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the product details on the page
    product_elements = soup.find_all('div', {'class': '_2kHMtA'})
    for product in product_elements:
        name_element = product.find('div', {'class': '_4rR01T'})
        name = name_element.text.strip() if name_element else "N/A"

        price_element1 = product.find('div', {'class': '_30jeq3 _1_WHN1'})
        current_price = price_element1.text.replace('₹', '').replace(',', '').strip() if price_element1 else "N/A"

        price_element2 = product.find('div', {'class': '_3I9_wc _27UcVY'})
        actual_price = price_element2.text.replace('₹', '').replace(',', '').strip() if price_element2 else "N/A"

        offer_element = product.find('div', {'class': '_3Ay6Sb'})
        offer = offer_element.text.replace(r"% off","").strip() if offer_element else "N/A"

        review_element = product.find('div', {'class': '_3LWZlK'})
        rating = review_element.text.strip() if review_element else "N/A"

        discription_element = product.find('ul', {'class': '_1xgFaf'})
        discription_element_list = []
        for dic in discription_element:
            discription_element_list.append(dic.text.strip() if dic else "N/A")
        discription = "/".join(discription_element_list)

        imgscr_element = product.find('img', {'class': '_396cs4'})
        img = imgscr_element['src']


        products.append({
            'product_name': name,
            'current_price': current_price,
            'actual_price': actual_price,
            'offer(%)': offer,
            'rating': rating,
            'Discription': discription,
            'Image': img,
        })

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(products)


# Save the DataFrame to a CSV file
df.to_csv('../Mobile-Phones-Analysis/Data/flipkart_product.csv', index=False)
