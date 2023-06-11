import requests

url = "https://bahoqdqx2lbikl43po5525wljy0wmphu.lambda-url.us-east-1.on.aws/"  # Replace with your target URL
payload = "<html><body><h1>Custom HTML POST Request</h1></body></html>"  # Replace with your custom HTML payload

response = requests.post(url, data=payload)

print(response)  # Print the response from the server