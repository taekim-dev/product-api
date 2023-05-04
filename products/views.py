import json
import requests
import os
from django.conf import settings
from django.http import JsonResponse

def get_products_fromURL(request):
    url = 'Your_URL'
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def get_products(request):
    file_path = os.path.join(settings.BASE_DIR, 'dummyProducts.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def all_products(request):
    products_data = get_products(request)
    return JsonResponse(products_data, safe=False)

def get_product_by_id(request, product_id):
    products_data = get_products(request)
    product = next((item for item in products_data["products"] if item["id"] == product_id), None)
    if product:
        return JsonResponse(product, safe=False)
    else:
        return JsonResponse({"error": "Product not found"}, status=404)

def get_products_in_stock(request):
    products_data = get_products(request)
    in_stock_products = [product for product in products_data["products"] if product["stock"] > 0]
    return JsonResponse({"products": in_stock_products}, safe=False)

def get_products_on_discount(request):
    products_data = get_products(request)
    on_discount_products = [product for product in products_data["products"] if product["discountPercentage"] > 0]
    return JsonResponse({"products": on_discount_products}, safe=False)

def get_all_categories(request):
    products_data = get_products(request)
    categories = set(product["category"] for product in products_data["products"])
    return JsonResponse({"categories": list(categories)}, safe=False)

def search_products_by_title(request, search_query):
    products_data = get_products(request)
    matching_products = [product for product in products_data["products"] if search_query.lower() in product["title"].lower()]
    return JsonResponse({"products": matching_products}, safe=False)

def get_products_by_category(request, category_name):
    products_data = get_products(request)
    products_by_category = [product for product in products_data["products"] if product["category"].lower() == category_name.lower()]
    return JsonResponse({"products": products_by_category}, safe=False)


