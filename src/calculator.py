TAX_RATE = 0.08


def calculate_price(base_price: int) -> int:
    """税込価格を計算する（小数点以下切り捨て）"""
    return int(base_price * (1 + TAX_RATE))


def format_price(base_price: int) -> str:
    """価格を日本円形式でフォーマットする"""
    price = calculate_price(base_price)
    return f"{price}円"
