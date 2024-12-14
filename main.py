from gpt4all import GPT4All
from halo import Halo

model = GPT4All("Phi-3-mini-4k-instruct.Q4_0.gguf")
with Halo(text='Processing your files\n', spinner="monkey"):
    print(model.generate("quadratic formula"))