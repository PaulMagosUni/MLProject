from .LossFunction import LossFunction
import numpy as np

__all__ = ["CrossCorrelation"]

class CrossCorrelation(LossFunction):
    def __init__(self) -> None:
        super().__init__(
            name = "Cross Correlation",
            loss_function = lambda x, y: -1 * np.sum(x * y) / np.sqrt(np.sum(x * x) * np.sum(y * y), dtype=np.float64),
            loss_function_derivative = lambda x, y: (x * y) / np.sqrt(np.sum(x * x) * np.sum(y * y), dtype=np.float64),
        )