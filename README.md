# 🔗 Gerador de QR Code - Python + Streamlit

Um site **simples, direto e funcional** para criar QR Codes **sem data de expiração**.

> ✅ Feito com Python  
> ✅ Interface moderna via Streamlit  
> ✅ Geração instantânea de QR Code  
> ✅ Download em PNG  
> ✅ Sem rastreio, sem tempo limite

---

## 💡 O que é?

Este projeto é uma aplicação web criada em Python que permite:

- Inserir qualquer link
- Gerar um QR Code automaticamente
- Baixar o QR Code como imagem `.png`
- Usar o código gerado para sempre — **ele nunca expira**

---

## 🛠️ Como funciona?

Por trás da interface, usamos:

- [`qrcode`](https://pypi.org/project/qrcode/) – para gerar o QR Code em imagem
- [`Pillow`](https://pypi.org/project/Pillow/) – para manipulação da imagem
- [`Streamlit`](https://streamlit.io) – para a interface web moderna

---

## 🚀 Como usar

1. Acesse o site: [https://qrcodewasabi.streamlit.app/](https://qrcodewasabi.streamlit.app/)
2. Cole o link que deseja transformar em QR Code  
3. Clique em **"Gerar QR Code"**  
4. Visualize e clique em **"Baixar"** para salvar o PNG

---

## 🧱 Rodando localmente

Clone o repositório e instale as dependências:

```bash
pip install -r requirements.txt
streamlit run app.py
