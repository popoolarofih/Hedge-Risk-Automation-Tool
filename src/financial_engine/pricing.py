import QuantLib as ql

def price_european_option(spot_price, strike_price, volatility, risk_free_rate, maturity_date, option_type, calculation_date=None):
    """
    Prices a European option using the Black-Scholes model.
    """
    # Set up the market data
    day_count = ql.Actual365Fixed()
    calendar = ql.UnitedStates(ql.UnitedStates.NYSE)
    if calculation_date is None:
        calculation_date = ql.Date.todaysDate()
    ql.Settings.instance().evaluationDate = calculation_date

    # Set up the option
    payoff = ql.PlainVanillaPayoff(option_type, strike_price)
    exercise = ql.EuropeanExercise(maturity_date)
    option = ql.VanillaOption(payoff, exercise)

    # Set up the Black-Scholes process
    spot_handle = ql.QuoteHandle(ql.SimpleQuote(spot_price))
    flat_ts = ql.YieldTermStructureHandle(ql.FlatForward(calculation_date, risk_free_rate, day_count))
    dividend_yield = ql.YieldTermStructureHandle(ql.FlatForward(calculation_date, 0.0, day_count))
    flat_vol_ts = ql.BlackVolTermStructureHandle(ql.BlackConstantVol(calculation_date, calendar, volatility, day_count))
    bsm_process = ql.BlackScholesMertonProcess(spot_handle, dividend_yield, flat_ts, flat_vol_ts)

    # Price the option
    option.setPricingEngine(ql.AnalyticEuropeanEngine(bsm_process))
    price = option.NPV()
    return price
