import requests

def main():

    # get username
    username = get_username()
    base_url = f'https://api.github.com/users/{username}/events'

    response = requests.get(base_url)
    if response.status_code == 200:
        all_data = response.json()
        for data in all_data:
            print (f'GitHub User Activity for {username}')
            print("-" * 30)
            print(f"Event type: {data['type']}")
            print(f"Repo: {data['repo']['name']}")
            print(f"Create at: {data['created_at']}")
            print("-" * 30)

    else:
        print (f'Fetch error. {response.status_code}')


def get_username():
    while True:
        try:
            return input("Username: ")
        except TypeError:
            return
            
if __name__ == '__main__':
    main()

