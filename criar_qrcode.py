import streamlit as st
import qrcode
from PIL import Image
import io

st.set_page_config(page_title="Gerador de QR Code", page_icon="🔗")

st.title("🔗 Gerador de QR Code para Links")

link = st.text_input("Digite o link que deseja transformar em QR Code:")

if link:
    if st.button("Gerar QR Code"):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Salva em buffer
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)

        # Exibe o QR code
        st.image(buf, caption="Seu QR Code", use_column_width=False)

        # Botão de download
        st.download_button(
            label="📥 Baixar QR Code",
            data=buf,
            file_name="qrcode.png",
            mime="image/png"
        )
