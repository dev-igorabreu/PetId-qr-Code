import os
import json
import qrcode
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Garante que as pastas de armazenamento existam
os.makedirs('data', exist_ok=True)
os.makedirs('static/qrcodes', exist_ok=True)

JSON_FILE = 'data/pets.json'

def carregar_dados():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def salvar_dados(dados):
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    # Coleta de dados do formulário
    pet_id = str(len(carregar_dados()) + 1)
    
    info_pet = {
        'id': pet_id,
        'pet_nome': request.form.get('pet_nome'),
        'pet_idade': request.form.get('pet_idade'),
        'pet_sexo': request.form.get('pet_sexo'),
        'pet_classe': request.form.get('pet_classe'),  # ex: Cão, Gato
        'pet_hostil': request.form.get('pet_hostil'),  # Sim ou Não
        'pet_foto_url': request.form.get('pet_foto_url'),
        'tutor_nome': request.form.get('tutor_nome'),
        'tutor_idade': request.form.get('tutor_idade'),
        'tutor_telefone': request.form.get('tutor_telefone'),
        'tutor_email': request.form.get('tutor_email'),
        'tutor_foto_url': request.form.get('tutor_foto_url')
    }

    # Salva no JSON
    dados = carregar_dados()
    dados[pet_id] = info_pet
    salvar_dados(dados)

    # Gera o link que o QR Code irá abrir
    # Substitua 'http://localhost:5000' pelo seu domínio real ao publicar o projeto
    link_perfil = f"http://localhost:5000/pet/{pet_id}"

    # Gera o QR Code
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(link_perfil)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    qr_filename = f"static/qrcodes/pet_{pet_id}.png"
    img.save(qr_filename)

    return f"<h3>Cadastro realizado com sucesso!</h3><p>QR Code gerado para o pet {info_pet['pet_nome']}:</p><img src='/{qr_filename}'><br><br><a href='/pet/{pet_id}'>Visualizar página do pet</a>"

@app.route('/pet/<pet_id>')
def visualizar_pet(pet_id):
    dados = carregar_dados()
    pet = dados.get(pet_id)
    if not pet:
        return "Pet não encontrado!", 404
    return render_template('pet.html', pet=pet)

if __name__ == '__main__':
    app.run(debug=True)