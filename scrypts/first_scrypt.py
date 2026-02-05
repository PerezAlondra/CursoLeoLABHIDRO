# -*- coding: utf-8 -*-
"""
Documentar Código
----------------------first_scrypt.py------------------------------------------
Este escrpit foi usado para prender a usar o python
"""

#importação de pacotes para usar este Script
import numpy as np
import matplotlib.pyplot as plt


def timeSeriesPlot(arr):
    """
    Esta função é usada para gerar uma figuara...
    Parameters
    ----------
    arr : np.array
        array com matriz de dados
    Returns
    -------
    fig : TYPE
        DESCRIPTION.
    Exemplo de uso
    fig, arr_avegrage = timeSeriesPlot(arr)
    """
    
    #Media o eixo 1  (coluna)
    arr_average = np.mean(arr,axis=1)
    
    #Criando uma figura 
    fig, ax = plt.subplots(2)
    
    #Plotando a media e dados brutos
    ax[0].plot(arr_average)
    ax[1].plot(arr)
    fig.savefig(r"C:/Users/alond/Documents/GitHub/CursoLeoLABHIDROpy/figuras"+
                '/timeSeriesPlot.png', dpi = 300)
    return fig, arr_average