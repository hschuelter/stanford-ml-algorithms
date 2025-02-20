import numpy as np
import math
import matplotlib.pyplot as plt

from models.model import Model

class Single_Feature_Model(Model):
    w = 0.0
    b = 0.0
    cost = math.inf
    cost_history = []

    # def __init__(self, alpha: float, iterations: int) -> None:
    #     self.alpha = alpha
    #     self.iterations = iterations

    def compute_model_output(self, x: np.ndarray) -> np.ndarray:
        """
        Computes the prediction of a linear model
        Args:
            x (ndarray (m,)): Data, m examples 
            w,b (scalar)    : model parameters  
        Returns
            f_wb (ndarray (m,)): model prediction
        """
        m = x.shape[0]
        f_wb = np.zeros(m)
        for i in range(m):
            f_wb[i] = self.w * x[i] + self.b

        return f_wb
    
    def compute_model_output(self, x: float) -> float:
        """
        Computes the prediction of a linear model
        Args:
            x (scalar): Data, single example 
        Returns
            f_wb (float): model prediction
        """
        f_wb = self.w * x + self.b

        return f_wb
    
    def compute_cost(self, x: np.ndarray, y: np.ndarray) -> float:
        """
        Computes the cost of data.
        Args:
            x (ndarray (m,)): Data, m examples 
            y (ndarray (m,)): Data, m examples 
        Returns:
            cost (float): 
        """
        m = x.shape[0]
        cost_sum = 0
        for i in range(m):
            f_wb = self.w * x[i] + self.b
            cost = (f_wb - y[i]) ** 2
            cost_sum += cost
        
        total_cost = (1 / (2 * m)) * cost_sum  
        
        self.cost = total_cost
        return total_cost
    
    def compute_gradient(self, x: np.ndarray, y: np.ndarray, w: float, b: float) -> tuple[float, float]:
        """
        Computes the gradient, used for gradient descent.
        Args:
            x (ndarray (m,)): Data, m examples 
            y (ndarray (m,)): Data, m examples 
            w,b (scalar)    : model parameters 
        Returns:
            cost (float): 
        """

        n = x.shape[0]

        dw = 0.0
        db = 0.0

        for i in range(n):
            f_wb = w * x[i] + b
            dw_i = (f_wb - y[i]) * x[i]
            db_i = f_wb - y[i]

            dw += dw_i
            db += db_i

        dw /= n
        db /= n

        return dw, db
    
    def gradient_descent(self, x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
        """
        Computes the gradient, used for gradient descent.
        Args:
            x (ndarray (m,)): Data, m examples 
            y (ndarray (m,)): Data, m examples 
        Returns:
            w,b (scalar)    : model parameters
        """
        _w = self.w
        _b = self.b

        for i in range(self.iterations):
            dw, db = self.compute_gradient(x, y, _w, _b)

            _w = _w - (self.alpha * dw)
            _b = _b - (self.alpha * db)

            self.w = _w
            self.b = _b
            self.cost_history.append(self.compute_cost(x, y))

        self.cost_history = np.array(self.cost_history)
        return _w, _b