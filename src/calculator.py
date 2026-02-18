TAX_RATE = 0.10


def calculate_price(base_price: int) -> int:
    """税込価格を計算する（小数点以下切り捨て）"""
    return int(base_price * (1 + TAX_RATE))


def format_price(base_price: int) -> str:
    """価格を日本円形式でフォーマットする"""
    price = calculate_price(base_price)
    return f"{price}円"


def calculate_bulk_price(base_price: int, quantity: int) -> int:
    """まとめ買い価格を計算する（10個以上で10%割引）"""
    unit_price = calculate_price(base_price)
    discount = 0.9 if quantity >= 10 else 1.0
    return int(unit_price * quantity * discount)
