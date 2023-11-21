from exclusiveAI.components.ActivationFunctions import ActivationFunction
from exclusiveAI.components.Layers import Layer
from .Optimizer import Optimizer
from ...utils import myzip

class Adam(Optimizer):
    def __init__(self, beta1: float, beta2: float, eps: float):
        self.__init__()  
        self.mean = 0
        self.variance = 0
        self.beta1 = beta1
        self.beta2 = beta2
        self.eps = eps
        
    def update(self, model, y_true, x):
        if self.old_dw is None: self.old_dw = [0 for _ in model.layers]
        
        deltas = self.calulate_deltas(model, y_true, x)

        self.mean = self.beta1 * self.mean + (1 - self.beta1) * deltas
        self.variance = self.beta2 * self.variance + (1 - self.beta2) * deltas ** 2
        
        new_mean = self.mean / (1 - self.beta1)
        new_var = self.variance / (1 - self.beta2)
        
        for layer in model.layers:
            layer.weights = layer.weights - (self.learning_rate * new_mean / (new_var ** 0.5 + self.eps))
        
        self.old_dw = deltas