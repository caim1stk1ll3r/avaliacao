from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculadora():  
    if request.method == 'POST':

        nome = request.form.get('nome', '').strip()
        peso = request.form['peso']
        altura = float(request.form['altura'])

        erros = []
        
        imc = float(peso) / float((altura * altura)) 

        if imc < 18.5:
            faixa = "🔵 Abaixo do peso"
        elif imc <= 25:
            faixa = "🟢 Peso normal"
        elif imc <= 30:
            faixa = "🟡 Sobrepeso"
        else:
            faixa = "🔴 Obesidade"

        return render_template('index.html', nome=nome,peso=peso,altura=altura, imc=round(imc, 2), faixa=faixa)

    return render_template('index.html')


@app.route('/equipe')
def equipe():
    return render_template('equipe.html')


































if __name__ == '__main__':
    app.run(debug=True)