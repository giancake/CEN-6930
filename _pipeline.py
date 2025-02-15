import argparse
import requests
import json
import os
import time

def load_config():
    """
    Load config file looking into multiple locations
    """
    config_locations = [
        "./_config",
        "prompt-eng/_config",
        "../_config"
    ]
    
    # Find CONFIG
    config_path = None
    for location in config_locations:
        if os.path.exists(location):
            config_path = location
            break
    
    if not config_path:
        raise FileNotFoundError("Configuration file not found in any of the expected locations.")
    
    # Load CONFIG
    with open(config_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()


def create_payload(model, prompt, target="ollama", **kwargs):
    """
    Create the Request Payload in the format required byt the Model Server
    @NOTE: 
    Need to adjust here to support multiple target formats
    target can be only ('ollama' or 'open-webui')

    @TODO it should be able to self_discover the target Model Server
    [Issue 1](https://github.com/genilab-fau/prompt-eng/issues/1)
    """

    payload = None
    if target == "ollama":
        payload = {
            "model": model,
            "prompt": prompt, 
            "stream": False,
        }
        if kwargs:
            payload["options"] = {key: value for key, value in kwargs.items()}

    elif target == "open-webui":
        '''
        @TODO need to verify the forma for 'parameters' for 'open-webui' is correct.
        [Issue 2](https://github.com/genilab-fau/prompt-eng/issues/2)
        '''
        payload = {
            "model": model,
            "messages": [ {"role" : "user", "content": prompt } ]
        }

        # payload.upload({key: value for key, value in kwargs.items()})
        payload.update({key: value for key, value in kwargs.items()})

    
    else:
        print(f'!!ERROR!! Unknown target: {target}')
    return payload


def model_req(payload=None):
    """
    Issue request to the Model Server
    """
        
    # CUT-SHORT Condition
    try:
        load_config()
    except:
        return -1, f"!!ERROR!! Problem loading prompt-eng/_config"

    url = os.getenv('URL_GENERATE', None)
    api_key = os.getenv('API_KEY', None)
    delta = response = None

    headers = dict()
    headers["Content-Type"] = "application/json"
    if api_key: headers["Authorization"] = f"Bearer {api_key}"

    #print(url, headers)
    #print(payload)

    # Send out request to Model Provider
    try:
        start_time = time.time()
        response = requests.post(url, data=json.dumps(payload) if payload else None, headers=headers)
        delta = time.time() - start_time
    except:
        return -1, f"!!ERROR!! Request failed! You need to adjust prompt-eng/config with URL({url})"

    # Checking the response and extracting the 'response' field
    if response is None:
        return -1, f"!!ERROR!! There was no response (?)"
    elif response.status_code == 200:

        ## @NOTE: Need to adjust here to support multiple response formats
        result = ""
        delta = round(delta, 3)

        response_json = response.json()
        if 'response' in response_json: ## ollama
            result = response_json['response']
        elif 'choices' in response_json: ## open-webui
            result = response_json['choices'][0]['message']['content']
        else:
            result = response_json 
        
        return delta, result
    elif response.status_code == 401:
        return -1, f"!!ERROR!! Authentication issue. You need to adjust prompt-eng/config with API_KEY ({url})"
    else:
        return -1, f"!!ERROR!! HTTP Response={response.status_code}, {response.text}"
    return

###
### DEBUG
###

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the model pipeline")
    parser.add_argument("prompt", type=str, default="1+1", nargs='?', help="The prompt to be used")
    parser.add_argument("target", choices=["ollama-local", "ollama-remote", "open-webui"], default="open-webui", nargs='?', help="The target to be used") 
    parser.add_argument("model", type=str, default="phi4:latest", nargs='?', help="The model name to be used")
    parser.add_argument("system_instructions", type=str, default="Act like you are a math teacher\nYour student is asking:", nargs='?', help='System instruction to be used')
    parser.add_argument("format_response", type=str, default="give a super detailed answer", nargs='?', help='format response')
    args=parser.parse_args()
    
    from _pipeline import create_payload, model_req
    
    MESSAGE = args.prompt
    TARGET= args.target
    MODEL = args.model
    TEMPLATE_BEFORE = args.system_instructions
    TEMPLATE_AFTER = args.format_response
    PROMPT = TEMPLATE_BEFORE + '\n' + MESSAGE + '\n' + TEMPLATE_AFTER

    payload=create_payload(
                        target=TARGET,
                        model=MODEL,
                        prompt=PROMPT,
                        temperature=1.0,
                        num_ctx=100,
                        num_predict=100)

    time, response = model_req(payload=payload)
    print(response)
    if time: print(f'Time taken: {time}s')