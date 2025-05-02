# import requests

# def get_current_stock(product_name: str) -> int:
#     res = requests.get(f"http://warehouse-service/api/stock/{product_name}/")
#     if res.status_code == 200:
#         return res.json().get('current_stock', 0)
#     return 0
