import json

def loadSecrets(filePath: str) -> dict :
    # load the file and parse it into dictionary
    with open(filePath) as secrets_file:
        secret_data = json.load(secrets_file)
        return secret_data
