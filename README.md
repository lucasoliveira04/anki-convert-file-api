# API de Conversão para Anki (.apkg)

### Visão Geral

Esta API recebe um conjunto de flashcards no formato JSON e os converte para um arquivo `.apkg` compatível com o Anki.

### URL Base
```prompt
https://anki-convert-file-api.onrender.com
```
---
**Endpoints**
### 1. Converter Flashcards para `.apkg`
```prompt
POST /convert
```
**Descrição**: Converte um conjunto de flashcards em um deck do Anki (`.apkg`) e retorna o arquivo gerado para download.

**Parâmetros da Requisição**:
```json
{
  "deckName": "Meu Deck de Estudo",
  "cards": [
    {
      "front": "O que é Flask?",
      "back": "Um microframework web para Python."
    },
    {
      "front": "O que é Anki?",
      "back": "Um software de repetição espaçada para memorização."
    }
  ]
}

```
**Resposta de Sucesso (200 OK)**:
- Retorna um arquivo `.apkg` para download.

**Possíveis Erros:**
- **400 Bad Request**: Se o JSON enviado estiver mal formatado ou faltar campos obrigatórios.
- **500 Internal Server Error:** Se ocorrer um erro inesperado na geração do arquivo.
