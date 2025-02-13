import os
import json
import requests
import sys

from llama_stack_client import LlamaStackClient

def request(server, model, question):
    url = server
    
    headers = { "Content-Type": "application/json" }

    data = {
        "model": model,
        "prompt": question,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if (response.status_code == 200):
        return json.loads(response.text)[response]
    else:
        return f"Request to {server} failed with code {response.status_code}: {response.text}"
    
def create_http_client(server: str, port: int):
    return LlamaStackClient(
        base_url=f"{server}:{int(port)}"
    )
