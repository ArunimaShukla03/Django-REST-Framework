import requests
'''
#"endpoint" in terms of an API client is like a URL.

# FOR EXAMPLE: When I type in "https://www.github.com", my web browser sends in a request to the github server and it returned an HTML document. THIS IS NOT AN API ENDPOINT.

endpoint = "https://httpbin.org/anything"

 # get_response = requests.get(endpoint) where endpoint = "https://httpbin.org".
 
 # API (Application Programming Interface): here using the "requests" library is a form of using an API. In this we are assigning the get_response to the result we get when we type in the request for the endpoint. This is an HTTP request.

# These are not "REST APIs". These are "library APIs" which are basically set of functions or methods that can be used by other software applications to perform a specific task.

# REST APIs can be thought of as "Web APIs" as they recieve in requests and send responses over the web.

# Python requests perform HTTP requests that we are trying to do.

# print(get_response.text) prints source code or prints the raw text response. When we type in "python py_client/basic.py", it gets the source code of "https://httpbin.org". This is a normal HTTP request.

get_response = requests.get(endpoint)

print(get_response.text) # We can use what it returns back for my python application.

# While an HTTP Request sends back an HTML page, a REST API HTTP Request returns an JSON or an XML file. While HTTP Request is something that humans can look at but a REST API HTTP Request is meant for softwares to communicate with each other over the internet.print(get_response.text).

# (JSON) JavaScript Object Notation ~ Python Dictionary

print(get_response.json()) # "get_response.json()" is a method that is used to convert the response data from the API (which is typically in JSON format) into a Python dictionary object.

# In python requests libraries, we can pass in our own JSON data.

get_response = requests.get(endpoint, json={"query":"Hello World"}) 

print(get_response.json()) # We will find that it echos data that we sent to it in a python dictionary format.

# A web browser client, which is a way to interact over the internet while Python API client is used to interact with an API using python code.

# Thus we can say that this py_client has nothing to do with the django-rest-framework(it is used to build API) and django or python on the backend. 

print(get_response.status_code) # 200 means success.

'''

endpoint = "http://localhost:8000/" # This endpoint is based off of Django.

get_response = requests.get(endpoint)

print(get_response.text)

print(get_response.status_code)