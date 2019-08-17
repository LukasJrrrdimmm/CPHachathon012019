import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64
import json


def postMsg(text, intent):
    headers = {
        # Request headers
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": "8cd51b2f9b594164ad87f4d8b88b6d3b"
    }

    params = urllib.parse.urlencode({
        "appId": "8536448d-6aed-4191-98f7-3227cb74f409",
        "versionId": "0.1"
    })
    body = {
        "text": text,
        "intentName": intent
    }
    body = json.dumps(body)
    try:
        conn = http.client.HTTPSConnection(
            'westus.api.cognitive.microsoft.com')
        conn.request("POST", "/luis/api/v2.0/apps/8536448d-6aed-4191-98f7-3227cb74f409/versions/0.1/example?%s" % params,
                     body, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return(data)
    except Exception as e:
        return (e)


print(postMsg("qual é o valor realizado do CAPS PDF até o mês de abril de dois mil e dezenove", "capex"))
