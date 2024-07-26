import requests
import sys

def main():
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))

if __name__ == "__main__":
    main()

