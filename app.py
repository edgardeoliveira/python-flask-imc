from flask import Flask, request

app = Flask(__name__)

@app.route('/calcular-imc', methods=['GET'])
def calcular_imc():
    peso = float(request.args.get('peso'))
    altura = float(request.args.get('altura'))
    
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        classificacao = "Magreza"
    elif imc >= 18.5 and imc <= 24.9:
        classificacao = "Normal"
    elif imc >= 25.0 and imc <= 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"
    
    return f"IMC: {imc}, Classificação: {classificacao}"

if __name__ == '__main__':
    app.run(debug=True)