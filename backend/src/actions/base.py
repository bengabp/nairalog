from typing import Literal, Dict
from curl_cffi import requests
from pydantic import BaseModel, Field
from src.config import simple_pydantic_model_config


class RateProvider:
    def make_request(
            self,
            url: str,
            params: Dict,
            headers: Dict,
            method: Literal['GET', "POST"] = "GET",
            json_data: Dict = None
    ) -> Dict:
        res = {}
        kwargs = {
            "method": method,
            "url": url,
            "headers": headers,
        }
        if method == "GET":
            kwargs["params"] = params
        elif method == "POST":
            kwargs["json"] = json_data or {}

        try:
            response = requests.request(**kwargs)
            res = response.json()
        except KeyError:
            pass
        return res


    def get_naira_usd_rate(self):
        """ Get the usd naira rate for platform """
        raise NotImplementedError("This method is not implemented")


class Rate(BaseModel):
    model_config = simple_pydantic_model_config

    platform: Literal['bybit', 'grey', 'chipper'] = Field(description="Platform")
    buy_price: float = Field(description="Buy price")
    sell_price: float = Field(description="Sell price")
    is_p2p: bool = Field(description="Is p2p")
