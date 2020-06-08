import urllib.request

def main():
    url = "http://httpbin.org/xml"
    result = urllib.request.urlopen(url)
    # print the status code
    print(f"Result code : {result.status}")
    #printing the header
    print(f"Headers data : {result.getheaders()}")
    # printing  the returned data itself
    # read() will return xml data itself
    # print(f"Returned data : {result.read()}")
    # data we had retrieved is in raw format so
    # we need to decode the data to see it in clear picture as nicely formated
    print(f"Returned data in nicely formated :{result.read().decode('utf-8')}")

if __name__ == "__main__":
    main()
