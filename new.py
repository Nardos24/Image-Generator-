import streamlit as st
from diffusers import StableDiffusionPipeline
from diffusers import EulerDiscreteScheduler
from PIL import Image
import torch

st.title("Stable Diffusion Image Generator")
st.markdown("""
<style>
.st-emotion-cache-w3nhqi.ef3psqc5

{
    visibility: hidden;
}
</style>

""", unsafe_allow_html= True)
st.markdown(
    f"""
        <style>
        .stApp {{
            background-image: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1350&q=80");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Load the model
generated_image = None
model_id = "stabilityai/stable-diffusion-2"
scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float32)

# Option to load from CPU or GPU 
use_gpu = st.checkbox("Use GPU (if available)")
if use_gpu and torch.cuda.is_available():
  pipe = pipe.to("cuda")
else:
  pipe = pipe.to("cpu")

# Text prompt
prompt = st.text_input("Enter your text prompt:")

# Upload image (optional)
uploaded_image = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])
# Generate Image
if st.button("Generate"):
  with st.spinner("Generating image..."):
    # Progress bar
    progress_bar = st.progress(0)
    if uploaded_image is not None:
      image = Image.open(uploaded_image)
      # Use the image as a starting point for the generation
      generated_image = pipe(prompt=prompt, init_image=image).images[0]
    else:
      generated_image = pipe(prompt=prompt).images[0]
    
    # Display the generated image
    st.image(generated_image, caption="Generated Image", use_column_width=True)

# Save the generated image (optional)
  if generated_image is not None:
    st.write("If you want to download the generated image click the button below")
    st.download_button("Download Image", generated_image, file_name="generated_image.png", mime="image/png")
