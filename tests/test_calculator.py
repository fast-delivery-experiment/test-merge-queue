from calculator import calculate_bulk_price, calculate_price, format_price


class TestCalculatePrice:
    def test_calculate_tax_included_price(self):
        assert calculate_price(1000) == 1100

    def test_truncate_decimal(self):
        assert calculate_price(999) == 1098


class TestFormatPrice:
    def test_format_as_yen(self):
        assert format_price(1000) == "1100円"


class TestCalculateBulkPrice:
    def test_no_discount_under_10(self):
        # 1000円 × 税率10% = 1100円、5個 → 5500円
        assert calculate_bulk_price(1000, 5) == 5500

    def test_10_percent_discount_over_10(self):
        # 1000円 × 税率10% = 1100円、10個 × 0.9 = 9900円
        assert calculate_bulk_price(1000, 10) == 9900
