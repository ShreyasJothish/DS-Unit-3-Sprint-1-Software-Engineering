"""
File name: acme_report.py
Developer: Shreyas Jothish
Description: Acme Corporation - Generate random products and
print a summary of them.
"""

import random
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']


def generate_products(product_num=30):
    """
    Generate a given number of products randomly,
    and return them as a list.
    """
    product_list = []

    for i in range(product_num):
        name = random.choice(ADJECTIVES) + " " + random.choice(NOUNS)
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)

        product_list.append(Product(name, price, weight, flammability))

    return product_list


def inventory_report(product_list):
    """
    Prints a "nice" summary of list of products mentioned below:
    Number of unique product names in the product list
    Average (mean) price, weight, and flammability of listed products
    """
    product_set = set()
    total_price = 0
    total_weight = 0
    total_flammability = 0
    num_of_products = len(product_list)

    for product in product_list:
        product_set.add(product.name)
        total_price += product.price
        total_weight += product.weight
        total_flammability += product.flammability

    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print(f"Unique product names: {len(product_set)}")
    print(f'Average price: {total_price/num_of_products}')
    print(f'Average weight: {total_weight/num_of_products}')
    print(f'Average flammability: {total_flammability/num_of_products}')

if __name__ == '__main__':
    inventory_report(generate_products())
