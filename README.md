# Calculadora em Cadeia Inteligente

Este é um projeto de uma calculadora em cadeia desenvolvida em Python. Ele foi construído para ser totalmente à prova de erros de digitação do usuário e falhas matemáticas clássicas.

## Funcionalidades

- **Cálculo em Cadeia:** O resultado da última operação é guardado na memória e serve como ponto de partida para a próxima conta.
- **Tratamento de Exceções (`try/except`):** O programa não quebra se o usuário digitar letras ou caracteres especiais onde deveriam ser números.
- **Validação de Inputs:** Filtros inteligentes que impedem símbolos de operações inválidos e tratam respostas maiúsculas/minúsculas (ex: `S` ou `s`).
- **Proteção Matemática:** Validação interna que impede a quebra do sistema por divisão por zero.
