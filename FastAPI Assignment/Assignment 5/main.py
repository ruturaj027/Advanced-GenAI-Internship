from fastapi import FastAPI, Query

app = FastAPI()

products = [
    {"id": 1, "name": "Wireless Mouse", "category": "Electronics", "price": 499},
    {"id": 2, "name": "Notebook", "category": "Stationery", "price": 99},
    {"id": 3, "name": "USB Hub", "category": "Electronics", "price": 799},
    {"id": 4, "name": "Pen Set", "category": "Stationery", "price": 49}
]

orders = []
cart = []


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Store"}

@app.get("/products")
def get_products():
    return {"products": products}


@app.post("/products")
def add_product(product: dict):
    products.append(product)
    return {"message": "Product added", "product": product}



@app.get("/products/search")
def search_products(keyword: str = Query(...)):
    result = [p for p in products if keyword.lower() in p["name"].lower()]

    if not result:
        return {"message": f"No products found for: {keyword}", "products": []}

    return {
        "keyword": keyword,
        "total_found": len(result),
        "products": result
    }


@app.get("/products/sort")
def sort_products(
    sort_by: str = Query("price"),
    order: str = Query("asc")
):
    if sort_by not in ["price", "name"]:
        return {"error": "sort_by must be 'price' or 'name'"}

    reverse = True if order == "desc" else False

    sorted_data = sorted(products, key=lambda p: p[sort_by], reverse=reverse)

    return {
        "sort_by": sort_by,
        "order": order,
        "products": sorted_data
    }



@app.get("/products/page")
def paginate_products(
    page: int = Query(1),
    limit: int = Query(2)
):
    start = (page - 1) * limit
    end = start + limit

    total = len(products)
    total_pages = -(-total // limit)

    return {
        "page": page,
        "limit": limit,
        "total_pages": total_pages,
        "products": products[start:end]
    }


@app.get("/orders/search")
def search_orders(customer_name: str = Query(...)):
    result = [o for o in orders if customer_name.lower() in o["customer_name"].lower()]

    if not result:
        return {"message": f"No orders found for: {customer_name}", "orders": []}

    return {
        "customer_name": customer_name,
        "total_found": len(result),
        "orders": result
    }



@app.get("/products/sort-by-category")
def sort_by_category():
    sorted_products = sorted(products, key=lambda p: (p["category"], p["price"]))
    return {"products": sorted_products}


@app.get("/products/browse")
def browse_products(
    keyword: str = Query(None),
    sort_by: str = Query("price"),
    order: str = Query("asc"),
    page: int = Query(1),
    limit: int = Query(4)
):
    result = products

    if keyword:
        result = [p for p in result if keyword.lower() in p["name"].lower()]

  
    if sort_by not in ["price", "name"]:
        return {"error": "sort_by must be 'price' or 'name'"}

    reverse = True if order == "desc" else False
    result = sorted(result, key=lambda p: p[sort_by], reverse=reverse)

    # Pagination
    total = len(result)
    start = (page - 1) * limit
    end = start + limit

    return {
        "keyword": keyword,
        "sort_by": sort_by,
        "order": order,
        "page": page,
        "limit": limit,
        "total_found": total,
        "total_pages": -(-total // limit),
        "products": result[start:end]
    }



@app.post("/orders")
def place_order(order: dict):
    order["order_id"] = len(orders) + 1
    orders.append(order)
    return {"message": "Order placed", "order": order}

@app.get("/orders")
def get_orders():
    return {"orders": orders}


@app.get("/orders/page")
def paginate_orders(
    page: int = Query(1),
    limit: int = Query(3)
):
    start = (page - 1) * limit
    end = start + limit

    total = len(orders)
    total_pages = -(-total // limit)

    return {
        "page": page,
        "limit": limit,
        "total_pages": total_pages,
        "orders": orders[start:end]
    }
