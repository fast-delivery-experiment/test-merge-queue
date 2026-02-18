from bulk_discount import calculate_bulk_price


class TestCalculateBulkPrice:
    def test_no_discount_under_10(self):
        # 1000円 × 税率10% = 1100円、5個 → 5500円
        assert calculate_bulk_price(1000, 5) == 5500

    def test_10_percent_discount_over_10(self):
        # 1000円 × 税率10% = 1100円、10個 × 0.9 = 9900円
        assert calculate_bulk_price(1000, 10) == 9900
