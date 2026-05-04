from fastapi import APIRouter
from pydantic import BaseModel

from core.motor import (
    obter_perguntas,
    calcular_score,
    classificar_urgencia,
    gerar_recomendacao
)
from core.perguntas import PERGUNTAS
from core.sessao import criar_sessao, obter_sessao, atualizar_resposta

router = APIRouter()


class IniciarRequest(BaseModel):
    sintomas: list[str]


class ResponderRequest(BaseModel):
    session_id: str
    resposta: bool


@router.post("/iniciar")
def iniciar(data: IniciarRequest):
    perguntas = obter_perguntas(data.sintomas)

    session_id = criar_sessao(data.sintomas, perguntas)

    primeira = perguntas[0]

    return {
        "session_id": session_id,
        "pergunta": PERGUNTAS[primeira]["texto"],
        "pergunta_id": primeira
    }


@router.post("/responder")
def responder(data: ResponderRequest):
    sessao = obter_sessao(data.session_id)

    if not sessao:
        return {"erro": "Sessão inválida"}

    indice = sessao["indice"]
    perguntas = sessao["perguntas"]

    pergunta_atual = perguntas[indice]

    atualizar_resposta(data.session_id, pergunta_atual, data.resposta)

    # próxima pergunta
    if sessao["indice"] < len(perguntas):
        proxima = perguntas[sessao["indice"]]

        return {
            "pergunta": PERGUNTAS[proxima]["texto"],
            "pergunta_id": proxima
        }

    # fim → calcular resultado
    score = calcular_score(sessao["sintomas"], sessao["respostas"])
    nivel = classificar_urgencia(score)
    recomendacao = gerar_recomendacao(nivel)

    return {
        "final": True,
        "score": score,
        "urgencia": nivel,
        "recomendacao": recomendacao
    }