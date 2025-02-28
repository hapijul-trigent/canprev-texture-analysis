import streamlit as st
import cv2
import numpy as np
from PIL import Image
import tools


# Load
model_bottle_shoulder = tools.load_yolo_model(model_path='models/model_bottle_shoulder.pt')

def panel():

    uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'], key='BottleShoulderTab')

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image = np.array(image)
        
        
        # Create two columns
        col1, col2 = st.columns(2)

        with col1:
            st.header("Uploaded Image")
            image_pil = Image.fromarray(image)
            st.image(image=image, caption='...', use_column_width=True)
        
        with col2:
            
            result_image = tools.detect_shoulder(image, model=model_bottle_shoulder)
            result_image_pil = Image.fromarray(result_image)

            st.header("Detections")
            st.image(result_image_pil, caption='...', use_column_width=True)

