from fastapi import FastAPI
from pydantic import BaseModel
import QuantLib as ql
from src.financial_engine.pricing import price_european_option
import datetime

app = FastAPI()

class OptionRequest(BaseModel):
    spot_price: float
    strike_price: float
    volatility: float
    risk_free_rate: float
    maturity_date: datetime.date
    option_type: str

@app.post("/hedge/price-option")
def get_option_price(request: OptionRequest):
    """
    Prices a European option using the Black-Scholes model.
    """
    option_type_map = {
        "call": ql.Option.Call,
        "put": ql.Option.Put
    }
    option_type = option_type_map.get(request.option_type.lower())
    if option_type is None:
        return {"error": "Invalid option type"}

    maturity_date = ql.Date(request.maturity_date.day, request.maturity_date.month, request.maturity_date.year)
    price = price_european_option(
        request.spot_price,
        request.strike_price,
        request.volatility,
        request.risk_free_rate,
        maturity_date,
        option_type
    )
    return {"price": price}

@app.get("/")
def read_root():
    return {"Hello": "World"}
