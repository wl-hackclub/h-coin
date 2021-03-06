from flask import Flask
import json
from flask import jsonify
import os

public = Flask(__name__)

if __name__ == "__main__":
    public.run()

public_nodes = {}

#Matthew look here
blockchain = ['nothing']

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + "/nodes.json", "r") as json_file:
    data = json.load(json_file)
    public_nodes = data

@public.route("/nodes")
def return_nodes():
    return json.dumps(public_nodes)

#Matthew Look Here
@public.route("/blockchain", methods=['POST'])
def return_blockchain():
    return jsonify(chain=blockchain)

#Matthew Look Here
@public.route("/blockchain/update", methods=['POSTS'])
def update_blockchain():
    data = request.get_json()
