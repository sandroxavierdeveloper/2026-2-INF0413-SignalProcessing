#!/bin/bash

# Define o diretório do projeto
PROJECT_DIR="/home/deck/dev/sentinela"
cd "$PROJECT_DIR" || exit 1

# Verifica se o ambiente virtual existe antes de ativar
if [ -d ".venv" ]; then
    source .venv/bin/activate
    echo "Ambiente virtual (.venv) ativado com sucesso."
else
    echo "AVISO: Ambiente virtual (.venv) não encontrado!"
    echo "Iniciando Jupyter usando o ambiente do sistema..."
fi

# Força a execução usando o binário Python ativo no ambiente para garantir o Kernel correto
python -m jupyter lab
