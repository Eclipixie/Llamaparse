from llama_stack_client import LlamaStackClient

import util

def create_http_client(port: int):
    return LlamaStackClient( base_url=f"http://localhost:{port}" )

def request(client: LlamaStackClient, model:str, sys_msg: str, user_msg: str, verbose: bool=False):
    # req = f"{data}\n\nAnalyse this CSV data with respect to the query on the next line. Do not explain what CSV is or how it works.\n{msg}"
    if (verbose): print(user_msg)
    response = client.inference.chat_completion(
        model_id=model,
        messages=[ 
            { "role": "system", "content": sys_msg },
            { "role": "user", "content": user_msg } 
        ]
    )
    return response
