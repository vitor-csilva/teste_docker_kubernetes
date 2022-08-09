from flask import Flask
import os 

app = Flask(__name__)

#os.environ('TWORPTEST')
#os.environ('PATH')
@app.route("/") ## Endpoint na qual será realizado a requisição
def true_100():
    return os.environ('TWORPTEST') # Retorno da variável TWORPTEST na qual foi declarada no Dockerfile. 

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")