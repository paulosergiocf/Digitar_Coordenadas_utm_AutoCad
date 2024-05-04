#!/bin/bash

# Função para procurar e remover pastas __pycache__
remove_pycache() {
    for pycache_dir in $(find . -type d -name "__pycache__"); do
        echo "Removendo $pycache_dir"
        rm -r "$pycache_dir"
    done
}

# Chamando a função para remover pastas __pycache__
remove_pycache

echo "Remoção de pastas __pycache__ concluída."
