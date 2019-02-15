#!/usr/bin/env python3

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_product_methods(self):
        """Test product methods `stealability()` and `explode()` methods"""
        prod = Product('Test Product', 4, 10, 0.6)
        self.assertEqual(prod.stealability(), 'Not so stealable...')
        self.assertEqual(prod.explode(), '...fizzle.')


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme reports works"""
    def test_default_num_products(self):
        """Test default number of products"""
        product_list = generate_products()
        self.assertEqual(len(product_list), 30)

        for product in product_list:
            name = product.name
            split_words = name.split(" ")
            self.assertIn(split_words[0], ADJECTIVES)
            self.assertIn(split_words[1], NOUNS)


if __name__ == '__main__':
    unittest.main()
