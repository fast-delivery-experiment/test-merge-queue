from calculator import calculate_price


def calculate_bulk_price(base_price: int, quantity: int) -> int:
    """まとめ買い価格を計算する（10個以上で10%割引）"""
    unit_price = calculate_price(base_price)
    discount = 0.9 if quantity >= 10 else 1.0
    return int(unit_price * quantity * discount)
