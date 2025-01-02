from typing import Literal, Dict
from curl_cffi import requests


class RateProvider:

    def make_request(
            self,
            url: str,
            params: Dict,
            headers: Dict,
            method: Literal['GET', "POST"] = "GET"
    ) -> Dict:
        res = {}
        try:
            response = requests.request(method, url=url, params=params, headers=headers)
            res = response.json()
        except KeyError:
            pass
        return res


    def get_naira_usd_rate(self):
        """ Get the usd naira rate for platform """
        raise NotImplementedError("This method is not implemented")

