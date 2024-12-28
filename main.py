
import pandas as pd
import json
import torch
from torch.utils.data import random_split
from detecto import core

with open('probe_dataset/probe_labels.json', 'r') as file:
    data = json.load(file)

annotations = pd.DataFrame(data['annotations'])
annotations.set_index('image_id', inplace=True)

images_info = pd.DataFrame(data['images'])

dataset = core.Dataset('probe_dataset/probe_annotations/', 'probe_dataset/probe_images/')

train, val, test = random_split(dataset, [0.7, 0.1, 0.2], generator=torch.Generator().manual_seed(42))

model = core.Model(['probe'])

history = model.fit(train, val)
print(history)
model.save('model_weights.pth')

