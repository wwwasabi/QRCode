import streamlit as st
import qrcode
from PIL import Image
import io

st.set_page_config(page_title="Gerador de QR Code", page_icon="🔗")

st.title("🔗 Gerador de QR Code para Links")

# Input do link
link = st.text_input("Digite o link que deseja transformar em QR Code:")

if link:
    # Botão para gerar o QR Code
    if st.button("Gerar QR Code"):
        # Gera o QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Exibe o QR Code
        st.image(img, caption="Seu QR Code", use_column_width=False)

        # Salva em memória para download
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        # Botão de download
        st.download_button(
            label="📥 Baixar QR Code",
            data=byte_im,
            file_name="qrcode.png",
            mime="image/png"
        )
