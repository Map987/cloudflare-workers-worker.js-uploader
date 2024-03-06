import requests
import json
import time

account_identifier = ''
service_name = ''
cf_token = ''

# 
with open("/storage/emulated/0/Download/worker.js", "r") as file:
    data = file.read()

# 
delimiter = "----WebKitFormBoundary" + hex(int(time.time() * 1000))

# 
body = f"--{delimiter}\r\nContent-Disposition: form-data; name=\"worker\"; filename=\"test.js\"\r\n\r\n{data}\r\n"
body += f"--{delimiter}\r\nContent-Disposition: form-data; name=\"metadata\"\r\n\r\n{{\"body_part\":\"worker\"}}\r\n"
body += f"--{delimiter}--\r\n"

headers = {
    "Authorization": f"Bearer {cf_token}",
    "Content-Type": f"multipart/form-data; boundary={delimiter}"
}

# 
response = requests.put(
    f"https://api.cloudflare.com/client/v4/accounts/{account_identifier}/workers/services/{service_name}/environments/production/content",
    headers=headers,
    data=body.encode()
)

# 检查
if response.status_code == 200:
    print("Upload successful.")
    print(response.text)
else:
    print("Upload failed.")
    print(response.text)
    
    
    
   
