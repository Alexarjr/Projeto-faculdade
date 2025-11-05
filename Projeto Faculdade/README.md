# 🎲 QR Sorteio

Um sistema simples de sorteio onde as pessoas se inscrevem escaneando um QR Code e digitando o nome.  
Desenvolvido em **Python + FastAPI**, salva os nomes em um arquivo JSON e gera a ordem sorteada.

---

## 🚀 Funcionalidades

- Página de cadastro acessível via QR Code
- Armazena nomes em `participants.json`
- Página `/draw` embaralha os nomes e mostra a ordem do sorteio

---

## 🧩 Estrutura do Projeto

```
qr_sorteio/
├── main.py
├── participants.json
├── requirements.txt
├── README.md
└── static/
    └── index.html
```

---

## 🖥️ Como rodar localmente

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```

3. Acesse no navegador:
   ```
   http://127.0.0.1:8000
   ```

4. Acesse `/draw` para ver o resultado do sorteio:
   ```
   http://127.0.0.1:8000/draw
   ```

---

## ☁️ Como hospedar no Render

1. Faça login em [https://render.com](https://render.com)
2. Crie um novo Web Service e conecte seu repositório GitHub
3. Use as seguintes configurações:
   - **Build Command:**
     ```
     pip install -r requirements.txt
     ```
   - **Start Command:**
     ```
     uvicorn main:app --host 0.0.0.0 --port $PORT
     ```
4. Clique em **Create Web Service**
5. Após o deploy, acesse o link gerado (exemplo):
   ```
   https://qr-sorteio.onrender.com
   ```

---

## 🧠 Exemplo de uso

- Gere um QR Code apontando para a URL do seu site (exemplo: `https://qr-sorteio.onrender.com`)
- Cada pessoa acessa, digita o nome e confirma.
- Depois, acesse `/draw` para ver a ordem sorteada!

---

Feito com ❤️ em FastAPI.
