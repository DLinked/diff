from dataclasses import dataclass
from typing import List, Union

import numpy as np

import PIL
from PIL import Image

from ...utils import BaseOutput, is_onnx_available, is_transformers_available


@dataclass
class StableDiffusionPipelineOutput(BaseOutput):
    """
    Output class for Stable Diffusion pipelines.

    Args:
        images (`List[PIL.Image.Image]` or `np.ndarray`)
            List of denoised PIL images of length `batch_size` or numpy array of shape `(batch_size, height, width,
            num_channels)`. PIL images or numpy array present the denoised images of the diffusion pipeline.
    """

    images: Union[List[PIL.Image.Image], np.ndarray]


if is_transformers_available():
    from .pipeline_stable_diffusion import StableDiffusionPipeline
    from .pipeline_stable_diffusion_img2img import StableDiffusionImg2ImgPipeline
    from .pipeline_stable_diffusion_inpaint import StableDiffusionInpaintPipeline

if is_transformers_available() and is_onnx_available():
    from .pipeline_stable_diffusion_onnx import StableDiffusionOnnxPipeline
