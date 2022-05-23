# -*- coding: utf8 -*-
import requests

url = "https://www.pttime.org/attendance.php"
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
'cookie': 'c_secure_uid=OTgyOA==; c_secure_pass=5b80506648747b4c42565d12faabeeaf; c_secure_ssl=eWVhaA==; c_secure_tracker_ssl=eWVhaA==; c_secure_login=bm9wZQ=='
}

response = requests.post(url, headers=headers)

print(response.text)
