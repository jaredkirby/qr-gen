import streamlit as st
import qrcode
from io import BytesIO


# Function to generate a QR code
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img


# Function to convert PIL image to bytes for Streamlit display
def convert_image_to_bytes(img, format="PNG"):
    buffered = BytesIO()
    img.save(buffered, format=format)
    buffered.seek(0)
    return buffered


# Function to get image in bytes for downloading
def get_image_download_link(img, file_format="PNG"):
    buffered = BytesIO()
    img.save(buffered, format=file_format)
    return st.download_button(
        label=f"Download QR Code as {file_format}",
        data=buffered.getvalue(),
        file_name=f"qr_code.{file_format.lower()}",
        mime=f"image/{file_format.lower()}",
    )


# Streamlit app
def main():
    st.title("👉 You do it, Randy! 😂")
    st.subheader("QR Code Generator 📲")
    data = st.text_input("Enter URL or Text for QR Code 🪄:")

    if data:
        qr_img = generate_qr_code(data)
        qr_img_bytes = convert_image_to_bytes(qr_img, "PNG")

        # Image format selection and download button moved above the image display
        file_format = st.selectbox(
            "Select Image Format for Download 👇", ["PNG", "JPEG"]
        )
        download_link = get_image_download_link(qr_img, file_format)

        # Display the QR code image
        st.image(qr_img_bytes, caption="Generated QR Code 👍", use_column_width=True)


if __name__ == "__main__":
    main()
