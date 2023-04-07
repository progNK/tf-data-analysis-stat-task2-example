import pandas as pd
import numpy as np

from scipy.stats import gamma


chat_id = 1262156999 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    loc1 = 2 / 92 ** 2 * (gamma.ppf((1 - p) / 2, x.size) / x.size + x.mean() - 1 / 2)
    loc2 = 2 / 92 ** 2 * (gamma.ppf((1 + p) / 2, x.size) / x.size + x.mean() - 1 / 2)

    return loc1, loc2
