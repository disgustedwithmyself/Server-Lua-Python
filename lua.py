import requests

print(requests.post("http://127.0.0.1:5000/api", json={
    "name": "liztochek_code",
    "uuid": "99999",
    "password": "afh27fa9g72",
    "processor": "amd-ryzen 3500",
    "video-card": "GeForce RTX 3050",
    "ip": "localhost"
        }).text)
