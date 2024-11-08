from typing import Any, AsyncGenerator, List, Dict
from vertexai.preview.vision_models import ImageGenerationModel
from vertexai.preview.vision_models import ImageGenerationResponse
from vertexai.preview.vision_models import GeneratedImage
from datetime import datetime

async def generate_image(prompt: str, model: ImageGenerationModel) -> ImageGenerationResponse:
    """Generates an image from the given prompt using Vertex AI Imagen 3.0."""
    image = model.generate_images(
        prompt=prompt,
        # Optional parameters
        number_of_images=1,
        language="en",
        # You can't use a seed value and watermark at the same time.
        # add_watermark=False,
        # seed=100,
        aspect_ratio="1:1",
        safety_filter_level="block_some",
        person_generation="allow_adult",
    )
    return image

async def save_image(prompt: List[str], image: GeneratedImage) -> str:
    """Saves the generated image to a file."""
    now = datetime.now()
    now_formatted = now.strftime("%d-%m-%Y %H.%M.%S")
    output_file = f"{prompt}{now_formatted}.png"
    image.save(location=output_file, include_generation_parameters=False)
    return output_file

async def generate_and_save_image(prompt: str, model: ImageGenerationModel) -> Dict[str, str]:
    """Generates an image from the given prompt and saves it to a file."""
    image = await generate_image(prompt, model)
    image_path = await save_image(prompt, image[0])
    return {"prompt": prompt, "image_path": image_path}

async def generate_images(prompts: List[str], model: ImageGenerationModel) -> AsyncGenerator[list, Any]:
    """Generates and saves images for the given list of prompts, and returns a stream of image paths."""
    image_paths = []
    for prompt in prompts:
        result = await generate_and_save_image(prompt, model)
        image_paths.append(result)
        yield image_paths

async def generate_single_image(prompt: str, model: ImageGenerationModel) -> Dict[str, str]:
    """Generates and saves images for the given list of prompts, and returns a stream of image paths."""
    return await generate_and_save_image(prompt, model)