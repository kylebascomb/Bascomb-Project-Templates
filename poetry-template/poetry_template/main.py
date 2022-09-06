import requests

def github_request():
    response = requests.get('https://api.github.com')
    return response

if __name__ == "__main__":
    print(github_request())