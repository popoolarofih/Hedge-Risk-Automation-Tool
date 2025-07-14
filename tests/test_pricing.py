import QuantLib as ql
import pytest
from src.financial_engine.pricing import price_european_option

def test_price_european_option():
    # Test case data
    spot_price = 100
    strike_price = 100
    volatility = 0.2
    risk_free_rate = 0.05
    maturity_date = ql.Date(15, 6, 2025)
    option_type = ql.Option.Call
    calculation_date = ql.Date(15, 6, 2024)

    # Price the option
    price = price_european_option(spot_price, strike_price, volatility, risk_free_rate, maturity_date, option_type, calculation_date)

    # Expected price (you can use an online calculator to verify)
    expected_price = 10.45  # Approximate value

    # Assert that the price is close to the expected price
    assert abs(price - expected_price) < 0.1
