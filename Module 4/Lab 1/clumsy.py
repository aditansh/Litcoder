import http.client

conn = http.client.HTTPSConnection("judge0-ce.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "57857c65f7mshb52a4a5853d83c3p1287e6jsn61534b268711",
    'X-RapidAPI-Host': "judge0-ce.p.rapidapi.com"
}

conn.request("GET", "/about", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))