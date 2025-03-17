from llama_stack_client import LlamaStackClient

import util

def create_http_client(port: int):
    return LlamaStackClient( base_url=f"http://localhost:{port}" )

def request(client: LlamaStackClient, msg: str, data: str, verbose: bool=False):
    req = f"{data}\n\nAnalyse this CSV data with respect to the query on the next line. Do not explain what CSV is or how it works.\n{msg}"
    util.log(req, verbose)
    response = client.inference.chat_completion(
        model_id="meta-llama/Llama-3.2-3B-Instruct",
        messages=[ { "role": "user", "content": req } ]
    )
    return response
