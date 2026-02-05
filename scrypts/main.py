# -*- coding: utf-8 -*-
"""
Este é o main, arquivo raiz onde executos minhas funções (master) 
"""

import numpy as np
import first_scrypt 

arr = np.random.rand(100,100) 

first_scrypt.timeSeriesPlot(arr)
