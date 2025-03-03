import requests

def trace_redirects(url):
    # Send a GET request to the URL and follow redirects
    response = requests.get(url, allow_redirects=True)
    
    # Initialize a list to store the hops (redirects)
    hops = [response.url]  # Start with the initial URL

    # If there were any redirects, capture each hop
    for resp in response.history:
        hops.append(resp.url)  # Add each redirect URL to the hops list

    # Print all hops
    print("Redirect hops:")
    for hop in hops:
        print(hop)

# Example usage
url = "https://tivikoh.com/playlist/B329.m3u"
trace_redirects(url)
