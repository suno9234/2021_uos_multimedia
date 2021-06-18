from PIL import Image
from torch import nn,optim
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import reshape, shape
import torch

from torch.utils.data import Dataset,DataLoader
import torchvision
from torchvision import datasets ,transforms

print("start")

trans = transforms.Compose([transforms.Resize((100,100)),
                            transforms.ToTensor(),
                            transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))])


img_path = "data\imgs\img_copy"
trainSet = torchvision.datasets.ImageFolder(root=img_path, transform=trans)

trainloader = DataLoader(
    dataset=trainSet,
    batch_size=1,
    shuffle=True,
    num_workers=0
)

def train():
    net = nn.Sequential(
        nn.Linear(30000,300),
        nn.LeakyReLU(),
        nn.Linear(300,30),
        nn.LeakyReLU(),
        nn.Linear(30,10),
        nn.LeakyReLU(),
        nn.Linear(10,1)

    )
    loss_fn = nn.MSELoss()
    optimizer = optim.Adagrad(net.parameters(),lr=0.25)
    total_epochs=200
    for epoch in range(total_epochs+1):
        for i, data in enumerate(trainloader):
            x_train, y_train = data
            
            x_train = x_train.to(torch.float32)
            x_train = reshape(x_train,[-1])
            y_train = y_train.to(torch.float32)

            prediction = net(x_train)
            loss = loss_fn(prediction,y_train)
            optimizer.zero_grad()
            
            loss.backward()
            optimizer.step()
            
            if epoch % 10 ==0 :
                print('Epoch {:4d}/{} Batch {}/{} loss : {:.6f}'.format(epoch, total_epochs, i+1, len(trainloader),
                    loss.item()))
    path = "results"
    torch.save(net,path+"model3.pt")
train()

print("end")

