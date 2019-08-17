import http.client, urllib.request, urllib.parse, urllib.error, base64

def postMsg(text,intent):
    headers = {
        # Request headers
        "Content-Type":"application/json",
        "Ocp-Apim-Subscription-Key":"8cd51b2f9b594164ad87f4d8b88b6d3b"
    }

    params = urllib.parse.urlencode({
        "appId":"8536448d-6aed-4191-98f7-3227cb74f409"
        "versionId":"0.1"
    })

    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/luis/api/v2.0/apps/8536448d-6aed-4191-98f7-3227cb74f409/versions/0.1/example?%s" % params,
            # 
        , headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return(data)
    except Exception as e:
        return ("[Errno {0}] {1}".format(e.errno, e.strerror))
