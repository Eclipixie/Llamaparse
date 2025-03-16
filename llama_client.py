import os
import json
import requests
import sys

from llama_stack_client import LlamaStackClient

def create_http_client(port: int):
    return LlamaStackClient( base_url=f"http://localhost:{port}" )

def request(client: LlamaStackClient, msg: str):
    response = client.inference.chat_completion(
        model_id="meta-llama/Llama-3.2-3B-Instruct",
        messages=[ { "role": "user", "content": msg } ]
    )
    print(response)
