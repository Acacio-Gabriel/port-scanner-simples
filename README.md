# 🔍 Port Scanner Simples

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue)](https://python.org)
[![Licença](https://img.shields.io/badge/Licença-MIT-green)](LICENSE)

Um scanner de portas TCP básico desenvolvido em Python, criado com fins educacionais para demonstrar conceitos de redes e sockets. Ideal para quem está começando na área de segurança da informação ou desenvolvimento de ferramentas de rede.

## 📌 Índice
- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Como Executar](#como-executar)
- [Exemplo de Uso](#exemplo-de-uso)
- [Explicação do Código](#explicação-do-código)
- [Conceitos de Redes Envolvidos](#conceitos-de-redes-envolvidos)
- [Aviso Legal](#aviso-legal)
- [Melhorias Futuras](#melhorias-futuras)
- [Licença](#licença)
- [Contato](#contato)

---

## 🧠 Sobre o Projeto

Este projeto faz parte do meu portfólio pessoal e tem como objetivo mostrar na prática como funciona um scanner de portas. Ele tenta estabelecer uma conexão TCP com um alvo (IP ou domínio) em um intervalo de portas pré-definido e informa quais estão abertas.

A ferramenta é **extremamente simples** e foi feita para aprendizado – não possui otimizações como multithreading, mas serve como base para entender os fundamentos.

---

## ⚙️ Funcionalidades

- Escaneamento de portas TCP em um alvo (IP ou hostname).
- Range de portas configurável (padrão: 1 a 1024).
- Timeout para evitar travamentos em portas filtradas.
- Exibição do status da porta (aberta/fechada) em tempo real.
- Tratamento de interrupção (Ctrl+C).
- Resolução de hostname para IP automaticamente.

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.6 ou superior instalado.
- Acesso a um terminal (Linux, macOS ou Windows).

### Passos

1. Clone o repositório:
   ```bash
   git clone [https://github.com/Acacio-Gabriel/port-scanner-simples.git](https://github.com/Acacio-Gabriel/port-scanner-simples.git)
   cd port-scanner-simples

2. Execute o scanner:
   ```bash
   python port-scanner.py <IP ou Hostname>
> **Atenção**: Utilize apenas em redes ou sistemas que você possui autorização para testar



