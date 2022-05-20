

from urlrequest import UrlRequest

if __name__ == '__main__':
    response = UrlRequest('https://httpbin.org/ip')
    print(response.text)
    print(response.status_code)
    print(response.headers)
    print(response.json)

    response = UrlRequest("https://httpbin.org/basic-auth/user/password",auth=('user','password'))
    print(response.text)

    response = UrlRequest("https://httpbin.org/post",method="POST",json={"hello":"world"})
    print(response.text)

    response = UrlRequest("https://httpbin.org/image/png")
    with open("test.png","wb") as f:
        f.write(response.raw)
    print(response.status_code)

    # drop in for requests
    response = UrlRequest.get("https://httpbin.org/headers",headers={"hello":"world header test"})
    print(response.text)