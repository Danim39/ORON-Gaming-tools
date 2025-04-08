# WireGuard Configuration Generator

import os
import random
import string




def generate_key():
    return os.popen('wg genkey').read().strip()

def generate_ipv4():
    
    return ".".join(f"{random.randint (0, 255)}" for _ in range(4))

def generate_config(private_key, public_key, address, port, dns):
    config = f"""
[Interface]
PrivateKey = {private_key}
Address = {address}
ListenPort = {port}
DNS = {dns}

[Peer]
PublicKey = B/LjUVKQjsjDvdR6PJj8l8/RGsasUUM158ccQibIqH8=
PresharedKey = ZUpHV28xZmhQandlam9pZG5UbEpmdXZNdFFsNElGSDU=
Endpoint = 37.226.40.161:42238
PersistentKeepalive = 25

"""
    return config

def main():
    private_key = generate_key()
    public_key = os.popen(f'echo {private_key} | wg pubkey').read().strip()
    address = f"10.0.0.{random.randint(2, 254)}/24"
    port = random.randint(51820, 65535)

    dns = f'10.202.10.10,{generate_ipv4()}'


    config = generate_config(private_key, public_key, address, port, dns)
    with open(f'name.conf', 'w') as f:
        f.write(config)

if __name__ == "__main__":
    main()
    