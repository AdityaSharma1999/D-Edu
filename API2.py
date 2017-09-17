import http.client
import urllib.error
import urllib.parse
import urllib.request


def run(sentence):
    headers={
        # Request headers. Replace the placeholder key below with your subscription key.
        'Content-Type':'application/json',
        'Ocp-Apim-Subscription-Key':'51885ec0957749399dbc427c9c7f685b',
    }

    params=urllib.parse.urlencode({
    })
    body="{'language': 'en', 'analyzerIds': ['4FA79AF1-F22C-408D-98BB-B7D7AEEF7F04','22A6B758-420F-4745-8A3C-46835A67C0D2'], 'text': '"+sentence+"'}"

    try:
        conn=http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST","/linguistics/v1.0/analyze?%s"%params,body,headers)
        response=conn.getresponse()
        data=response.read()
        #   print(data)
        conn.close()
        return data
    except Exception as e:
        print(e.args)

####################################
