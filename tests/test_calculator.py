from calculator import calculate_price, format_price


class TestCalculatePrice:
    def test_calculate_tax_included_price(self):
        assert calculate_price(1000) == 1100

    def test_truncate_decimal(self):
        assert calculate_price(999) == 1098


class TestFormatPrice:
    def test_format_as_yen(self):
        assert format_price(1000) == "1100円"
