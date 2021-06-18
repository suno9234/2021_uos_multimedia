import torch
import numpy as np
from PIL import Image
import numpy as np

import matplotlib.pyplot as plt
import torch

from torch.utils.data import Dataset,DataLoader
import torchvision
from torchvision import datasets ,transforms

seq_model = torch.load("resultsmodel.pt")

trans = transforms.Compose([transforms.Resize((100,100)),
                            transforms.ToTensor(),
                            transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))])


img_path = "data\\test"
trainSet = torchvision.datasets.ImageFolder(root=img_path, transform=trans)

item = trainSet.__getitem__(0)
print(type(item[0]))
print(seq_model(item[0]))