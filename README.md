# Stable Diffusion Image Generator
This Streamlit app lets you create stunning images using the power of Stable Diffusion. You can generate images from text prompts, upload an existing image for image-to-image generation, or combine both!

## Features

- **Text-to-Image:** Enter a text description, and the app will generate an image based on your words. 
- **Image-to-Image:** Upload an image, and the app will create variations or modifications based on your prompt.
- **Combined Prompts:** Use both text and image prompts to achieve even more creative results.

## Getting Started

1. **Install Dependencies:**
  
bash
  pip install -r requirements.txt
  ```

2. **Run the App:**
  
  streamlit run app.py
  

3. **Access the App:**
  The app will be available in your browser at the provided URL.

## Usage

1. Text Prompt: Enter your text description in the "Text Prompt" field. 
2. Image Upload: Optionally, upload an image to use as a starting point for image-to-image generation.
3. Generate: Click the "Generate Image" button.

## Requirements

- Python 3.7 or higher
- Streamlit
- Diffusers
- Transformers
- PIL
- torch

## Dependencies

The requirements.txt file contains all the necessary dependencies for this app.

## Example Prompts

- Text-to-Image:
  - "A futuristic cityscape with flying cars"
  - "A portrait of a cat wearing a top hat"
  - "A surreal landscape with melting clocks"
- Image-to-Image:
  - Upload a photo of a cat and prompt: "The cat wearing a superhero costume"
  - Upload a landscape photo and prompt: "The landscape painted in vibrant colors"

## Note

- The app uses the Stable Diffusion model, which is a powerful generative model. The quality of the generated images depends on the prompt and the model's training data.
- Feel free to experiment with different prompts and images to see the amazing results Stable Diffusion can achieve.
