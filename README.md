# 🔍 Port Scanner Simples

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue)](https://python.org)
[![Licença](https://img.shields.io/badge/Licença-MIT-green)](LICENSE)

Um scanner de portas TCP básico desenvolvido em Python, criado com fins educacionais para demonstrar conceitos de redes e sockets. Ideal para quem está começando na área de segurança da informação ou desenvolvimento de ferramentas de rede.

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
   git clone https://github.com/Acacio-Gabriel/port-scanner-simples.git
   cd port-scanner-simples

2. Execute o scanner:
   ```bash
   python port-scanner.py <IP ou Hostname>
> **Atenção**: Utilize apenas em redes ou sistemas que você possui autorização para testar

---

## 🖥️ Exemplo de Uso
```bash
==================================================
   Port Scanner Simples
==================================================

Escaneando alvo: google.com (172.217.29.46)
Hora de inicio: 15:48:29
--------------------------------------------------
Porta 80 -> ABERTA
Porta 443 -> ABERTA
--------------------------------------------------
Escaneamento concluido. Portas abertas encontradas: 2
Portas: 80,443                         
```
---

## 📝 Explicação do codigo

O coração do programa esta na função `scan_port(host, port)`:

```python
def scan_port(host, port):
    try: 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) 

        resultado = sock.connect_ex((host, port))

        if resultado == 0 :
            sock.close()
            return True
        else:
            sock.close()
            return False

    except socket.error:
        return False 
```
Onde:
- `socket.socket()` cria um socket IPv4 (AF_INET) do tipo TCP (SOCK_STREAM).
- `settimeout(1)` define um tempo maximo de espera pela conexão.
- `connect_ex()` tenta conetar e retorna 0 se a porta estiver aberta (conexão bem sucedida). Diferente da `connect()`, não levanta exceção, facilitando o tratamento.
- Caso a conexão seja estabelecida, a porta foi considerado **aberta**; caso contrario, **fechada** ou **filtrada**
> O loop principal do código percorre as portas desejadas e acumula as abertas em uma lista.

---

## 🌐 Conceitos de Redes Envolvidos
1. **Socket**: Interface de comunicação entre processos, seja na mesma máquina ou pela rede.
2. **Porta**: Número que identifica um serviço específico em um host (ex: 80-> HTTP, 22 -> SSH).
3. **TCP**: Protocolo orientado à conexão. O scanner tenta completar o *three-way handshake*; se conseguir, a porta esta aberta.
4. **Timeout**: Mecanismo para não travar o programa ao tentar conectar em portas que não respondem (filtradas pelo firewall).
5. **Resolução de Nomes**: Uso de `gethostbyname()` para converter um dominio em endereço de IP.
---

## ⚖️ Aviso Legal
**Este software é fornecido apenas para fins educacionais**. O uso não autorizado de scanners de porta em sistemas de terceiros pode violar leis locais e políticas de uso aceitável. O autor não se responsabiliza por qualquer uso indevido ou danos causados pela ferramenta.

---
## 🔮 Melhorias Futuras
- Adicionar argumentos de linha de comando (porta inicial, final, timeout).
- Implementar multithreading para acelerar o escaneamento.
- Detecção de serviço via banner grabbing.
- Suporte a escaneamento UDP.
- Exportar resultados para JSON ou CSV.
- Criar uma interface gráfica simples (Tkinter ou web).

