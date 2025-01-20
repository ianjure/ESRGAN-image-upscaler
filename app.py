import streamlit as st
from PIL import Image
from utils import upscale_image

st.title('ESRGAN Image Upscaler')

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
upscale_button = st.button('Upscale Image')

if uploaded_file is not None and upscale_button:
    image = Image.open(uploaded_file).convert('RGB')
    final_image = upscale_image(image)

    original_img, final_img = st.columns(2)

    with original_img:
        st.image(image, caption='Original Image', use_column_width=True)
    with final_img:
        st.image(final_image, caption='Upscaled Image', use_column_width=True)
    