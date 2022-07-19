import requests
response_ip = requests.get("http://jsonip.com/").json()
ip = response_ip['ip']

url = "https://ip-location5.p.rapidapi.com/get_geo_info"

payload = "ip="+ip
headers = {
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Key": "7935f117c2msh6e45eee2fce413dp141b6bjsn2b3c6a2b4d51",
    "X-RapidAPI-Host": "ip-location5.p.rapidapi.com"
}

response_location = requests.request(
    "POST", url, data=payload, headers=headers)
location = (response_location.text)
