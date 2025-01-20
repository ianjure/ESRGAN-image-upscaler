import torch
import numpy as np
from PIL import Image
from basicsr.archs.rrdbnet_arch import RRDBNet # MODEL
from realesrgan import RealESRGANer # FRAMEWORK

import warnings
warnings.filterwarnings('ignore')

def upscale_image(image):
    model_path = 'RealESRGAN_x4plus.pth' # PARAMETERS

    state_dict = torch.load(model_path, map_location=torch.device('cpu'))['params_ema']

    model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=4)
    model.load_state_dict(state_dict, strict=True)

    upsampler = RealESRGANer(scale=4, model_path=model_path, model=model, tile=0, pre_pad=0, half=True)

    img_array = np.array(image)

    output, _ = upsampler.enhance(img_array, outscale=4)

    output_img = Image.fromarray(output)

    return output_img
