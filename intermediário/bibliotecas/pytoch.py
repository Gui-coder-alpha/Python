import torch 
import torch.nn as nn
import torch.optim as optim

# Definir uma rede neural simples
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(10, 50)
        self.fc2 = nn.Linear(50, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Instanciar a rede neural, definir a função de perda e o otimizador
net = Net()
criterion = nn.MSELoss()
optimizer = optim.SGD(net.parameters(), lr=0.01)

# Treinar a rede neural
for epoch in range(100):
    inputs = torch.randn(10)  # Exemplo de dados de entrada
    target = torch.randn(1)   # Exemplo de alvo
    optimizer.zero_grad()
    output = net(inputs)
    loss = criterion(output, target)
    loss.backward()
    optimizer.step()

# Devo aprender mais sobre o assunto
