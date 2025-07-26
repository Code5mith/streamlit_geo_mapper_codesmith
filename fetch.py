import requests as rt

def fetch(url):

    try:
        response = rt.get(url)
        serialize_response = response.json()
        print("Network Call!")
        return serialize_response

    except Exception as e:
        print("Network call failed")
        return e
    
