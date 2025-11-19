def discount(price, category):
    thresholds = {"student": {"limit": 1000, "high": 0.90, "low": 0.95}, "default": {"limit": 2000, "high": 0.85, "low": 1.00}}
    rule = thresholds.get(category, thresholds["default"])
    rate = rule["high"] if price > rule["limit"] else rule["low"]
    return price * rate

price = float(input("Enter price: "))
category = input("Enter category: ")
print(discount(price, category))