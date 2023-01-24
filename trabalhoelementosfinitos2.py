# Continuacao do trabalho 1 de elementos finitos mas adicionando a matéria final 
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sympy import Matrix, init_printing

init_printing()

T_inf = 293.15
L = 0.025
k = 35
U = 67967200
rho = 8618
h_barra = 0.25 * (10**5)
c = 460
euler = 2.718281828459045235360287  # nao foi definido no problema mas estou fazendo por
                                # conta própria por conveniencia caso precise

