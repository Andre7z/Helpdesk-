from flask import Flask, render_template, request, redirect, url_for

from dao.chamado_dao import (
    inserir_chamado,
    listar_chamados,
    atender_chamado,
    concluir_chamado,
    cancelar_chamado
)

from model.chamado import Chamado

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/abrir')
def abrir():
    return render_template('abrir_chamado.html')


@app.route('/novo', methods=['POST'])
def novo():
    cliente = request.form['cliente']
    descricao = request.form['descricao']
    prioridade = request.form['prioridade']

    chamado = Chamado(
        cliente,
        descricao,
        prioridade
    )

    inserir_chamado(chamado)

    return redirect(url_for('fila'))


@app.route('/fila')
def fila():
    chamados = listar_chamados()

    return render_template(
        'fila.html',
        chamados=chamados or ()
    )


@app.route('/atender/<int:id_chamado>')
def atender(id_chamado):
    atender_chamado(id_chamado)
    return redirect(url_for('fila'))


@app.route('/concluir/<int:id_chamado>')
def concluir(id_chamado):
    concluir_chamado(id_chamado)
    return redirect(url_for('fila'))


@app.route('/cancelar/<int:id_chamado>')
def cancelar(id_chamado):
    cancelar_chamado(id_chamado)
    return redirect(url_for('fila'))


if __name__ == '__main__':
    app.run(debug=True, port=8000)
    # arruma debug para false
    