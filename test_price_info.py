import price_info

def test_total_cost_shopping():
    assert price_info.total_cost_shopping() == 46.75

def test_cost_of_fruits():
    assert price_info.cost_of_fruits('apple', 10) == 12.0