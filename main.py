import google.generativeai as genai
import os

#Config
genai.configure(api_key="SUA_CHAVE_API")
modelo = genai.GenerativeModel('gemini-1.5-flash')

def clear():
    os.system('cls')

#funções de cada artigo
def tratarSobreArtigo(nomeArtigo, detalhesPrompt):
    clear()
    print("< =================================================================== > \n")
    promptContexto = f"Contexto: Considerando apenas o artigo {nomeArtigo}, {detalhesPrompt}. Resuma o artigo de forma extensa e didática"
    responseContexto = modelo.generate_content(promptContexto)
    print(responseContexto.text)

    print("< =================================================================== > \n")

    promptPerguntas = f"""
                        Agora, baseado apenas no resumo a seguir, recomende 4 questões para serem respondidas por quem leu seu resumo:

                        {responseContexto.text}

                        (As perguntas devem estar no formato: Pergunta 1: ...; Pergunta 2:...;)
                    """
    response = modelo.generate_content(promptPerguntas)

    perguntasSplit = response.text.split("**")
    perguntas = [(perguntasSplit[2]), (perguntasSplit[4]), (perguntasSplit[6]), (perguntasSplit[8])]
    
    print("Selecione um das perguntas para responder: \n\n")
    for i, pergunta in enumerate(perguntas):
        print(f"{i+1}. {pergunta}")
    pergunta_selecionada = int(input("Digite o número da pergunta: "))

    respostaUsuario = input(f"Responda a pergunta: {perguntas[pergunta_selecionada-1]}")

    print("< =================================================================== > \n")

    promptCorrecao = f"Baseado no artigo {nomeArtigo} e no resumo {responseContexto.text} fornecido por você, corrija a resposta do usuário: {respostaUsuario} para a pergunta: {perguntas[pergunta_selecionada-1]}. Você deve utilizar apenas o contexto fornecido, deve explicar o motivo do erro (Caso haja) na resposta para que a pessoa que forneceu consiga aprender e aprimorar e deve avaliar de forma objetiva a resposta."
    responseCorrecao = modelo.generate_content(promptCorrecao)
    print(responseCorrecao.text)    

    input("Pressione Enter para continuar...")
    clear()

def main():
    #Menu
    artigo = 1

    while artigo != 0:
        print("Escolha um dos artigos para aprofundamento:")
        print("1. Facing Up to the Problem of Consciousness")
        print("2. The Conscious Mind")
        print("3. Hard problem of consciousness (https://iep.utm.edu/hard-problem-of-conciousness/)")
        print("4. Zumbis filosóficos, Stanford Encyclopedia of Philosophy (https://plato.stanford.edu/entries/zombies/)")
        print("0. Sair")

        artigo = int(input("Digite o número do artigo: "))

        if artigo == 1:
            nomeArtigo = "'Facing Up to the Problem of Consciousness' de David J. Chalmers"
            detalhesPrompt = "explique o que ele entende por 'problema difícil da consciência' e como ele diferencia este problema do 'problema fácil'"
            tratarSobreArtigo(nomeArtigo, detalhesPrompt)