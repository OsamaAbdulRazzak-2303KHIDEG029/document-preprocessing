import requests
import json
import os

API_KEY = "llx-h1i19WInubxNtdmxQRoNYunacafCmusPpxrpvMQk84yCGrx0"
url = "https://api.cloud.llamaindex.ai/api/v2alpha1/parse/upload"

headers = {"Authorization": f"Bearer {API_KEY}"}

files = {
    "file": open(
        "monthwise_file_data/Islamic Fund Manager Report – November 2025.pdf", "rb"
    )
}

configuration = {
    "parse_options": {
        "tier": "agentic",
        "version": "latest",
        "result_type": "markdown",
    }
}

data = {"configuration": json.dumps(configuration)}

response = requests.post(url, headers=headers, files=files, data=data)

print(response.status_code)
print(response.json())
