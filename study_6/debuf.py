import requests
url = "127.0.0.1:5000/wuliu"
data = {
    "dspt":"T",
    "fsaddress":"山东济南",
    "jsaddress":"甘肃定西"
}
headers = {
    "Content-Type:":"multipart/form-data"
}
res = requests.post(url=url,data=data,headers=headers)

print(res.json())