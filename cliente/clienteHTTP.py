import http.client
conn = http.client.HTTPSConnection("www.google.com")
conn.request("HEAD", "/")
res = conn.getresponse()
print(res.status, res.reason, res._method)