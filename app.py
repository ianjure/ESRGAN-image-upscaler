import streamlit as st
from PIL import Image
from utils import upscale_image

st.title('ESRGAN Image Upscaler')
st.write('Upload an image to upscale it using **Enhanced Super-Resolution Generative Adversarial Networks**.')

uploaded_file = st.file_uploader('Choose an image', type=['jpg', 'png'])

col1, col2, col3 = st.columns(3)
with col2:
    upscale_button = st.button('Upscale Image', use_container_width=True)

if uploaded_file is not None and upscale_button:
    image = Image.open(uploaded_file).convert('RGB')
    final_image = upscale_image(image)

    original_img, final_img = st.columns(2)
    with original_img:
        st.image(image, caption='Original Image', use_container_width=True)
    with final_img:
        st.image(final_image, caption='Upscaled Image', use_container_width=True)
    