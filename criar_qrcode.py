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

        st.image(img, caption="Seu QR Code", use_column_width=False)

        buf = io.BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="📥 Baixar QR Code",
            data=byte_im,
            file_name="qrcode.png",
            mime="image/png"
        )