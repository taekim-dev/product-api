# ProductAPI

A simple RESTful API built with Django, which provides access to product data.

## Live Demo

This ProductAPI is used as a backend for the portfolio website 'Click and Collect'. You can visit the live demo [here](https://click-and-collect2.netlify.app).

## API Endpoints

The following API endpoints are supported:

- `GET /api/products/all/`: Retrieve all products.
- `GET /api/products/<product_id>/`: Retrieve a specific product by its ID.
- `GET /api/products/in-stock/`: Retrieve all products that are in stock (stock > 0).
- `GET /api/products/on-discount/`: Retrieve all products that have a discount percentage greater than 0.
- `GET /api/products/categories/`: Get all available categories.
- `GET /api/products/search/{search_query}/`: Search products by title.
- `GET /api/products/category/{category_name}/`: Retrieve all products in the specified category.

## Setup

1. Clone the repository
2. Install the required dependencies
3. Run the Django server

## Configuration

In order to use the live version of the ProductAPI, the developer needs to configure the actual URL for the JSON data. The current setup uses a `dummyProducts.json` file for development purposes. Replace the contents of the `dummyProducts.json` file with the actual data, or update the `get_products` function in `views.py` to fetch data from the actual URL.
