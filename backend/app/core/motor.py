# backend/app/core/motor.py

from .sintomas import SINTOMAS
from .perguntas import PERGUNTAS


def obter_perguntas(sintomas_usuario):
    perguntas = []

    for sintoma in sintomas_usuario:
        if sintoma in SINTOMAS:
            perguntas.extend(SINTOMAS[sintoma]["perguntas"])

    # remove duplicadas mantendo ordem
    perguntas_unicas = []
    for p in perguntas:
        if p not in perguntas_unicas:
            perguntas_unicas.append(p)

    return perguntas_unicas


def calcular_score(sintomas_usuario, respostas):
    score = 0

    # soma gravidade base
    for sintoma in sintomas_usuario:
        if sintoma in SINTOMAS:
            score += SINTOMAS[sintoma]["gravidade_base"]

    # soma respostas
    for pergunta, resposta in respostas.items():
        if resposta is True and pergunta in PERGUNTAS:
            score += PERGUNTAS[pergunta]["peso"]

    return score


def classificar_urgencia(score):
    if score >= 7:
        return "alta"
    elif score >= 4:
        return "moderada"
    else:
        return "baixa"


def gerar_recomendacao(nivel):
    if nivel == "alta":
        return "Procure atendimento médico imediato."
    elif nivel == "moderada":
        return "Recomenda-se procurar um médico em breve."
    else:
        return "Acompanhe os sintomas. Procure ajuda se piorar."