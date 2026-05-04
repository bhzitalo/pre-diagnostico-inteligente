import uuid

SESSOES = {}


def criar_sessao(sintomas, perguntas):
    session_id = str(uuid.uuid4())

    SESSOES[session_id] = {
        "sintomas": sintomas,
        "perguntas": perguntas,
        "respostas": {},
        "indice": 0
    }

    return session_id


def obter_sessao(session_id):
    return SESSOES.get(session_id)


def atualizar_resposta(session_id, pergunta, resposta):
    SESSOES[session_id]["respostas"][pergunta] = resposta
    SESSOES[session_id]["indice"] += 1