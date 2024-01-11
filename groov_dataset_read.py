import json

with open("./AmazonCat-13K_train.json", "r") as file:
    print(json.dumps(json.loads(file.readline()), indent=4))