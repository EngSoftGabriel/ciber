import sys

def detectar_invasao(registros):
    # Variáveis para rastrear o ID do usuário atual e suas falhas consecutivas
    usuario_atual = None
    tentativas_consecutivas = 0
    invasor_detectado = None

    # Percorre cada registro de log
    for registro in registros:
        id_usuario, status = registro.split(':')

        # Verifica se o usuário atual é o mesmo da iteração anterior
        if id_usuario == usuario_atual:
            if status == "falha":
                tentativas_consecutivas += 1
                if tentativas_consecutivas >= 4:
                    invasor_detectado = id_usuario
            else:
                tentativas_consecutivas = 0
        else:
            # Atualiza para o novo usuário e reinicia a contagem de tentativas falhas
            usuario_atual = id_usuario
            tentativas_consecutivas = 1 if status == "falha" else 0

    return invasor_detectado if invasor_detectado else "Nenhum invasor detectado"

# Função principal para executar o programa
def main():
    # Solicita ao usuário que insira os registros de log
    entrada = sys.stdin.readline().strip()
    
    registros = [registro.strip().strip('"') for registro in entrada.split(",")]

    # Chama a função para detectar tentativas de invasão
    resultado = detectar_invasao(registros)

    # Imprime o resultado
    print(resultado)

# Chama a função principal para executar o programa
if __name__ == "__main__":
    main()