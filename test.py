from diffusers import DiffusionPipeline
import torch

device = torch.device("cuda" if torch.cuda.is_available else "cpu")
print(device)

pipe = DiffusionPipeline.from_pretrained("black-forest-labs/FLUX.1-dev")
pipe = pipe.to(device)

prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
image = pipe(prompt).images[0]