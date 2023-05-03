import json
import requests
from django.http import JsonResponse

def get_products(request):
    url = 'https://click-and-collect2.s3.amazonaws.com/data/productAll.json'
    response = requests.get(url)
    data = json.loads(response.text)
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
