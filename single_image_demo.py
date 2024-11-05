import asyncio
import vertexai
import os
from vertexai.preview.vision_models import ImageGenerationModel
from dotenv import load_dotenv
import time
from utils import vertexai_utils

load_dotenv()  # take environment variables from .env.
PROJECT_ID = os.getenv("PROJECT_ID")

prompt = "doomguy"

async def main():
    # record start time
    start = time.time()

    vertexai.init(project=PROJECT_ID, location="us-central1")
    model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-001")
    image_path = await vertexai_utils.generate_single_image(prompt, model)
    print(image_path)
    
    # record end time
    end = time.time()
    print("The time of execution of above program is :",
      (end-start), "s")

asyncio.run(main())