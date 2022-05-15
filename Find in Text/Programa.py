from collections import Counter

texto1 = """
Se entre os petistas o lançamento da candidatura Lula–Alckmin foi vista com entusiasmo, dentro dos demais partidos o clima ainda de desconfiança. O deputado Evair de Melo (PP) classifica a união como uma “agenda de desespero”, um “mero ato para voltar ao poder”. “Isso é um casamento de cartório ode está se juntando o atraso da política brasileira, uma pauta retrógrada. Naturalmente, essa essa dupla que se apresenta hoje é defensora pública do aborto, da invasão de proprietário privada, quer revogar todas as avanços que nós tivemos na desburocratização do país e criar uma moeda própria. É um casamento de cartório, de desespero. É um abraço dos afogados, tendo em vista que ele não tem conteúdo, nem tem agenda para propor e para questionar, por exemplo, as ações positivas e proativas do governo federal e da bancada. Eu chego a dizer que é lamentável. É tanto atraso reunido para tentar retroceder com o país”, avalia o parlamentar.
O deputado Bibo Nunes (PL) segue o mesmo entendimento e avalia que o presidente Jair Bolsonaro tem muito mais chance de ser reeleito no fim do ano. 
“Essa Chapa Lula Alckmin, ao natural, já se desmoraliza. Basta ver o que o Alckmin falava do Lula. Chamava o Lula do que tinha de pior para o Brasil 
e agora está ao lado do Lula. As últimas falas do ex e futuro presidiário Lula revela um certo desequilíbrio, ele está muito despreparado. 
Não sei o que está acontecendo com ele, mas a verdade é que essa chapa será muito fácil de vencer essa”, afirma o deputado. O ex-presidente do PSDB 
José Aníbal avalia que Lula deu mais ênfase às críticas ao atual governo do que as propostas em si. “A gente viu um candidato que hoje está 
polarizando com o atual presidente. Os dois estão disputando a primazia nas pesquisas, O Lula com alguma vantagem, Bolsonaro atrás e os 
outros correndo atrás, mas sem ainda conseguirem alguma expressão mais relevante em matéria de intenção de voto”, considera Aníbal.
O atual presidente do PSDB, Bruno Araújo, também não poupou críticas. Pelas redes sociais, foi irônico ao comentar declarações do ex-presidente 
Lula de que não indicaria a ex-presidente Dilma Rousseff para um ministério por conta da grandeza dela. Araújo lembrou que o próprio Lula só 
não foi ministro por conta da resistência do Supremo Tribunal Federal (STF). Ainda segundo ele, para o PT, qualquer discurso para esconder 
Dilma serve. Dentro do Palácio do Planalto, o ministro do chefe da Casa Civil, Ciro Nogueira, também foi irônico. Pelas redes sociais, 
disse que a chapa é um “prato indigesto que o Brasil não vai engolir”. Segundo Nogueira, Lula disse que Alckmin, que é conhecido no meio 
político como chuchu, é “insosso, como se fosse comida sem sal” e, no passado, Alckmin dizia que Lula era mentiroso. 
Para Ciro Nogueira, o prato também pode ser de mentira.
"""

texto2 = """
O diretor da CIA, Bill Burns, alertou neste sábado (7) que o presidente russo, Vladimir Putin, apostou muito na segunda fase de sua guerra na Ucrânia e acredita que “dobrar” o conflito militar ainda é seu melhor caminho a seguir.
É essa mentalidade, disse Burns, que torna a segunda fase da ofensiva pelo menos tão arriscada – e talvez até mais arriscada – do que a primeira fase do conflito.
“Ele está em um estado de espírito em que não acredita que possa se dar ao luxo de perder”, disse Burns sobre Putin durante um evento do Financial Times em Washington. “Acho que ele está convencido agora de que dobrar ainda permitirá que ele progrida”.
“Suas convicções sobre a Ucrânia e a realidade da capacidade da Rússia de continuar lutando contra a resistência ucraniana – não sei se isso já foi abalado”, acrescentou. “Assim, as apostas são bastante altas.”
Essa visão é informada pelo que Burns disse ter observado sobre Putin nos últimos anos.
“O que eu vi, especialmente na última década, é ele de certa forma fervendo em uma combinação muito inflamável de queixas, ambição e insegurança, tudo meio que embrulhado”, disse ele.
Burns também disse que o risco de a guerra se transformar em um conflito nuclear não deve ser subestimado durante a segunda fase, mesmo que a comunidade de inteligência dos Estados Unidos não veja “evidências práticas neste momento do planejamento russo para a implantação de armas nucleares táticas”.
“Dado o tipo de agitação que ouvimos da liderança russa, não podemos ignorar essas possibilidades”, disse Burns. “Em um momento em que as apostas são muito altas para a Rússia de Putin e esses riscos nesta segunda fase do conflito são sérios e não devem ser subestimados”.
Ramificações fora da Rússia
Burns também disse que o conflito da Rússia na Ucrânia afetou os cálculos da China quando se trata de “como e quando” tentar assumir o controle de Taiwan.
“Claramente a liderança chinesa está tentando analisar cuidadosamente as lições que devem tirar da Ucrânia sobre suas próprias ambições em Taiwan”, disse Burns.
“Não acho que tenha erodido a determinação de Xi ao longo do tempo de ganhar controle sobre Taiwan, mas acho que é algo que está afetando seus cálculos sobre como e quando eles vão fazer isso”, acrescentou.
"""


def analisa_freq_letras_no_texto(texto):
    contador1 = Counter(texto.lower())
    total_letras = sum(contador1.values())

    proporcoes = [(letra, frequencia / total_letras) for letra, frequencia in contador1.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comum = proporcoes.most_common(10)
    print("Porcetagens Abaixo : ==v")
    for caracter, proporcao in mais_comum:
        print(" {} ==> {:.1f}%".format(caracter, proporcao * 100))


analisa_freq_letras_no_texto(texto1)
analisa_freq_letras_no_texto(texto2)
