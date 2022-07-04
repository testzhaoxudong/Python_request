from pprint import pprint

import requests

from hc_api_study_0610.config import *
class HcApi:
    def get_zhuti_api(self):
        url = f"{HOST}{SHOUYE_API_PATH}"
        data ={"page":"1",
               "tab":"share",
               "limit":"1",
               "mdrender":"false"}
        res = requests.get(url=url,data=data)
        return res.json()
    def


if __name__ == '__main__':
    info = HcApi().get_zhuti_api()
    pprint(info)
