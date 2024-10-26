import requests
from session import MySession


URL = ""

def get_server_public_key() -> str:
    response = requests.post(f'{URL}/api/init-session', json={'client_public_key': 0})
    response.raise_for_status()
    data = response.json()
    return data['server_public_key']

def get_encrypted_challenge() -> str:
    response = requests.post(f'{URL}/api/request-challenge')
    response.raise_for_status()
    data = response.json()
    return data['encrypted_challenge']

def get_encrypted_flag() -> str:
    response = requests.post(
        f'{URL}/api/dashboard',
        json={
            'challenge': sesh.challenge_hash,
            'packet_data': sesh.packet,
        })
    response.raise_for_status()
    data = response.json()
    return data['packet_data']


if __name__ == '__main__':
    sesh = MySession(
        server_public_key=get_server_public_key(),
        encrypted_challenge=get_encrypted_challenge(),
    )
    flag = sesh.decrypt_flag(encrypted_flag=get_encrypted_flag())
    print(flag)
