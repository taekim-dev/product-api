from django.test import TestCase, Client
from products.views import all_products, get_product_by_id
import json


class ProductAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    # all product
    def test_all_products(self):
        response = self.client.get('/api/products/all/')
        self.assertEqual(response.status_code, 200)

    # product by id
    def test_get_product_by_id(self):
        response = self.client.get('/api/products/1/')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertEqual(data["title"], "Wooden Radio")

        response = self.client.get('/api/products/75/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/api/products/145/')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertEqual(data["category"], "Office Products")

        response = self.client.get('/api/products/999/')
        self.assertEqual(response.status_code, 404)

    # product in stock
    def test_get_products_in_stock(self):
        response = self.client.get('/api/products/in-stock/')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertIsInstance(data, dict)
        self.assertIn('products', data)

    # product on discount
    def test_get_products_on_discount(self):
        response = self.client.get('/api/products/discounted/')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertIsInstance(data, dict)
        self.assertIn('products', data)

    # get all categories
    def test_get_all_categories(self):
        response = self.client.get('/api/products/categories/')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertIn("categories", data)
        self.assertGreater(len(data["categories"]), 0)

    # search products by title
    def test_search_products_by_title(self):
        search_query = "Ball"
        response = self.client.get(f'/api/products/search/{search_query}/')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertIn("products", data)

        # Check if all the returned products have the search_query in their title (case-insensitive)
        for product in data["products"]:
            self.assertIn(search_query.lower(), product["title"].lower())

    def test_get_products_by_category(self):
        category_name = "Electronics"
        response = self.client.get(f'/api/products/category/{category_name}/')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertIn("products", data)

        # Check if all the returned products belong to the specified category (case-insensitive)
        for product in data["products"]:
            self.assertEqual(category_name.lower(),
                             product["category"].lower())
