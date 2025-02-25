import http.client
conn = http.client.HTTPSConnection("api.ultramsg.com")
payload = "token=wl9xgibiztm6loex&to=380687400721&body=WhatsApp API on UltraMsg.com works good&priority=10&referenceId="
headers = { 'content-type': "application/x-www-form-urlencoded" }
conn.request("POST", "/instance16/messages/chat", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))