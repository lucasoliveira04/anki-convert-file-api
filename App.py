from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import genanki
import json
import os

app = Flask(__name__)
CORS(app)

@app.route('/convert', methods=['POST'])
def convert_to_apkg():
    try:
        # Recebe o JSON enviado pelo cliente com o nome do deck e os cartões
        data = request.get_json()

        # Extraindo informações do JSON
        deck_name = data["deckName"]
        cards = data["cards"]

        # Criando o modelo de cartão Anki
        model = genanki.Model(
            1607392319,  # ID único do modelo
            "Modelo Simples",  # Nome do modelo
            fields=[{"name": "Frente"}, {"name": "Verso"}],  # Definindo os campos
            templates=[{
                "name": "Cartão Simples",
                "qfmt": "{{Frente}}",  # Formato da frente do cartão
                "afmt": "{{FrontSide}}<hr id='answer'>{{Verso}}",  # Formato do verso
            }]
        )

        # Criando o deck Anki
        deck = genanki.Deck(
            hash(deck_name) % (2**31),  # Gerando um ID único para o deck
            deck_name  # Nome do deck
        )

        # Adicionando os cartões ao deck
        for card in cards:
            note = genanki.Note(
                model=model,
                fields=[card["front"], card["back"]]  # Preenchendo os campos do cartão
            )
            deck.add_note(note)

        # Gerando o arquivo .apkg
        output_file = f"{deck_name}.apkg"
        genanki.Package(deck).write_to_file(output_file)

        # Enviando o arquivo gerado para o cliente com o nome correto
        return send_file(
            output_file,
            as_attachment=True,
            download_name=f"{deck_name}.apkg",  # Nome do arquivo a ser baixado
            mimetype="application/octet-stream"  # Tipo MIME do arquivo
        )

    except Exception as e:
        # Retorna erro caso algo falhe
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # Rodando o servidor Flask na porta 5000
    app.run(debug=True, port=5000)
