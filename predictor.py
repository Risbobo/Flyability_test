import torch
from torch.utils.data import random_split
from detecto import core, utils, visualize

model = core.Model.load('model_weights.pth', ['probe'])

dataset = core.Dataset('probe_dataset/probe_annotations/', 'probe_dataset/probe_images/')
train, val, test = random_split(dataset, [0.7, 0.1, 0.2], generator=torch.Generator().manual_seed(42))
#print(test[0][0].shape)
#print(len(test[:][0]))

images = [im[0] for im in test]
print(len(images))
prediction = model.predict(images)

labels, boxes, scores = prediction

print(labels)
print(boxes)
print(scores)

#visualize.show_labeled_image(images, boxes, labels)