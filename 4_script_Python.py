import pandas as pd
import json
import requests

url = "https://edamam-food-and-grocery-database.p.rapidapi.com/api/food-database/v2/parser"

querystring = {
    "app_key": "56c9423f7a3c76f991e97c781c7ed958",
    "app_id": "bf70547b",
    "nutrition-type": "cooking",
    "category[0]": "generic-foods",
    "health[0]": "alcohol-free",
    "ingr": "champagne"
}

headers = {
    "X-RapidAPI-Key": "2912abea9cmsh9bf3fe4dc41b3b4p10a6c7jsnc3a9e4894b9f",
    "X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data_API = response.json()

hints = data_API.get('hints', [])

hint_data = []
for hint in hints:
    food = hint['food']
    food_id = food.get('foodId')
    label = food.get('label')
    category = food.get('category')
    food_contents_label = food.get('foodContentsLabel')
    image = food.get('image')

    hint_data.append({
        'foodId': food_id,
        'label': label,
        'category': category,
        'foodContentsLabel': food_contents_label,
        'image': image
    })

if hint_data:
    df_API = pd.DataFrame(hint_data[:10]) 

print(df_API)
df_API.to_csv('APi_Champagne.csv', index=False)
print(df_API)




