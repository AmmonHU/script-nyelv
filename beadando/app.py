import json
from jsonschema import validate
from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    data = 0
    greenhouse = json.load(open("greenhouse.json", ))

    if 'id' in request.args:
        data = greenhouse[int(request.args["id"])]

    return render_template('index.html', greenhouse=greenhouse, data=data)


@app.route('/add', methods=['POST'])
def record():
    if request.form["temperature"] == "" or request.form["humidity"] == "" or request.form["brightness"] == "" or request.form["time"] == "":
        return "Minden adat megadása kötelező!", 400

    records = json.load(open('greenhouse.json', ))

    record = {
        "id": len(records),
        "temperature": request.form["temperature"],
        "humidity": int(request.form["humidity"]),
        "brightness": int(request.form["brightness"]),
        "time": request.form["time"]
    }

    pattern = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "temperature": {"type": "string"},
            "humidity": {"type": "number"},
            "brightness": {"type": "number"},
            "time": {"type": "string"}
        },
    }

    error = True

    try:
        validate(instance=record, schema=pattern)
        error = False
    except:
        return 'Hiba történt, kérem próbálja újra!', 400

    if not error:
        records.append(record)

        with open("greenhouse.json", "w") as FILE:
            FILE.write(json.dumps(records, indent=2))

    return redirect("/")


if __name__ == "__main__":
    app.run()
