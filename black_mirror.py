'''
DESENVOLVA UM PROGRAMA EM QUE O USUÁRIO IRÁ INFORMAR UMA PERGUNTA (UTILIZANDO
EXATAMENTE AS PERGUNTAS DO QUESTIONÁRIO ANTERIOR) E O SISTEMA DEVERÁ APRESENTAR A
RESPOSTA.
'''
'''
QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO?
QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE TELEVISÃO?
QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA A NETFLIX NO EPISÓDIO?
COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA?
QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE ELA FAZ EM RESPOSTA?
QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DE BLACK MIRROR?
O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK MIRROR? EXPLIQUE.
'''

pergunta = ""

while  True:
    pergunta = input("O que deseja saber sobre a serie -Joan is awful-?\n")

    if (pergunta == "Quem dirige a vida de Joan em tempo real para uma série de televisão?"):
        print("\nQuem dirige a vida de Joan é um computador quantico, uma especie de IA que nem os donos entendem bem\n")
    elif (pergunta == "Qual o nome do serviço de streaming fictício que parodia a netflix no episódio? "):
        print("\nO nome do serviço de streaming fictício é STREAMBARRY\n")
    elif (pergunta == "Como Joan descobre a existência da série sobre sua vida?"):
        print("\nJoan descobriu a série indo assistir algo na hora do jantar, seu noivo insiste em ver a serie com uma atriz que se asemelha a ela\n")
    elif (pergunta ==  "Qual a reação inicial de Joan ao descobrir a série e o que ela faz em resposta?"):
        print("\nJoan ficou em choque, teve uma crise de ansiedade e entrou em desespero\n")
    elif (pergunta == "Quais são os temas principais explorados neste episódio de Black Mirror?"):
        print("\nOs temas principais são como as empresas usam os dados dos cliente, quebra de privacidade e o uso do avanço tecnologico para o mal.\n")
    elif (pergunta == "O episódio termina de maneira típica para a série black mirror? Explique"):
        print("\nPelo meu pouco conhecimento sobre a serie em questão, não. Um final feliz e pleno não é tão comum em episodios tão catastroficos.\n")
    elif (pergunta == "Tchau"):
        print("Tchau. Até a proxima!")
        break
    else: 
        print("Não tenho conhecimentos o suficiente sobre essa pergunta, lamento.")