from dao.database import execute_query


def inserir_chamado(chamado):
    sql = """
    INSERT INTO chamados
    (cliente, descricao, prioridade, status, statusfinal)
    VALUES (%s, %s, %s, %s, %s)
    """

    return execute_query(
        sql,
        (
            chamado.cliente,
            chamado.descricao,
            chamado.prioridade,
            chamado.status,
            chamado.statusfinal
        )
    )


def listar_chamados():
    sql = """
    SELECT *
    FROM chamados
    WHERE statusfinal = FALSE
    ORDER BY id ASC
    """

    return execute_query(sql, fetch=True)


def atender_chamado(id_chamado):
    sql = """
    UPDATE chamados
    SET status = 'Em Atendimento'
    WHERE id = %s
    """

    return execute_query(sql, (id_chamado,))


def concluir_chamado(id_chamado):
    sql = """
    UPDATE chamados
    SET status = 'Resolvido'
    WHERE id = %s
    """

    return execute_query(sql, (id_chamado,))


def cancelar_chamado(id_chamado):
    sql = """
    UPDATE chamados
    SET statusfinal = TRUE
    WHERE id = %s
    """

    return execute_query(sql, (id_chamado,))


def buscar_por_id(id_chamado):
    sql = """
    SELECT *
    FROM chamados
    WHERE id = %s
    """

    resultado = execute_query(
        sql,
        (id_chamado,),
        fetch=True
    )

    if resultado:
        return resultado[0]

    return None