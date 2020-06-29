import requests


def bufar():
    r = requests.get('https://api-v3.mbta.com/routes/?filter[type]=0,1&fields[route]=long_name')
    print(f'{r.status_code=}')
    print(r.headers)
    print(f'{r.encoding=}')
    print(r.text)

    obj = r.json()
    for x in obj['data']:
        print(f"{x['id']} : {x['attributes']['long_name']}")


if __name__ == '__main__':
    bufar()