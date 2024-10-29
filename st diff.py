from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
import torch
import matplotlib.pyplot as plt
from PIL import Image
import os
# Model and scheduler setup (same as before)
model_id = "stabilityai/stable-diffusion-2" 
scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float32)
pipe = pipe.to("cpu")

# Load your input image
input_image = Image.open("C:/Users/hp/Downloads/my dubai.jpg")
     
# Generate the image with image-to-image
prompt = "A beautiful girl"  # You can still use a text prompt
generated_image = pipe(prompt=prompt, init_image=input_image).images[0]

# Save and display the generated image
generated_image.save("generated_image.png")
plt.imshow(generated_image)
plt.show()
