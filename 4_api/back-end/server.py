import json
import sys
from flask_cors import CORS
from flask import Flask
from Operadoras import Operadoras

app = Flask(__name__)
CORS(app)

@app.get("/razao/<corporate_name>")
def operadora_corporate(corporate_name: str):
    exception_base_message = f'[/razao/{corporate_name}]: '
    try:
        entries = Operadoras.find_closest(corporate_name, 'Nome Fantasia')
        json_entries = json.dumps(entries)
        return json_entries
    except LookupError as lookupErr:
        print(exception_base_message, lookupErr, file=sys.stderr)
        return 'Not Found', 404
    except Exception as excp:
        print(exception_base_message, excp, file=sys.stderr)
        return 'Internal Server Error', 500

@app.get("/nome/<commercial_name>")
def operadora_commercial(commercial_name):
    exception_base_message = f'[/razao/{commercial_name}]: '
    try:
        entries = Operadoras.find_closest(commercial_name, 'Nome Fantasia')
        json_entries = json.dumps(entries)
        return json_entries
    except LookupError as lookupErr:
        print(exception_base_message, lookupErr, file=sys.stderr)
        return 'Not Found', 404
    except Exception as excp:
        print(exception_base_message, excp, file=sys.stderr)
        return 'Internal Server Error', 500


csv_name = 'Relatorio_cadop.csv'
try:
    Operadoras.set_singleton(csv_name)
except FileNotFoundError:
    print(f"File `{csv_name}` not found. Aborting server...", file=sys.stderr)
except Exception as err:
    print("An error ocurred while initializing server. Aborting server...", file=sys.stderr)
    print("The error can be found below:", file=sys.stderr)
    print(err, file=sys.stderr)

if __name__ == "__main__":
    app.run(debug=True)
