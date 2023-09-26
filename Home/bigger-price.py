def bigger_price(limit, data):
    return sorted(data, key=lambda k: k['price'], reverse=True)[:limit]
