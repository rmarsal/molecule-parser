import re
import collections
import flask

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/parse/<path:molecule_string>", methods=["GET"])
def get_molecule_elements(molecule_string):
    molecule_string = molecule_string.replace("[", "(").replace("{", "(").replace("]", ")").replace("}", ")")
    parse = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", molecule_string)
    composition = [collections.Counter()]
    for name, m1, left_open, right_open, m2 in parse:
      if name:
            composition[-1][name] += int(m1 or 1)
      if left_open:
            composition.append(collections.Counter())
      if right_open:
            top = composition.pop()
            for k in top:
                composition[-1][k] += top[k] * int(m2 or 1)
    response = flask.jsonify({"Composition": dict(composition[0].most_common())})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
