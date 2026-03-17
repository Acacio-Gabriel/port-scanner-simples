"""
Port Scanner Simples 
Escaneia portas abertas em um alvo utilizando sockets tcp.
"""

import socket
import sys
from datetime import datetime

def scan_port(host, port):
    """
    Tenta fazer conexão a uma porta especifica do host
    Retornara TRUE se feita conexão ou FALSE se não houver conexão
    """
    try: 
        #Cria um socket IPv4, TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) #1seg de timeout para evitar travamento

        #Tentar conectar
        resultado = sock.connect_ex((host, port))

        #connet_ex retorna 0 se conxão bem sucessidida
        if resultado == 0 :
            sock.close()
            return True
        else:
            sock.close()
            return False
    except socket.error:
        return False
    
def main():
    
    #Exibir banner
    print("=" * 50)
    print("   Port Scanner Simples")
    print("=" * 50)

    #Obtem o alvo do usuario
    if len(sys.argv) != 2:
        print("Uso: python port-scanner.py <IP ou hostname>")
        print("Exemplo: python port-scanner.py 192.168.1.1")
        sys.exit[1]

    alvo = sys.argv[1]

    #Resolve o hostname para IP
    try:
        ip_alvo = socket.gethostbyname(alvo)
    except socket.gaierror:
        print("Não foi possivel revolver o hostname!")

    print(f"\nEscaneando alvo: {alvo} ({ip_alvo})")
    print("Hora de início:", datetime.now().strftime("%H:%M:%S"))
    print("-" * 50)

    #Definir portas a serem escaneadas
    portas = range(1, 1025)

    abertas = []

    try:
        for porta in portas:
            if scan_port(ip_alvo, porta):
                print(f"Porta {porta} -> ABERTA")
                abertas.append(porta)
    except KeyboardInterrupt:
        print("\n\nEscaneamento interrompido pelo usuário.")

    print("-" * 50)
    print(f"Escaneamento concluido. Portas abertas encontradas: {len(abertas)}")
    if abertas:
        print("Portas:", ",".join(str(p) for p in abertas))
    else:
        print("Nenhuma porta aberta no range especificado")
    print("Hora do término", datetime.now().strftime("%H:%M:%S"))

if __name__ == "__main__":
    main()
