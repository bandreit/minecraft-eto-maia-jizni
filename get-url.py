import json
import os


def get_ngrok_url(startswith: str = 'https://') -> str:
    ngrok_tunnels = 'http://localhost:4040/api/tunnels'
    r = os.system(f'curl {ngrok_tunnels} > tunnels.json 2> /dev/null')

    if r != 0:
        os.system('rm -f tunnels.json')
        raise OSError('Either ngrok is not running or curl is not installed.')

    with open('tunnels.json', 'r') as f:
        tunnels = json.loads(f.read())
        os.system('rm -f tunnels.json')

        for tunnel in tunnels['tunnels']:
            if tunnel['public_url'].startswith(startswith):
                return tunnel['public_url'].replace(startswith, '')

print(get_ngrok_url('tcp://'))