import requests

def get_data_from_server(url):
    # Vulnerable: SSL certificate validation is turned off
    response = requests.get(url, verify=False)
    return response.text

# Example usage
url = "https://example.com"
data = get_data_from_server(url)
print(data)

