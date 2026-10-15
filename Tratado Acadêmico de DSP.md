# TRATADO ACADÊMICO DE PROCESSAMENTO DIGITAL DE SINAIS: FUNDAMENTOS, ALGORITMOS E APLICAÇÕES PRÁTICAS

Edição Especial Linearizada e Otimizada para Leitura em Voz Alta e Leitores de Tela.

---

## CAPÍTULO I — FUNDAMENTOS: DO CONTÍNUO AO DISCRETO E A SIMULAÇÃO COMPUTACIONAL

### 1. Natureza dos Sinais e o Mapeamento Temporal

A ontologia do Processamento Digital de Sinais repousa sobre a distinção axiomática entre o mundo físico, inerentemente contínuo, e o paradigma computacional, estritamente discreto e finito. Um sinal analógico ou contínuo no tempo é definido matematicamente como uma função x de t, cujo domínio temporal t pertence ao conjunto dos números reais. 

Neste domínio contínuo, entre quaisquer dois instantes no tempo existe uma infinidade de outros instantes. Isso reflete a natureza de fenômenos físicos clássicos, como a flutuação da pressão acústica de uma onda sonora que se propaga pelo ar, a variação de voltagem através de um condutor, ou a dinâmica orbital de um corpo celeste.

Para que a arquitetura de von Neumann de um computador digital — uma máquina de estados essencialmente finita e operada por pulsos discretos de relógio, ou clock — possa processar tais fenômenos, torna-se imperativa a discretização temporal. O sinal discreto no tempo, representado por x de n entre colchetes, é gerado através da extração de observações de x de t em instantes perfeitamente espaçados. 

O parâmetro que governa este retalhamento do tempo é o período de amostragem, denominado T s, medido em segundos por amostra. A sua recíproca é a taxa de amostragem, denominada f s, mensurada em amostras por segundo, ou Hertz.

O mapeamento rigoroso entre o domínio contínuo e o discreto é estabelecido pela relação fundamental: o tempo contínuo t é igual ao índice da amostra n multiplicado pelo período de amostragem T s, o que também equivale a n dividido pela taxa de amostragem f s. Aqui, n é o índice adimensional inteiro da amostra. 

A intuição geométrica desta transformação é o congelamento do movimento contínuo em quadros ou fotografias sucessivas. A simulação computacional de eventos contínuos pressupõe que, se o passo de integração delta t for infinitesimalmente pequeno em relação à dinâmica intrínseca do sistema, a evolução temporal física poderá ser aproximada de forma iterativa por equações a diferenças, sem perdas qualitativas de informação estrutural. A falha em compreender esta limitação gera armadilhas clássicas de simulação, onde a máquina diverge da realidade física.

---

### 2. Estudo de Caso Analógico 1: Circuito RC (Carga e Descarga de Capacitores)

O circuito formado por um resistor R e um capacitor C em série atua como o paradigma clássico e primário de um sistema dinâmico contínuo de primeira ordem. Para derivar a sua dinâmica, invocamos a Lei das Malhas de Kirchhoff, a qual postula que a tensão fornecida pela fonte, V de t, deve ser igual à soma da queda de tensão no resistor, V R de t, com a queda de tensão no capacitor, V C de t.

Sabendo pela Lei de Ohm que a tensão no resistor é a resistência R multiplicada pela corrente i de t, e sabendo pela definição de capacitância que a corrente elétrica é a taxa de variação da carga no tempo — isto é, a corrente i de t é igual à capacitância C multiplicada pela derivada temporal da tensão no capacitor, d V C sobre d t —, podemos formular a Equação Diferencial Ordinária canônica do sistema:

A resistência R multiplicada pela capacitância C, multiplicada pela derivada de V C em relação ao tempo, mais a tensão V C de t, é igual à tensão constante da fonte V zero. Em símbolos algébricos usuais, escreve-se: R vezes C vezes d V C sobre d t, mais V C de t, igual a V zero.

Para obtermos a solução exata da carga, isolamos a derivada e utilizamos o método de separação de variáveis. Rearranjando os termos, obtemos:

A derivada d V C dividida pela diferença entre V C e V zero é igual a menos d t dividido pelo produto R vezes C.

Integrando ambos os lados da equação, a partir do instante inicial t igual a zero até o instante t genérico, e assumindo a condição inicial de um capacitor inteiramente descarregado — ou seja, V C no instante zero é igual a zero volts —, obtemos:

O logaritmo natural do módulo da fração cujo numerador é V C de t menos V zero, e cujo denominador é menos V zero, é igual a menos t dividido pelo produto R vezes C.

Exponenciando ambos os membros da igualdade e isolando a tensão no capacitor V C de t, definimos a constante de tempo do sistema físico como a letra grega tau, igual ao produto da resistência R pela capacitância C. A equação governante da carga consolida-se como:

A tensão no capacitor V C de t é igual à tensão da fonte V zero, multiplicada pelo fator um menos a exponencial de menos t dividido por tau. Em notação compacta: V C de t é igual a V zero que multiplica abre colchetes um menos e elevado a menos t sobre tau fecha colchetes.

Inversamente, para a fase de descarga, a fonte é removida e curto-circuitada, estabelecendo V zero igual a zero na Equação Diferencial Ordinária, com a condição inicial de que o capacitor possui uma tensão máxima inicial V C zero. A solução homogênea resulta no decaimento exponencial puro:

A tensão no capacitor V C de t durante a descarga é igual à tensão inicial V C zero multiplicada pela exponencial de menos t dividido por tau. Em notação compacta: V C de t é igual a V C zero vezes e elevado a menos t sobre tau.

Uma regra prática amplamente utilizada em instrumentação e análise de estabilidade é o critério de cinco vezes a constante de tempo tau. Numericamente, ao atingir o tempo t igual a cinco vezes tau, a componente transiente residual, dada pela exponencial de menos cinco, decai para aproximadamente zero vírgula zero zero seis sete, ou seja, menos de zero vírgula sete por cento do seu valor original. Isso significa que o sistema atinge mais de noventa e nove vírgula três por cento do seu estado final de regime permanente, permitindo que engenheiros assumam, para fins práticos, que a transição se concluiu.

#### Dedução da Equação a Diferenças e Análise Profunda de Estabilidade Numérica

A simulação computacional desta Equação Diferencial Ordinária requer a aproximação da derivada contínua por diferenças finitas. Implementando o método de integração numérica de Euler explícito para a frente, aproximamos a derivada contínua d V C sobre d t pela taxa de variação discreta no intervalo: a tensão no capacitor na amostra atual n menos a tensão na amostra imediatamente anterior n menos um, tudo dividido pelo passo de integração delta t.

Substituindo esta aproximação na Equação Diferencial Ordinária original, temos: o produto R vezes C multiplicado pela fração com numerador V C de n menos V C de n menos um e denominador delta t, somado a V C de n menos um, é igual a V zero. 

Multiplicando toda a expressão por delta t dividido pela constante tau — lembrando que tau é igual a R vezes C —, e isolando a amostra futura V C de n, obtemos a equação de recorrência discreta fundamental:

A tensão V C de n é igual a abre parênteses um menos delta t sobre tau fecha parênteses multiplicado por V C de n menos um, mais a fração delta t sobre tau multiplicada pela tensão da fonte V zero.

A solução analítica exata desta equação a diferenças discretas de primeira ordem decompõe-se na soma de uma solução particular de regime permanente com a solução homogênea transitória:

A tensão V C de n é igual a V zero, mais a diferença entre a tensão inicial V C de zero e V zero, multiplicada pelo termo lambda elevado à enésima potência inteira n. Aqui, a base de decaimento lambda é a raiz característica discreta dada por: lambda é igual a um menos a fração delta t sobre tau.

Para que a simulação numérica permaneça estável e convirja para o regime físico real, a magnitude da raiz característica lambda deve residir estritamente dentro do círculo unitário de convergência. Isso impõe a inequação estrita de estabilidade assintótica: o módulo de lambda deve ser menor do que um.

Expandindo esta condição em termos das grandezas físicas: o módulo de abre parênteses um menos delta t sobre tau fecha parênteses deve ser estritamente menor do que um. Isso desdobra-se em duas desigualdades simultâneas: menos um deve ser menor do que um menos delta t sobre tau, e um menos delta t sobre tau deve ser menor do que mais um.

A primeira desigualdade estabelece que delta t sobre tau deve ser maior do que zero, o que é naturalmente atendido, pois o tempo avança para a frente. Contudo, a segunda desigualdade impõe uma barreira física e matemática inegociável: delta t sobre tau deve ser estritamente menor do que dois, o que significa que o passo de amostragem delta t deve ser rigorosamente menor do que duas vezes a constante de tempo tau.

Se o pesquisador cometer a negligência de escolher uma taxa de amostragem f s excessivamente baixa — de modo que o passo delta t seja estritamente superior a duas vezes tau —, o valor de lambda torna-se um número real negativo com magnitude estritamente maior do que um, como por exemplo menos um vírgula dois. Elevado à potência n no computador, este termo oscilará de sinal a cada amostra sucessiva com amplitudes exponencialmente crescentes, divergindo para mais infinito e menos infinito. Isso gera um colapso numérico violento que nada tem a ver com o circuito elétrico real, constituindo um artefato espúrio da discretização matemática desestabilizada.

#### Roteiro Prático e Instruções para o Jupyter Notebook no Laboratório 2

No repositório do curso, este experimento encontra-se no primeiro notebook da pasta assets barra labs barra le zero dois sublinhado sampling hífen theorem, chamado le zero dois sublinhado p t zero um sublinhado analog hífen digital hífen signals ponto ipynb. Ele não usa o método de Euler: calcula as curvas analíticas direto sobre um vetor de tempo denso, que representa o sinal contínuo.

Preparação do ambiente: o notebook importa NumPy como n p e Matplotlib Pyplot como p l t, e acrescenta dois níveis acima ao caminho de busca, com sys ponto path ponto append de ponto ponto barra ponto ponto barra, para importar a biblioteca de gráficos lib ponto myPlotLib. Abra o Jupyter com o diretório de trabalho na pasta do notebook.

Primeira etapa: parâmetros do circuito. A tensão da fonte V zero vale cinco volts. A resistência R vale dez quiloohms, isto é, dez elevado a quatro ohms. A capacitância C vale cem microfarads, isto é, cem vezes dez elevado a menos seis farads. A constante de tempo tau é R vezes C, igual a um segundo.

Segunda etapa: o vetor de tempo t é criado com n p ponto linspace de zero a cinco segundos, com quinhentos pontos. Cinco segundos são cinco vezes tau.

Terceira etapa: as duas curvas. A carga é v sublinhado carga igual a V zero vezes um menos a exponencial de menos t sobre tau. A descarga é v sublinhado descarga igual a V zero vezes a exponencial de menos t sobre tau. Ambas usam n p ponto exp sobre o vetor inteiro, sem laço.

Quarta etapa: gráficos. Uma figura com dois subgráficos lado a lado, plt ponto subplots com uma linha e duas colunas, traça a carga em azul e a descarga em vermelho, com grade, rótulo Tempo em segundos e rótulo Tensão em volts. Em cinco segundos, a carga chega a cerca de noventa e nove vírgula três por cento de cinco volts, ou quatro vírgula noventa e sete volts.

Exercício opcional, que não está no notebook: simulação numérica pelo método de Euler e o limite de estabilidade. Com passo delta t igual a um sobre f s, a recorrência é v de n igual a v de n menos um mais delta t sobre tau vezes V zero menos v de n menos um. Com f s igual a cem Hertz, o passo é de zero vírgula zero um segundo e a curva acompanha a analítica. Se delta t passar de dois tau, o fator um menos delta t sobre tau fica menor que menos um, e os valores oscilam com amplitude crescente. Com f s de zero vírgula quatro Hertz, delta t vale dois vírgula cinco segundos e o fator é menos um vírgula cinco; para ver a divergência, simule por vários passos, por exemplo cinquenta segundos.

---

### 3. Estudo de Caso Analógico 2: Balística e Lançamento Oblíquo de Projéteis

O lançamento oblíquo oferece um contraponto pedagógico soberbo para desmistificar a representação temporal de sinais em contraste com a representação espacial. O movimento de um projétil sob aceleração da gravidade constante decompõe-se vetorialmente em dois eixos ortogonais independentes segundo a mecânica clássica newtoniana.

No eixo horizontal x, assumindo o vácuo ideal sem resistência do ar, a força resultante é nula. Pela Segunda Lei de Newton, a aceleração horizontal é zero, o que caracteriza um Movimento Retilíneo Uniforme com velocidade horizontal constante v zero x, dada por: v zero x é igual à velocidade inicial escalar de disparo v zero multiplicada pelo cosseno do ângulo de elevação teta. A sua equação horária de posição horizontal é: x de t é igual a v zero x multiplicado pelo tempo contínuo t.

No eixo vertical y, a força da gravidade atua apontando para o centro da Terra, imprimindo uma aceleração vertical descendente constante menos g. Pela integração no tempo, a velocidade vertical instantânea v y de t é igual à velocidade vertical inicial v zero y — calculada como v zero multiplicado pelo seno do ângulo teta — menos o produto da aceleração g pelo tempo t. 

Integrando a velocidade vertical em relação ao tempo com a condição inicial de disparo a partir do solo na origem, ou seja, y no instante zero igual a zero, obtém-se a clássica equação horária do Movimento Uniformemente Variado:

A altura vertical y de t é igual à velocidade vertical inicial v zero y multiplicada pelo tempo t, menos a metade da aceleração da gravidade g multiplicada pelo quadrado do tempo t. Em notação compacta: y de t é igual a v zero vezes seno de teta vezes t, menos meio de g vezes t ao quadrado.

O tempo total de voo até o projétil regressar ao solo é determinado calculando as raízes da equação quadrática em que a altura y de t se anula:

O produto do tempo t pelo fator abre parênteses v zero y menos meio de g vezes t fecha parênteses deve ser igual a zero.

Descartando a raiz trivial t igual a zero correspondente ao momento exato do disparo, isola-se o tempo total de voo até o impacto com o solo:

O tempo total de voo é igual a duas vezes a velocidade vertical inicial v zero y dividida pela aceleração da gravidade g. O instante de altura máxima ocorre exatamente na metade deste intervalo temporal, correspondente a v zero y dividido por g. Substituindo este instante na equação horária vertical, a altura máxima atingida pelo projétil é calculada analiticamente como o quadrado da velocidade inicial v zero multiplicado pelo quadrado do seno de teta, tudo dividido por duas vezes a gravidade g.

#### Dedução Analítica da Trajetória Espacial Bidimensional e a Distinção Conceitual

Uma pegadinha clássica em exames acadêmicos ocorre quando estudantes analisam o gráfico do sinal temporal da altura y de t e o confundem precipitadamente com a trajetória física bidimensional y de x descrita pelo corpo no espaço físico real. Embora ambos os gráficos desenhem parábolas descendentes com concavidade voltada para baixo, eles operam em domínios ontológicos completamente distintos.

Para deduzir analiticamente a equação da trajetória espacial pura e eliminar a variável independente tempo, isolamos o parâmetro temporal t a partir da equação horária do movimento horizontal: o tempo t é igual ao deslocamento horizontal x dividido pela velocidade horizontal v zero x, o que equivale a x dividido por v zero vezes cosseno de teta.

Substituindo esta expressão no lugar da variável t na equação horária da posição vertical y, obtemos sucessivamente:

A altura y é igual a v zero vezes seno de teta multiplicado por x sobre v zero vezes cosseno de teta, menos meio de g multiplicado pelo quadrado de x sobre v zero vezes cosseno de teta.

Simplificando a velocidade v zero no primeiro termo e lembrando da identidade trigonométrica fundamental de que o seno de teta dividido pelo cosseno de teta é a tangente de teta, alcançamos a expressão canônica final da trajetória espacial:

A altura vertical y em função do deslocamento horizontal x é igual à tangente do ângulo teta multiplicada por x, menos uma fração cujo numerador é a gravidade g multiplicada por x ao quadrado, e cujo denominador é duas vezes o quadrado da velocidade inicial v zero multiplicado pelo quadrado do cosseno do ângulo teta.

A análise comparativa profunda revela o abismo conceitual entre as duas curvas:

No sinal temporal y de t, o eixo das abscissas mede o tempo em segundos e o eixo das ordenadas mede a altura em metros. A taxa de variação instantânea desta curva — isto é, a derivada primeira d y sobre d t — é uma grandeza cinemática expressa em metros por segundo, representando fisicamente a velocidade vertical do projétil, a qual cruza pelo zero exatamente no topo do lançamento.

Por outro lado, na trajetória espacial y de x, tanto o eixo horizontal quanto o eixo vertical são medidos na mesma unidade física de comprimento — metros. A derivada d y sobre d x desta curva não é uma velocidade, mas sim a inclinação geométrica do vetor tangente da trajetória no espaço bidimensional, sendo uma grandeza adimensional equivalente à tangente do ângulo instantâneo da trajetória em cada ponto espacial. 

O alcance horizontal máximo no solo é obtido fazendo y de x igual a zero na equação da trajetória espacial, resultando em: o alcance total é duas vezes a velocidade inicial ao quadrado multiplicada pelo seno de teta vezes cosseno de teta, tudo dividido por g, o que pela identidade trigonométrica do arco duplo equivale a v zero ao quadrado multiplicado pelo seno de dois teta, tudo dividido pela gravidade g.

#### Roteiro Prático e Instruções para o Jupyter Notebook no Laboratório 2

No mesmo notebook, le zero dois sublinhado p t zero um sublinhado analog hífen digital hífen signals ponto ipynb, a simulação do projétil é uma célula própria, com o comentário Sinal de Balística.

Primeiro passo: constantes. A gravidade g vale nove vírgula oitenta e um metros por segundo ao quadrado, a velocidade inicial v zero vale cinquenta metros por segundo e o ângulo teta vale quarenta e cinco graus, convertido com n p ponto radians.

Segundo passo: componentes da velocidade. v zero x é v zero vezes cosseno de teta, e v zero y é v zero vezes seno de teta.

Terceiro passo: tempo de voo. t sublinhado voo é duas vezes v zero y dividido por g. O vetor t tem quinhentos pontos de n p ponto linspace entre zero e t sublinhado voo.

Quarto passo: x é v zero x vezes t. O vetor y é v zero y vezes t menos zero vírgula cinco vezes g vezes t ao quadrado.

Quinto passo: dois subgráficos lado a lado. À esquerda, o título é Sinal Analógico: Altura vs Tempo, com eixos Tempo em segundos e Altura em metros. À direita, o título é Trajetória 2D do Projétil, com eixos Distância em metros e Altura em metros.

Resultado: o sinal temporal dura cerca de sete vírgula dois segundos e atinge o ápice em cerca de três vírgula seis segundos. A trajetória espacial alcança cerca de duzentos e cinquenta e quatro vírgula oito metros de distância e sessenta e três vírgula sete metros de altura máxima. O mesmo vetor y é um sinal de tempo no primeiro gráfico e uma forma espacial no segundo.

---

## CAPÍTULO II — O TEOREMA DA AMOSTRAGEM DE NYQUIST-SHANNON E RECONSTRUÇÃO

### 1. O Teorema da Amostragem

O alicerce da revolução digital é o Teorema da Amostragem de Nyquist-Shannon. Ele resolve um aparente paradoxo filosófico: como é possível reconstruir perfeitamente infinitos pontos do espaço contínuo possuindo apenas um subconjunto finito e discreto de amostras?

O teorema afirma de forma matematicamente rigorosa que um sinal contínuo no tempo, x de t, pode ser amostrado e posteriormente reconstruído de maneira idêntica e sem qualquer grau de perda de informação se, e somente se, o espectro desse sinal for estritamente limitado por uma frequência máxima f máxima, e a taxa de amostragem f s obedecer à estrita desigualdade:

A taxa de amostragem f s deve ser estritamente maior do que duas vezes a frequência máxima f máxima. Em termos matemáticos diretos: f s é estritamente maior do que duas vezes f máxima.

A métrica fundamental de metade da taxa de amostragem, ou seja, f s dividido por dois, é consagrada como a Frequência de Nyquist do sistema. Ela constitui o limite agudo de resolução espectral, sendo também conhecida coloquialmente como a frequência de dobramento. A taxa mínima exigida inerente ao sinal analógico, correspondente ao dobro da sua frequência máxima, é formalmente referida como a Taxa de Nyquist.

---

### 2. O Fenômeno do Aliasing (Rebatimento Espectral) e a Formulação Analítica do Pente de Dirac

A amostragem analítica de um sinal contínuo x de t pode ser modelada de forma rigorosa como a multiplicação de x de t por um trem infinito e periódico de impulsos de Dirac, denominado pente de Dirac, representado por p de t:

O sinal amostrado x s de t é igual a x de t multiplicado pelo somatório, com o índice n variando de menos infinito a mais infinito, da função delta de Dirac avaliada em t menos n vezes o período de amostragem T s.

Pela propriedade fundamental da Transformada de Fourier, a multiplicação de dois sinais no domínio do tempo corresponde de forma inequívoca à convolução de seus respectivos espectros no domínio da frequência, escalonada pela constante de normalização:

O espectro do sinal amostrado X s de f é igual à Transformada de Fourier de x de t convoluída com a Transformada de Fourier do pente de Dirac p de t.

A Transformada de Fourier de um trem periódico de deltas de Dirac no tempo, por força da fórmula da soma de Poisson, resulta em outro trem de deltas de Dirac no domínio da frequência, cujos impulsos são ponderados pela taxa de amostragem f s e localizados em cada múltiplo inteiro k da frequência de amostragem f s:

A Transformada de Fourier de p de t é igual à taxa de amostragem f s multiplicada pelo somatório, com o índice k variando de menos infinito até mais infinito, do delta de Dirac avaliado em f menos k vezes f s.

Aplicando o operador de convolução entre o espectro original contínuo X de f e esse trem de impulsos na frequência, a propriedade de deslocamento do impulso de Dirac faz com que o espectro contínuo seja clonado em cada múltiplo inteiro k de f s. Obtém-se a magistral equação da replicação espectral:

X s de f é igual à taxa de amostragem f s multiplicada pelo somatório infinito, com o índice k variando de menos infinito até mais infinito, de X avaliado em f menos k vezes f s.

A intuição geométrica desta equação é assombrosa: amostrar um sinal no tempo cria infinitas réplicas fantasmas exatas do seu espectro original na frequência, centradas em cada múltiplo inteiro da taxa de amostragem f s.

Se a condição de Nyquist for violada — isto é, se a taxa de amostragem f s for menor ou igual ao dobro da frequência máxima —, a largura da base do espectro primário excederá o espaçamento entre as réplicas espectrais adjacentes. As saias do espectro original cruzarão o domínio das réplicas vizinhas, ocorrendo uma sobreposição aditiva irreversível de energias.

Este fenômeno destrutivo é denominado Aliasing, ou rebatimento espectral. Uma vez misturados os componentes de frequência, o algoritmo de reconstrução digital torna-se matematicamente cego à origem espectral da energia, sendo impossível separar o sinal original do conteúdo rebatido.

A frequência aparente rebatida no espectro observável de banda base é deduzida algebricamente pela distância da frequência do sinal original f zero em relação ao múltiplo inteiro k da taxa de amostragem mais próximo:

A frequência rebatida f de aliasing é igual ao módulo da diferença entre a frequência original f zero e o produto de k pela taxa de amostragem f s.

Considere a pegadinha clássica em exames acadêmicos e em sistemas de telecomunicações: injetar um tom puro e indesejado de mil e duzentos Hertz em um canal cuja taxa de conversão digital é restrita a dois mil Hertz.

A Frequência de Nyquist deste sistema — a barreira de contenção espectral — é de dois mil dividido por dois, ou seja, mil Hertz. O tom original de mil e duzentos Hertz excede claramente este limite de contenção.

Pela equação da replicação espectral, avaliando a réplica primária correspondente a k igual a um, temos: mil e duzentos Hertz menos dois mil Hertz resulta em menos oitocentos Hertz. No espectro observável de frequências reais, a magnitude é simétrica, de modo que a frequência rebatida torna-se o módulo de mil e duzentos menos dois mil, resultando exatamente em oitocentos Hertz.

A energia do tom originalmente em mil e duzentos Hertz rebate sobre a barreira dos mil Hertz, dobra-se para trás no espectro e emerge de forma cristalina no áudio reconstruído como um tom falsificado, audível e inabalável de oitocentos Hertz. Este é o sentido físico real do rebatimento: as frequências não desaparecem no vazio, elas assumem novos disfarces audíveis e destrutivos.

---

### 3. Reconstrução Ideal de Sinais (Fórmula de Whittaker-Shannon) e a Base Cardinal

Para resgatar o sinal contínuo subjacente x de t a partir de suas amostras digitais discretas x de n, deve-se extirpar completamente as réplicas espectrais infinitas geradas pela amostragem, isolando unicamente a banda base central original.

Isso exige multiplicar o espectro do sinal amostrado X s de f por um filtro passa-baixas ideal, conhecido na engenharia como filtro parede de tijolo, ou brick-wall filter. Este filtro analítico, denotado por H de f, atua como uma janela retangular centrada na origem, com largura igual a f s e amplitude igual ao inverso de f s para compensar o ganho de escala da amostragem:

H de f é igual a um dividido por f s para todo f cujo módulo seja menor ou igual a f s sobre dois, e vale zero para qualquer frequência cujo módulo seja estritamente maior do que f s sobre dois.

Pelo teorema da convolução, multiplicar o espectro na frequência por uma janela retangular equivale a convoluir no domínio do tempo o sinal amostrado x s de t com a Transformada de Fourier Inversa da resposta em frequência do filtro H de f.

A Transformada Inversa de Fourier de um pulso retangular contínuo no domínio da frequência é calculada analiticamente pela integração:

A resposta ao impulso contínua h de t é igual à integral definida, com f variando de menos f s sobre dois até mais f s sobre dois, de um dividido por f s multiplicado pela exponencial complexa de j vezes dois pi vezes f vezes t em relação à variável de integração d f.

Resolvendo esta integral elementar: a antiderivada é a exponencial complexa dividida por j vezes dois pi vezes t. Avaliando nos limites de integração e aplicando a clássica identidade de Euler — na qual a diferença entre duas exponenciais complexas conjugadas dividida por duas vezes a unidade imaginária j é o seno do argumento —, a expressão simplifica-se para:

A resposta ao impulso h de t é igual ao seno de pi vezes f s vezes t, tudo dividido por pi vezes f s vezes t.

Esta função transcendental é consagrada na literatura como a função seno cardinal normalizada, ou função sinc:

A função sinc de u é igual ao seno de pi vezes u, dividido por pi vezes u. Portanto, a resposta ao impulso do filtro ideal de reconstrução é simplesmente h de t igual a sinc avaliada em f s vezes t.

A operação de convolução contínua entre o trem de amostras x s de t e esta resposta ao impulso sinc produz a magistral e canônica Equação de Interpolação de Whittaker-Shannon:

O sinal contínuo reconstruído x de t é igual ao somatório, com o índice n variando de menos infinito a mais infinito, da amostra discreta x de n multiplicada pela função sinc avaliada no argumento f s vezes t menos n, o que equivale à sinc da fração t menos n vezes T s, tudo dividido pelo período T s.

Esta fórmula encerra uma propriedade matemática fundamental denominada ortogonalidade cardinal. Quando avaliamos a função sinc em um instante t igual a um múltiplo inteiro m vezes T s, o argumento t menos n vezes T s dividido por T s torna-se exatamente a diferença entre os inteiros m e n:

Se m for igual a n, sinc de zero é rigorosamente igual a um. 

Por outro lado, se m for diferente de n, o argumento é um número inteiro não nulo k. O numerador torna-se o seno de pi vezes k, o qual se anula identicamente para qualquer número inteiro, enquanto o denominador permanece finito. Portanto, a função sinc vale rigorosamente zero sobre todos os outros instantes de amostragem m vezes T s onde m é diferente de n.

Isso garante ausência absoluta de interferência intersimbólica nos momentos exatos de leitura das amostras. A função sinc gerada por cada amostra individual atinge o topo de sua amplitude exatamente no seu instante nominal e desaba para zero nos instantes de todas as amostras vizinhas. O sinal contínuo entre as amostras brota de forma orgânica e matematicamente perfeita pela superposição ondulatória infinita de todas as saias das funções sinc adjacentes.

A armadilha estrutural, no entanto, revela que a função sinc expande-se analiticamente do passado remoto menos infinito ao futuro absoluto mais infinito. Para reconstruir com exatidão matemática o valor entre duas amostras no presente, o filtro de reconstrução precisaria aguardar eternamente todas as amostras futuras do universo e integrar a sua energia, o que inviabiliza sistemas causais que operam em tempo real. 

A engenharia contorna esta impossibilidade prática aproximando a filtragem através de truncações janeladas, interpolações de ordem inferior com mantenedores de ordem zero, e a suavização final através de capacitores e indutores em filtros analógicos de reconstrução anti-imagem.

#### Roteiro Prático e Instruções para o Jupyter Notebook no Laboratório 2

No repositório da disciplina, o estudo do Teorema da Amostragem encontra-se no notebook assets barra labs barra le zero dois sublinhado sampling hífen theorem barra le zero dois sublinhado p t zero dois sublinhado sampling hífen theorem ponto ipynb.

Antes de executar, três avisos. O notebook acrescenta dois níveis acima ao caminho de busca, para importar a pasta lib. O som usado está em assets barra sounds, no arquivo freddy ponto wav. E as células de animação usam IPython ponto display, então rodam dentro do Jupyter.

Primeira etapa: o trem de sincs. Define-se o tempo inicial como dez elevado a menos doze, para evitar a divisão por zero, o tempo final como dez segundos e mil pontos com n p ponto linspace. A taxa de amostragem f s vale vinte Hertz e T s vale um sobre f s. O vetor n vai de zero a duzentos, isto é, o inteiro de tf menos ti dividido por T s, mais um. Em cada passo de um laço, calcula-se n p ponto sinc de f s vezes t menos n T s e anima-se o gráfico. No NumPy, sinc de x já é seno de pi x dividido por pi x.

Segunda etapa: reconstrução animada. O sinal analógico é um seno de dois Hertz entre zero e quatro segundos, com mil pontos, o que dá uma taxa de mil sobre quatro, isto é, duzentos e cinquenta amostras por segundo no vetor denso. Toma-se f s igual a cinco vezes f, isto é, dez Hertz. O passo de decimação Nd vale duzentos e cinquenta dividido por dez, vinte e cinco, e as amostras são yn igual a y com passo vinte e cinco. A reconstrução é um laço: começa com x igual a zeros e, para cada amostra, soma yn de nn vezes n p ponto sinc de f s vezes t menos nn T s. Ou seja, a reconstrução de Whittaker-Shannon é feita por acumulação em laço, e não por matriz com broadcasting. A célula seguinte compara em três gráficos o sinal original, o reconstruído e as amostras com plt ponto stem.

Terceira etapa: frequência mínima. Para o seno de dois Hertz, a taxa de Nyquist exige f s maior que quatro Hertz. Com f s igual a quatro Hertz cravado, as amostras caem nos zeros do seno e a reconstrução se anula. O notebook recomenda quatro vírgula zero um Hertz.

Quarta etapa: áudio real. O notebook lê freddy ponto wav com a função audioread da biblioteca do curso, que devolve os canais nas linhas. A saída informa taxa de amostragem de catorze mil Hertz e dois canais com cento e oitenta e seis mil, quinhentas e onze amostras cada. Em seguida, pula uma de cada oito amostras no último eixo, que é o tempo, com x_audio entre colchetes, reticências, dois pontos, dois pontos, fator oito. A taxa cai para mil setecentos e cinquenta Hertz e a saída mostra dois canais com vinte e três mil, trezentas e catorze amostras. Uma versão anterior do notebook fatiava o eixo dos canais e mantinha só um canal; isso foi corrigido.

Quinta etapa: espectro e reconstrução do áudio. A célula final usa o canal esquerdo, x_audio de zero, calcula a FFT com scipy, plota o espectro de zero a vinte e dois mil Hertz e reconstrói o sinal subamostrado com a função resample do scipy ponto signal. Ela imprime que, para a estimativa de quinze mil Hertz de frequência máxima, a taxa de Nyquist é de trinta mil Hertz, e que a taxa do arquivo, catorze mil Hertz, não atende a essa estimativa.

Exercício opcional, que não está no notebook: aliasing de um tom. Gere um seno de mil e duzentos Hertz com f s de dois mil Hertz, por um segundo, calcule a FFT e plote a primeira metade. O pico aparece em oitocentos Hertz, pois dois mil menos mil e duzentos é oitocentos, que é o espelho do tom ao redor da frequência de Nyquist de mil Hertz.

---

## CAPÍTULO III — SINAIS EM TEMPO DISCRETO, CONVOLUÇÃO E SISTEMAS LTI

### 1. Catálogo de Sinais Fundamentais em Tempo Discreto

O tratamento algorítmico da teoria de Sistemas Lineares e Invariantes no Tempo assenta sobre uma taxonomia rigorosa de primitivas matemáticas de excitação discreta.

A fundação elementar é o Impulso Unitário de Kronecker, denotado pela letra grega delta de n entre colchetes. Ele difere fundamentalmente do delta de Dirac analógico, que possui amplitude infinita. O impulso de Kronecker é definido estritamente por uma magnitude de um no instante n igual a zero, e magnitude zero em todos os outros instantes onde n é diferente de zero. A propriedade cardeal do impulso é o peneiramento ou amostragem escalar: multiplicar qualquer sequência genérica x de n por delta de n menos k silencia todos os valores exceto no instante k, permitindo a extração unitária exata do valor x de k.

O Degrau Unitário, denotado por u de n entre colchetes, vale um para todo índice n maior ou igual a zero, e vale zero para todo índice n estritamente negativo. Ele atua como a chave liga e desliga causal dos sistemas digitais. Suas ligações com o impulso formam pontes matemáticas elegantes: a soma acumulada de todos os impulsos passados forja o degrau unitário; inversamente, a diferença analítica de primeira ordem atrasada — isto é, u de n menos u de n menos um — quebra o degrau de volta a um impulso unitário isolado delta de n.

A Exponencial Decrescente, representada por a elevado a n multiplicado pelo degrau u de n, encapsula as oscilações naturais e tempos de dissipação de memória infinita em filtros digitais IIR. A fronteira inquebrável de estabilidade estrita de energia de entrada limitada para saída limitada dita que um filtro permanecerá estável se, e somente se, a soma absoluta dos coeficientes de sua resposta ao impulso convergir. A série geométrica somando a magnitude de a elevado a n converge se, e somente se, o módulo da base a for estritamente menor do que um. Este é o limite imutável que separa sistemas estáveis da divergência exponencial catastrófica.

Para análise harmônica, a Senoide Discreta subordina a frequência vibratória analógica f zero, em Hertz, à cadência da taxa de amostragem f s. Essa relação transmuta a medida para a frequência angular digital, representada pela letra grega ômega zero, expressa em radianos por amostra, através da relação: ômega zero é igual a duas vezes pi vezes a frequência analógica f zero, tudo dividido pela taxa de amostragem f s. Esta dependência expõe a relatividade temporal das oscilações em vetores numéricos isolados.

Por fim, no plano estocástico, a modelagem de perturbações fundamenta-se em sinais não determinísticos. O Ruído Gaussiano, parametrizado por uma média mi e uma variância sigma ao quadrado, materializa a soma de variáveis aleatórias independentes via Teorema Central do Limite, espelhando fielmente o ruído térmico de agitação de elétrons em resistores e circuitos. Complementarmente, o Ruído Uniforme, com distribuição plana entre limites pré-definidos, simula analiticamente o erro de truncamento decorrente da quantização em estágios de conversores analógico-digitais.

---

### 2. A Teoria da Convolução em Uma e Duas Dimensões e a Prova Algébrica do Suporte

A Convolução é o coração do Processamento de Sinais, traduzindo a intrincada superposição temporal e os ecos inerentes a sistemas dotados de memória. No domínio contínuo, a integral de convolução entre uma entrada x de t e uma resposta ao impulso h de t é dada pela integral de menos infinito a mais infinito de x de tau multiplicado por h de t menos tau em relação à variável auxiliar tau.

O desdobramento destas operações dita o ritmo de uma valsa espacial em quatro tempos estritos:

Primeiro tempo: define-se uma variável auxiliar muda de integração, a letra grega tau.

Segundo tempo: para calcular a saída em um instante t, inverte-se horizontalmente a resposta ao impulso em torno do eixo, obtendo h de menos tau.

Terceiro tempo: desliza-se essa função invertida para a frente no tempo até o instante atual t, gerando a janela de sobreposição temporal h de t menos tau.

Quarto tempo: multiplica-se a entrada excitante x de tau pelos valores correspondentes deste filtro espelhado e calcula-se a integral da área líquida contida sob a curva deste produto.

A formulação discreta, que permite a execução direta em processadores digitais, espelha a versão contínua através de um somatório cruzado:

A saída discreta y de n é igual à somatória, com o índice k variando de menos infinito a mais infinito, da entrada x de k multiplicada pela resposta ao impulso h avaliada em n menos k.

O operador de convolução atende estritamente às propriedades comutativa (x convolvido com h é idêntico a h convolvido com x), associativa (x convolvido com a convolução de h um e h dois é idêntico à convolução de x com h um, convolvida com h dois) e distributiva em relação à adição.

#### Dedução Algébrica do Comprimento da Sequência Convolvida

O comprimento natural da sequência de saída gerada pela convolução linear é uma armadilha frequente na prática de computação. Se injetarmos um vetor de entrada contíguo x de n com N amostras — definido estritamente no intervalo de índices de k igual a zero até k igual a N menos um — em um filtro com resposta ao impulso h de n contendo M amostras — definido no intervalo de índices de zero até M menos um —, qual será a extensão exata do vetor de saída y de n?

A resposta matemática decorre da análise dos limites de sobreposição dos suportes temporais. Pela definição da somatória, o produto x de k multiplicado por h de n menos k só produz termos não nulos quando ambos os fatores forem simultaneamente não nulos:

Para o sinal de entrada, o índice k deve satisfazer: zero menor ou igual a k, e k menor ou igual a N menos um.

Para a resposta ao impulso deslocada, o argumento n menos k deve satisfazer: zero menor ou igual a n menos k, e n menos k menor ou igual a M menos um.

Isolando o índice n na segunda desigualdade, somando k em todos os membros: k deve ser menor ou igual a n, e n deve ser menor ou igual a k mais M menos um.

Para encontrar o instante da primeira amostra não nula na saída, avaliamos o menor valor possível de k, que é zero. O limite inferior de n torna-se imediatamente n igual a zero.

Para encontrar o instante da última amostra não nula possível, avaliamos o maior valor possível que o índice k pode assumir no sinal de entrada, que é N menos um. Substituindo k por N menos um no limite superior de n, obtemos: o índice máximo de n é N menos um mais M menos um, o que simplifica algebricamente para N mais M menos dois.

Como o índice n inicia em zero e estende-se continuamente até N mais M menos dois, o número total de elementos contidos neste intervalo fechado é o índice final menos o índice inicial mais um: N mais M menos dois menos zero mais um, resultando rigorosamente em N mais M menos uma amostras.

O fundamento físico deste resultado é límpido: a excitação inicial preenche progressivamente a memória do filtro ao longo de M estágios de retardo. Quando a última amostra da entrada atinge o sistema no instante N menos um, o eco residual necessita de mais M menos um passos de tempo para esvaziar completamente a linha de retardo, estendendo a reverberação sonoro-espacial pela duração consolidada de N mais M menos uma amostras.

#### Teorema da Estabilidade Entrada Limitada Saída Limitada (BIBO)

A caracterização analítica da estabilidade de um sistema Linear e Invariante no Tempo depende da convergência absoluta de sua resposta ao impulso. Dizemos que um sistema atende ao critério de Entrada Limitada para Saída Limitada — conhecido pela sigla em inglês BIBO — se qualquer entrada x de n cuja magnitude seja estritamente limitada por uma constante real finita B de x produzir uma saída y de n cuja magnitude seja igualmente limitada por uma constante finita B de y.

Tomando o módulo da equação de convolução e aplicando a desigualdade triangular de Cauchy-Schwarz:

O módulo de y de n é menor ou igual à somatória, com k de menos infinito a mais infinito, do módulo de h de k multiplicado pelo módulo de x de n menos k.

Como a entrada é limitada por B de x, podemos substituir o módulo de x por B de x e colocar esta constante finita para fora do somatório:

O módulo de y de n é menor ou igual a B de x multiplicado pela somatória de menos infinito a mais infinito do módulo absoluto de h de k.

Desta inequação extrai-se a condição necessária e suficiente incondicional: a saída y de n será finita para qualquer entrada limitada se, e somente se, a somatória de todos os coeficientes absolutos da resposta ao impulso convergir para um valor finito S.

No caso clássico de um filtro com resposta exponencial decrescente h de n igual a a elevado a n multiplicado pelo degrau unitário u de n, a somatória dos módulos absolutos torna-se a série geométrica infinita da razão módulo de a, a qual converge para um dividido por um menos o módulo de a se, e somente se, o módulo da base a for estritamente menor do que a unidade. Se o módulo de a for maior ou igual a um, a soma diverge para infinito e o sistema desestabiliza-se catastroficamente.

#### Convolução Bidimensional e Processamento Espacial de Imagens

No domínio de matrizes digitais em Visão Computacional, a convolução bidimensional estende o conceito de sobreposição temporal para tensores espaciais de coordenadas de linhas i e colunas j. A saída y nas posições i e j é dada pelo duplo somatório de x nas posições m e n multiplicado pelo kernel K avaliado em i menos m e j menos n.

Operadores diferenciais clássicos mapeiam descontinuidades de iluminação aplicando aproximações por diferenças finitas do vetor gradiente bidimensional. O operador de Sobel vertical utiliza a matriz três por três com primeira coluna menos um, menos dois, menos um; coluna central com zeros; e terceira coluna mais um, mais dois, mais um. Ao deslizar sobre a imagem, este kernel calcula a derivada espacial horizontal d I sobre d x, destacando bordas verticais. 

Reciprocamente, o operador de Sobel horizontal posiciona a linha superior como menos um, menos dois, menos um; linha intermediária de zeros; e linha inferior com mais um, mais dois, mais um, calculando a derivada vertical d I sobre d y e destacando contornos horizontais. A magnitude total do gradiente em cada pixel é calculada pela raiz quadrada da soma dos quadrados dos gradientes horizontal e vertical.

---

### 3. Sistemas Lineares e Invariantes no Tempo, a Resposta ao Impulso e Acústica de Ambientes

O axioma inquebrantável da disciplina baseia-se na constatação de que qualquer sinal discreto x de n pode ser representado de forma exata como uma superposição linear de infinitos impulsos de Kronecker sequencialmente atrasados e ponderados por suas respectivas amplitudes: x de n é igual à somatória de x de k multiplicado por delta de n menos k.

Da união incondicional das premissas de Linearidade — onde a resposta a uma soma de entradas é igual à soma das respostas individuais — e da Invariância no Tempo — onde um atraso no sinal de excitação produz o mesmo atraso na resposta de saída sem alterar sua forma —, nasce o Teorema Fundamental dos Sistemas Lineares e Invariantes no Tempo:

A caracterização integral, absoluta e unívoca de todo o comportamento dinâmico de um sistema recai sumariamente em avaliar a sua reação a um único impulso fundamental singular aplicado em repouso. Denomina-se a esta sequência a Resposta ao Impulso do sistema, representada por h de n. A partir do seu conhecimento, a resposta do sistema a qualquer outro sinal de excitação x de n pode ser simulada simplesmente calculando a convolução discreta de x de n com h de n.

Na acústica arquitetural moderna, a resposta ao impulso de ambientes captura os complexos padrões de reflexão sonora de catedrais, teatros e salas de concerto. Ao disparar uma fonte percussiva impulsiva no palco e gravar o padrão residual de micro-reflexões nas paredes, obtém-se o vetor h de n do espaço físico. 

Convoluindo uma gravação musical puramente seca, capturada em estúdio anecoico, com esta resposta ao impulso, o áudio resultante soará exatamente como se a música estivesse sendo executada dentro daquela catedral específica. O mesmo princípio fundamenta as respostas ao impulso de gabinetes de guitarra, que emulam a acústica de alto-falantes e cones magnéticos.

Duas armadilhas práticas merecem atenção destacada:

Primeira armadilha: na conversão de um sinal estéreo com defasagens entre os canais esquerdo e direito para um sinal monoaral, a engenharia comumente adota a média aritmética simples, somando canal esquerdo e canal direito e dividindo por dois. Se houver descompasso espacial de fase onde componentes estejam defasados em cento e oitenta graus — isto é, quando o canal direito é exatamente o negativo do canal esquerdo —, a soma vetorial cancelará mutuamente as ondas, provocando o fenômeno de cancelamento de fase, que engole componentes centrais vitais da mixagem, silenciando vozes e baixos.

Segunda armadilha: alterar de forma desavisada a taxa de amostragem na reprodução de um arquivo digital. Ler um vetor gravado a quarenta e quatro mil e cem Hertz em uma placa configurada para oitenta e oito mil e duzentos Hertz esgotará as amostras na metade do tempo cronometrado. Isso acelera a reprodução em duas vezes e dobra todas as frequências fundamentais, transpondo todo o conteúdo musical em uma oitava inteira para cima, produzindo o conhecido efeito esquilo.

#### Roteiro Prático e Instruções para o Jupyter Notebook no Laboratório 3

No repositório da disciplina, os experimentos de sinais elementares, convolução contínua, convolução discreta unidimensional, filtragem acústica e convolução bidimensional estão distribuídos nos notebooks da pasta assets barras labs barras le zero três sublinhado discrete hífen time hífen signals, especificamente nos arquivos le zero três sublinhado basic hífen signal hífen library ponto ipynb, le zero três sublinhado convolution sublinhado Wallison ponto ipynb e no script le zero três sublinhado convolution sublinhado Wallison ponto py.

Para executar estes procedimentos no ambiente Jupyter com sucesso, o usuário deve seguir o seguinte guia de passos e células:

Primeiro passo: geração do catálogo de sinais fundamentais no Jupyter. No notebook de biblioteca básica, utiliza-se a função primitiva da disciplina SIGNALgenerate. Para criar um impulso de Kronecker com cinquenta amostras, chama-se a função passando o tamanho cinquenta e o tipo entre aspas como delta. Para gerar um degrau unitário causal, passa-se o tipo step. Para criar uma exponencial decrescente estável, passa-se o tipo exp com o parâmetro de decaimento a igual a zero vírgula oito. Plota-se cada sinal gerado com a função p l t ponto stem para confirmar visualmente as características discretas.

Segundo passo: animação e interação da convolução contínua. No notebook de convolução de Wallison, utilizam-se os módulos interativos do pacote ipywidgets, importando interact e FloatSlider. Define-se o sinal de entrada contínuo x de tau como um pulso retangular unitário de zero a três segundos, e a resposta ao impulso h de tau como um pulso retangular mais estreito de zero a um vírgula cinco segundos. 

Configura-se a função interativa de plotagem que recebe o parâmetro de deslocamento t do slider: calcula-se h de t menos tau invertendo o vetor de tempo tau, multiplica-se ponto a ponto por x de tau gerando o produto de sobreposição, e calcula-se a área sob a curva através da função de integração numérica n p ponto trapezoid do NumPy. O gráfico superior exibe a função deslizante e a área hachurada preenchida com a função p l t ponto fill sublinhado between, enquanto o gráfico inferior registra a curva integral acumulada y de t com um marcador circular acompanhando a posição do tempo atual t. O usuário arrasta o controle deslizante no Jupyter e testemunha a construção dinâmica contínua da convolução.

Terceiro passo: inspeção numérica da convolução discreta passo a passo. Cria-se um vetor de entrada simples x com valores binários e um filtro detector de transições kernel com três elementos: um, zero e menos um. Executa-se um laço for que imprime no console do Jupyter o alinhamento espacial do filtro sobre cada fatia contígua do sinal de três elementos, exibindo o produto elemento a elemento e a soma escalar resultante. Ao final, compara-se o vetor resultante com a função nativa n p ponto convolve passando o modo valid, comprovando a correspondência numérica perfeita dos pontos onde o filtro encontrou as bordas de transição do sinal.

Quarto passo: experimento acústico com áudio real e filtros LTI. No mesmo ambiente, importa-se o leitor de áudio wavfile do pacote scipy ponto io, e a classe Audio do módulo IPython ponto display. Carrega-se o arquivo de áudio local localizado em sounds barras freddy ponto wav ou audio sublinhado exemplo ponto wav.

Converte-se o array de áudio para ponto flutuante de precisão simples normalizado entre menos um e mais um: se os dados forem inteiros de dezesseis bits, divide-se por trinta e dois mil setecentos e sessenta e sete vírgula zero. Se o arquivo possuir dois canais estéreo, seleciona-se apenas o canal esquerdo para operar em mono.

Projeta-se um filtro de eco acústico: calcula-se o atraso de duzentos milissegundos em amostras multiplicando zero vírgula dois pela taxa de amostragem f s. Aloca-se um vetor kernel de eco preenchido com zeros de tamanho atraso mais um, fixando o primeiro elemento como um vírgula zero correspondente ao som direto, e a última posição como zero vírgula seis correspondente à reflexão atenuada.

Aplica-se a convolução discreta linear através do comando n p ponto convolve passando o áudio original e o filtro de eco com o parâmetro mode igual a same. Para evitar estalos por ceifamento de amplitude, divide-se o resultado pelo seu pico máximo absoluto caso ele exceda a unidade. 

Executa-se o comando display passando a classe Audio com o vetor filtrado e a taxa de amostragem original, permitindo ao usuário escutar no próprio navegador o eco sonoro gerado pela convolução. Testa-se em seguida o filtro de média móvel passa-baixas de quinze amostras gerado com n p ponto ones de quinze dividido por quinze, escutando a perda imediata de brilho e o som acusticamente abafado resultante da atenuação das altas frequências.

Quinto passo: convolução bidimensional sobre tensores de imagem. Utiliza-se a função convolve dois d do pacote scipy ponto signal. Constrói-se uma matriz sintética de dez por dez pixels com fundo escuro zero, preenchendo um quadrado intermediário com intensidade clara duzentos e um miolo interno escuro cinquenta. 

Definem-se as matrizes tridimensionais dos filtros de Sobel vertical e horizontal em arrays bidimensionais do NumPy. Executa-se a função convolve dois d passando a matriz base e o kernel de Sobel com o modo same. Plota-se o resultado na tela com p l t ponto imshow utilizando o mapa de cores cinza cmap igual a gray. O usuário constata que as arestas verticais acendem-se intensamente no primeiro filtro e as horizontais no segundo, comprovando a universalidade do operador de convolução desde o áudio unidimensional até o processamento computacional de matrizes visuais.

---

## CAPÍTULO IV — ÁUDIO DIGITAL, TIMBRE E SÍNTESE FÍSICA DE KARPLUS-STRONG

### 1. Do Vetor de Números ao Som Audível

Um arquivo de áudio digital descompactado nada mais é do que um fluxo sequencial contíguo de números reais na memória, tipicamente normalizados no intervalo simétrico de menos um vírgula zero até mais um vírgula zero. 

A frequência percebida pelo ouvido, denotada por f zero em Hertz, subordina-se à cadência de leitura governada pela taxa de amostragem f s e ao período digital fundamental, representado pela letra maiúscula P, que indica o número de amostras contidas em cada ciclo completo da forma de onda. A relação matemática fundamental é:

O período digital P, em amostras por ciclo, é igual à taxa de amostragem f s dividida pela frequência desejada f zero. A duração total em segundos é igual ao número total de amostras do vetor dividido pela taxa de amostragem f s.

Surge um contraste instrutivo ao analisar dois cenários distintos envolvendo a taxa de amostragem:

No primeiro cenário, recalculamos o gerador sintético de áudio. Se desejamos gerar uma nota Lá com frequência de quatrocentos e quarenta Hertz e dobramos a taxa de amostragem de quarenta e quatro mil e cem para oitenta e oito mil e duzentos Hertz, recalculamos a fórmula. O período digital P dobra de cem amostras para duzentas amostras por ciclo. A representação digital fica duas vezes mais refinada, mas a frequência audível nos alto-falantes e a duração em segundos permanecem escrupulosamente as mesmas.

No segundo cenário, reproduzimos incorretamente um vetor já gravado. Se pegamos o vetor de amostras gravado originalmente a quarenta e quatro mil e cem Hertz e o enviamos para um conversor digital-analógico configurado para operar a oitenta e oito mil e duzentos Hertz, as amostras expiram duas vezes mais rápido. O som dura metade do tempo e, como o número de amostras por ciclo estava congelado no arquivo original, a frequência emitida dobra de quatrocentos e quarenta para oitocentos e oitenta Hertz, subindo uma oitava inteira.

---

### 2. Decomposição Harmônica e a Definição de Timbre

Uma onda senoidal pura em frequência f zero é acusticamente estéril e monótona. No domínio da Transformada de Fourier, seu espectro exibe uma única componente pontiaguda na frequência fundamental. 

Porém, se preenchermos um bloco de memória de tamanho P com números aleatórios — correspondentes a ruído branco estocástico — e repetirmos ciclicamente esse bloco idêntico em um laço contínuo no tempo, forçamos o sinal a obedecer rigorosamente a um período fundamental de P amostras. 

Pelas propriedades da Transformada de Fourier, essa imposição de periodicidade cristaliza a energia do sinal não apenas na fundamental f zero, mas gera instantaneamente uma cascata de harmônicos inteiros perfeitamente espaçados em duas vezes f zero, três vezes f zero, quatro vezes f zero, e assim por diante. 

A distribuição relativa de amplitudes e fases ao longo desta série harmônica define a assinatura psicoacústica que chamamos de Timbre. Enquanto uma onda dente-de-serra possui amplitudes que decaem na proporção de um dividido pela ordem do harmônico, o ruído em repetição preserva uma rica e áspera densidade espectral.

---

### 3. O Algoritmo de Karplus-Strong para Síntese de Cordas Dedilhadas

Em mil novecentos e oitenta e três, Kevin Karplus e Alex Strong publicaram no Computer Music Journal um artigo seminal propondo uma formulação matemática elegante para síntese de áudio baseada em modelos físicos discretos, simulando o comportamento de cordas dedilhadas — técnica que posteriormente patentearam nos Estados Unidos.

A evolução do algoritmo organiza-se em três etapas históricas:

Etapa um: a versão Karplus-Strong um, correspondente à repetição pura do vetor. Inicializa-se um vetor de tamanho P com ruído aleatório entre menos um e mais um, simulando o ataque percussivo caótico da palheta contra a corda de náilon. O vetor é realimentado ciclicamente sem perdas. O som resultante soa metálico, contínuo e zumbidor, assemelhando-se a um oscilador de teclado eletrônico sem qualquer amortecimento ou naturalidade acústica.

Etapa dois: as versões Karplus-Strong dois e três, correspondentes ao decaimento exponencial simples de primeira ordem. Insere-se um coeficiente atenuador, a letra grega alfa, estritamente menor do que um, multiplicando o sinal atrasado: y de n é igual a alfa multiplicado por y de n menos P. O som agora decai e morre com o tempo. Contudo, como o fator alfa atenua todas as frequências exatamente na mesma proporção, tanto as baixas quanto as altas frequências desvanecem simultaneamente. Isso gera um timbre plástico e oco, ausente da física real dos instrumentos musicais, onde o atrito interno e a resistência da madeira amortecem as altas frequências com muito mais rapidez do que as fundamentais graves.

Etapa três: a versão canônica Karplus-Strong Média, publicada em mil novecentos e oitenta e três. A grande inovação consistiu em introduzir um filtro passa-baixas elementar de duas amostras dentro da malha de realimentação. A cada ciclo, o valor que retorna à linha de atraso é a média aritmética simples entre duas amostras consecutivas:

O valor sintetizado y de n é igual à entrada impulsiva x de n, mais o coeficiente alfa de decaimento multiplicado pela média entre y de n menos M e y de n menos M menos um. Em termos diretos: y de n é igual a x de n, mais alfa vezes a fração com numerador y de n menos M somado a y de n menos M menos um, e denominador dois.

#### Modelagem em Transformada Z e Dedução Analítica do Atraso de Meia Amostra

Para compreender analiticamente a física da malha de Karplus-Strong, modelamos a equação recursiva no domínio da frequência complexa utilizando a Transformada Z. 

Tomando a Transformada Z em ambos os lados da equação a diferenças: Y de z é igual a X de z, mais alfa multiplicado por z elevado a menos M, multiplicado pela resposta do filtro de média passa-baixas H sublinhado L P de z, tudo multiplicado por Y de z.

Isolando a relação entre a saída Y de z e a entrada excitadora X de z, obtemos a Função de Transferência do sistema em malha fechada:

H de z é igual a Y de z dividido por X de z, o que resulta na fração com numerador um, e denominador dado por: um menos alfa vezes z elevado a menos M vezes a função H sublinhado L P de z.

O filtro de média aritmética simples de duas amostras adjacentes é definido pela equação de resposta ao impulso h de n igual a meio para n igual a zero e meio para n igual a um. A sua função de transferência em Transformada Z é:

H sublinhado L P de z é igual a meio mais meio vezes z elevado a menos um, o que equivale a um mais z elevado a menos um, tudo dividido por dois.

Para avaliar a sua resposta em frequência contínua, substituímos a variável z pela exponencial complexa e elevado a j ômega, onde ômega é a frequência angular digital em radianos por amostra:

H sublinhado L P de e elevado a j ômega é igual a um mais e elevado a menos j ômega, tudo dividido por dois.

Fatorando o termo de fase linear e elevado a menos j ômega sobre dois para fora do binômio, a expressão reescreve-se como:

A exponencial de menos j ômega sobre dois, multiplicada pela fração cujo numerador é a exponencial de mais j ômega sobre dois somada à exponencial de menos j ômega sobre dois, e cujo denominador é dois.

Pela identidade fundamental de Euler, a soma de duas exponenciais complexas conjugadas dividida por dois é rigorosamente igual ao cosseno do argumento. Deste modo, a resposta em frequência do filtro de média decompõe-se de forma analítica exata em magnitude e fase:

H sublinhado L P de e elevado a j ômega é igual ao cosseno de ômega sobre dois, multiplicado pela exponencial complexa de menos j ômega sobre dois.

Esta dedução revela dois fatos matemáticos cruciais:

Primeiro fato: a resposta de magnitude é o módulo do cosseno de ômega sobre dois. Na frequência zero — corrente contínua —, o cosseno de zero vale um, proporcionando ganho unitário sem atenuação. Na frequência de Nyquist, onde ômega atinge pi radianos por amostra, o cosseno de pi sobre dois desaba para rigorosamente zero. Isso prova por que o filtro elimina as altas frequências a cada volta na malha, gerando o amortecimento ressonante doce característico das cordas dedilhadas.

Segundo fato: a resposta de fase angular é puramente linear, dada por teta de ômega igual a menos ômega sobre dois. O retardo de grupo temporal, definido pelo negativo da derivada da fase em relação à frequência angular — menos d teta sobre d ômega —, resulta exatamente no valor constante de meio: meia amostra temporal, ou zero vírgula cinco amostras, em todas as frequências do espectro.

Portanto, o atraso total experimentado pela onda sonora a cada volta completa pela malha de realimentação não é apenas o tamanho inteiro M do buffer de memória, mas sim M somado a zero vírgula cinco amostras do filtro de média:

O período digital acústico total da malha P é igual a M mais zero vírgula cinco amostras.

Consequentemente, para afinar uma corda na frequência fundamental desejada f zero a uma taxa de amostragem f s, o período acústico total ideal é f s dividido por f zero. Subtraindo o retardo intrínseco de zero vírgula cinco amostras introduzido pela média, derivamos a equação de sintonia exata para o comprimento inteiro M do buffer:

O atraso M que o buffer de memória deve alocar é igual ao arredondamento para o número inteiro mais próximo da quantidade: a taxa de amostragem f s dividida pela frequência fundamental desejada f zero, menos zero vírgula cinco.

#### Compensação Dinâmica de Decaimento e Erro de Afinação em Cents

Outro desafio surge na sustentação de notas diferentes: notas agudas possuem comprimentos de buffer M muito pequenos, o que significa que elas completam dezenas de voltas na malha de realimentação no mesmo intervalo de um segundo em comparação com notas graves. Se o fator alfa for fixo, as notas agudas morrerão de forma quase instantânea. 

Para equalizar a duração das notas, utiliza-se a técnica de compensação dinâmica de decaimento. Fixa-se um valor de referência alfa ref para um comprimento de buffer de referência M ref, e calcula-se o alfa específico de cada nota elevando alfa ref à potência fracionária dada por M dividido por M ref:

O coeficiente alfa da nota é igual a alfa de referência elevado à potência M dividido por M de referência.

Por fim, deparamo-nos com o problema da quantização de afinação e o erro em cents. Na memória digital, o comprimento M do vetor deve ser obrigatoriamente um número inteiro de índices. O período total da malha resultante torna-se esse inteiro M somado a zero vírgula cinco amostras do filtro. Arredondar o tamanho do buffer para o inteiro mais próximo introduz um desvio de afinação que pode ser mensurado em cents pela fórmula:

O desvio em cents é igual a mil e duzentos multiplicado pelo logaritmo na base dois da razão entre a frequência real sintetizada e a frequência nominal desejada.

Para ilustrar este fenômeno, considere os seguintes quatro casos comparativos deduzidos e conferidos em laboratório:

Primeiro caso, nota Ré dois de violão, com frequência nominal de setenta e três vírgula quarenta e dois Hertz a uma taxa de quarenta e quatro mil e cem Hertz. O período acústico total da onda seria de seiscentos vírgula sessenta e cinco amostras. Descontando meia amostra do filtro de média, o atraso ideal do buffer seria seiscentos vírgula quinze amostras, que é arredondado para o inteiro seiscentos e um. Quando o buffer de seiscentos e um opera com o filtro, o ciclo acústico total torna-se seiscentos e um vírgula cinco amostras. A frequência resultante é quarenta e quatro mil e cem dividido por seiscentos e um vírgula cinco, resultando em setenta e três vírgula trinta e um Hertz, com desvio de apenas menos dois vírgula seis cents.

Segundo caso, nota Lá quatro, com frequência nominal de quatrocentos e quarenta Hertz. O período acústico total é de cem vírgula vinte e duas amostras. Subtraindo meia amostra temos noventa e nove vírgula setenta e duas, arredondado para o inteiro cem. Com o acréscimo de meia amostra do filtro, o ciclo total passa a cem vírgula cinco amostras. A frequência obtida é de quatrocentos e trinta e oito vírgula oitenta Hertz, com erro de menos quatro vírgula sete cents.

Terceiro caso, nota Dó cinco, com frequência nominal de quinhentos e vinte e três vírgula vinte e cinco Hertz. O período acústico total é de oitenta e quatro vírgula vinte e oito amostras. Subtraindo meia amostra temos oitenta e três vírgula setenta e oito, arredondado para oitenta e quatro. Com a meia amostra do filtro, o ciclo efetivo passa a oitenta e quatro vírgula cinco amostras, gerando quinhentos e vinte e um vírgula oitenta e nove Hertz, com desvio de menos quatro vírgula cinco cents.

Quarto caso, nota Sol cinco, com frequência nominal de setecentos e oitenta e três vírgula noventa e nove Hertz. O período acústico total é de cinquenta e seis vírgula vinte e cinco amostras. Subtraindo meia amostra temos cinquenta e cinco vírgula setenta e cinco, arredondado para o inteiro cinquenta e seis. Com a meia amostra do filtro, o ciclo acústico passa a cinquenta e seis vírgula cinco amostras, fazendo a frequência sintetizada cair para setecentos e oitenta vírgula cinquenta e três Hertz, deflagrando um erro agressivo de menos sete vírgula seis cents.

Erros superiores a cinco cents cruzam o limiar de discriminação do ouvido treinado, gerando batimentos e desafinações audíveis. Para sanar esta limitação de hardware inteiro, os pesquisadores David Jaffe e Julius Smith propuseram em mil novecentos e oitenta e três o acoplamento de filtros passa-tudo fracionários, ou Fractional Delay Filters, com função de transferência dada por H sublinhado a p de z igual à fração com numerador C mais z elevado a menos um, e denominador um mais C vezes z elevado a menos um. Este filtro digital possui ganho unitário em todas as frequências e permite introduzir um atraso de fase contínuo e fracionário ajustando o coeficiente C, garantindo afinação microscópica contínua sem distorcer o timbre.

Na síntese polifônica de acordes complexos — como o famoso Acorde de Hendrix formado pelas notas Mi dois, Si dois, Mi três, Sol sustenido três, Ré quatro e Sol quatro —, múltiplas vozes são geradas em separado e somadas linearmente. Para evitar distorções por ceifamento, ou clipping, onde os valores extrapolam o intervalo de menos um a mais um, a soma acumulada deve ser dividida pela sua amplitude máxima de pico absoluto.

Um elegante teste conceitual é a síntese por Mínimo Múltiplo Comum. Ao concatenar quatro repetições de um ruído de cem amostras com cinco repetições de um ruído de oitenta amostras, cria-se um único vetor contíguo de quatrocentas amostras, correspondente ao Mínimo Múltiplo Comum entre cem e oitenta. Quando executado no algoritmo básico de repetição, este vetor emite simultaneamente duas frequências em proporção de cinco para quatro, reproduzindo com pureza analítica o intervalo harmônico da Terça Maior Pura.

#### Roteiro Prático e Instruções para o Jupyter Notebook no Laboratório 4

No repositório do curso, os códigos e experimentos de geração de tom digital e síntese física encontram-se na pasta assets barra labs barra le zero quatro sublinhado karplus hífen strong, nos arquivos le zero quatro sublinhado zero um sublinhado signal hífen reconstruction ponto ipynb e le zero quatro sublinhado karplus hífen strong ponto ipynb, complementados pelo guia técnico LE zero quatro sublinhado EXPLICACAO ponto md, na pasta assets barra labs.

Preparação do ambiente. Os dois notebooks acrescentam a pasta dois níveis acima ao caminho de busca do Python, com sys ponto path ponto append de ponto ponto barra ponto ponto barra, para importar as bibliotecas do curso, lib ponto myAudioProcessingLib e lib ponto mySignalProcessingLib, que ficam em assets barra lib. Por isso, o Jupyter deve ser aberto com o diretório de trabalho na própria pasta do notebook. As funções play e SIGNALgenerate vêm dessas bibliotecas. Os arquivos de áudio de apoio ficam em assets barra sounds.

Primeiro notebook, signal hífen reconstruction.

Primeira etapa: gerador básico de tom senoidal. A função create sublinhado sine sublinhado signal recebe a frequência f, a duração dur em segundos e a taxa de amostragem f s, com valores padrão de quatrocentos e quarenta Hertz, um segundo e quarenta e oito mil Hertz. Calcula-se o número de amostras N como o inteiro de dur vezes f s, o período discreto P como f s dividido por f, e a senoide x como seno de dois pi dividido por P vezes n. Com f igual a duzentos e vinte Hertz e duração de um vírgula cinco segundo, a saída mostra P igual a duzentos e dezoito vírgula dezoito amostras e N igual a setenta e dois mil amostras. Reproduzido com o dobro da taxa de amostragem, o mesmo vetor soa uma oitava acima e dura metade do tempo. Em seguida, repete-se o experimento com quarenta e quatro vírgula um quilohertz e confirma-se que a duração continua um vírgula cinco segundo, embora P caia para duzentos vírgula quarenta e cinco e N para sessenta e seis mil, cento e cinquenta.

Segunda etapa: validação pela Transformada de Fourier. Define-se a função SIGNALtone, que fixa f s em quarenta e quatro vírgula um quilohertz. Para um tom de trezentos e trinta Hertz e três segundos, aplica-se n p ponto fft ponto fft ao sinal e toma-se o módulo com n p ponto abs. O eixo de frequências em Hertz é o vetor de índices dividido pelo comprimento do espectro e multiplicado por f s. Recorta-se a primeira metade do espectro, porque o sinal é real e o espectro é simétrico, e limita-se o eixo horizontal de zero a mil e cem Hertz, o que revela um único pico na frequência programada.

Terceira etapa: sinal multifrequencial. Somam-se quatro senoides de duzentos, quatrocentos, seiscentos e oitocentos Hertz, a quarenta e quatro vírgula um quilohertz, por um segundo, cada uma com fase inicial de menos pi sobre dois radianos, geradas por SIGNALgenerate no modo osc. A segunda amostra do sinal vale cerca de menos três vírgula nove oito. No domínio espectral, aparecem quatro picos limpos, cada um com amplitude N sobre dois, isto é, vinte e dois mil e cinquenta. O coeficiente DC vale algo da ordem de dez elevado a menos onze, ou seja, zero para fins práticos.

Quarta etapa: timbre por forma de onda repetida. A função SIGNALwaveform calcula o período P como o inteiro arredondado de f s sobre f, gera um bloco de P amostras de ruído aleatório com SIGNALgenerate no modo random, que usa ruído gaussiano, e repete esse bloco por concatenação até completar N amostras, cortando o excesso. Com f igual a cento e dez Hertz e um segundo, o espectro, limitado a zero a quatrocentos e quarenta Hertz, mostra picos na fundamental de cento e dez Hertz e em todos os seus harmônicos inteiros, cada um com amplitude aleatória. Isso é o timbre.

Segundo notebook, karplus hífen strong. Aqui a taxa de amostragem é de dezesseis mil Hertz, e o buffer inicial é passado de fora para a função, como vetor x.

Quinta etapa: a família de funções, em ordem de evolução. KS sublinhado um recebe o buffer x e o tamanho N e apenas repete o buffer até completar N amostras. Com cinquenta amostras de ruído gaussiano obtém-se um tom de trezentos e vinte Hertz, e com cem amostras, uma oitava abaixo. Trocar o ruído gaussiano por ruído uniforme entre menos um e mais um não muda a altura, que depende só do tamanho do buffer, mas altera o ataque percebido. KS sublinhado dois escreve a mesma repetição como recorrência, y de n igual a x de n, enquanto n é menor que M, mais y de n menos M. KS sublinhado três acrescenta o fator de decaimento alfa, com valor padrão zero vírgula noventa e nove, multiplicando o termo atrasado. KS sublinhado media, a versão original de mil novecentos e oitenta e três, copia o buffer para uma lista y e, para i de M até N menos um, acrescenta alfa vezes zero vírgula cinco vezes a soma de y de i menos M com y de i menos M menos um. A função KS, final, calcula um alfa compensado, igual a alfa elevado à razão entre M e o tamanho de referência do buffer, que vale cinquenta por padrão.

Atenção a um detalhe: no notebook, o atraso do buffer é simplesmente M igual ao comprimento de x, ou, no acorde, ao inteiro arredondado de f s sobre a frequência. A correção de menos zero vírgula cinco amostra, descrita na teoria acima, não é aplicada no código. O erro de afinação resultante é medido em cents na tabela da sétima etapa.

Sexta etapa: comparação de amortecimento. Usando KS sublinhado três com alfa fixo em zero vírgula noventa e nove, um buffer de M igual a cinquenta, que dá trezentos e vinte Hertz, e um de M igual a vinte e cinco, que dá seiscentos e quarenta Hertz. Depois de um segundo, a amplitude restante é zero vírgula noventa e nove elevado a trezentos e vinte, cerca de quatro vírgula zero por cento, para a nota grave, e zero vírgula noventa e nove elevado a seiscentos e quarenta, cerca de zero vírgula dezesseis por cento, para a aguda. Note que o notebook imprime amplitude, e não energia. A nota aguda morre bem mais rápido porque o fator alfa age uma vez por período, e ela tem o dobro de períodos por segundo.

Sétima etapa: acordes. A função nota2freq converte uma cifra como A quatro ou C sustenido cinco em Hertz, tomando Lá quatro como quatrocentos e quarenta Hertz. A função ks sublinhado acorde recebe um dicionário que associa cada nota a um ganho, a duração e o alfa padrão, e aceita um dicionário opcional, sustentar, com alfas próprios. Para cada nota ela calcula M como o inteiro arredondado de f s sobre a frequência, gera um buffer gaussiano de M amostras, sintetiza com a função KS, soma com o ganho e, no fim, normaliza dividindo pelo pico e multiplicando por zero vírgula nove.

O primeiro acorde é o de abertura de A Hard Day's Night, com as notas Ré dois, com ganho um vírgula cinco e alfa zero vírgula novecentos e noventa e oito, Ré três, Fá três, Sol três, Fá quatro, Lá quatro, Dó cinco e Sol cinco, com ganho zero vírgula seis. A tabela de erros de afinação impressa pelo notebook, a dezesseis mil Hertz, mostra desvios de menos zero vírgula cinco cents em Ré dois e Ré três, cerca de menos sete cents em Fá três, Sol três e Fá quatro, mais dezessete vírgula quatro cents em Lá quatro, menos vinte e três vírgula sete cents em Dó cinco e mais trinta e cinco cents em Sol cinco. Esse erro cresce com a frequência, porque o buffer tem poucas amostras e o arredondamento pesa mais. É exatamente o problema que o filtro de atraso fracionário resolve.

O segundo é o acorde de Hendrix, com cinco notas, Mi dois, Mi três, Sol sustenido três, Ré quatro e Sol quatro, todas com ganho um, por três segundos e alfa zero vírgula noventa e oito. O terceiro é o Acorde Místico de Scriabin, com Dó três, Fá sustenido três, Si bemol três, Mi quatro, Lá quatro e Ré cinco, por quatro segundos e alfa zero vírgula novecentos e noventa e cinco. Os arquivos de áudio e MIDI de referência não estão no repositório, exceto a gravação do acorde de A Hard Day's Night, na pasta sounds, para comparação auditiva.

Oitava etapa: teste do mínimo múltiplo comum. Soma-se um bloco de cem amostras aleatórias repetido quatro vezes com um bloco de oitenta amostras repetido cinco vezes, obtendo um vetor de quatrocentas amostras. Reproduzido com KS sublinhado um a dezesseis mil Hertz, ele soa duas notas simultâneas, de cento e sessenta e duzentos Hertz, na razão de cinco para quatro, uma terça maior. O espectro confirma que todos os picos são múltiplos de cento e sessenta ou de duzentos Hertz.

---

## CAPÍTULO V — NÚMEROS COMPLEXOS, FASORES E EXPONENCIAIS COMPLEXAS

### 1. O Espaço dos Números Complexos e a Fórmula de Euler

A análise harmônica em processamento de sinais rompe as limitações das oscilações puramente reais ao projetá-las sobre o plano complexo de Argand-Gauss. 

Na representação cartesiana, um número complexo z é a soma de uma componente real a com uma componente imaginária b multiplicada pela unidade imaginária j, a qual satisfaz a propriedade axiomática: j elevado ao quadrado é igual a menos um.

A representação polar alternativa expressa o número complexo através de sua magnitude r, ou módulo, e de seu ângulo de fase teta, através da célebre Fórmula de Euler:

A exponencial de j vezes teta é igual ao cosseno de teta mais j vezes o seno de teta.

Deste teorema extrai-se a noção de fasor: um vetor de magnitude constante que gira no plano complexo com velocidade angular constante. Multiplicar dois números complexos na forma polar possui uma intuição geométrica direta: multiplica-se os seus respectivos módulos e somam-se os seus respectivos ângulos de fase. 

Da mesma forma, as raízes enésimas de um número complexo pela fórmula de De Moivre distribuem-se como vértices perfeitamente simétricos de polígonos regulares inscritos no círculo trigonométrico, atestando a harmonia da representação polar.

---

### 2. Módulo, Fase e a Falha Crítica do Arco Tangente Simples

Enquanto o módulo r de um número complexo a mais j b é calculado de forma inequívoca pelo teorema de Pitágoras — sendo a raiz quadrada da soma de a ao quadrado com b ao quadrado —, a determinação da fase angular encerra uma armadilha matemática clássica.

O uso ingênuo da função arco tangente da razão b dividido por a perde irremediavelmente a informação dos sinais algébricos individuais das variáveis a e b.

Considere a análise sistemática dos quatro quadrantes do plano cartesiano:

No primeiro quadrante, onde a é positivo e b é positivo — como no ponto um mais j —, a divisão de b por a resulta no valor positivo mais um. O arco tangente simples retorna mais pi sobre quatro radianos, ou quarenta e cinco graus, o que é geometricamente correto.

No segundo quadrante, onde a é negativo e b é positivo — como no ponto menos um mais j —, a divisão de b por a resulta no valor negativo menos um. O arco tangente simples retorna menos pi sobre quatro radianos, projetando o ângulo erroneamente no quarto quadrante. Para corrigir este erro grave, o algoritmo deve somar pi radianos ao resultado.

No terceiro quadrante, onde a é negativo e b é negativo — como no ponto menos um menos j —, a divisão de b por a resulta no valor positivo mais um, pois negativo dividido por negativo é positivo. O arco tangente simples retorna mais pi sobre quatro radianos, projetando o vetor erroneamente no primeiro quadrante. Para corrigir este erro, o algoritmo deve subtrair pi radianos do resultado.

No quarto quadrante, onde a é positivo e b é negativo — como no ponto um menos j —, a divisão de b por a resulta no valor negativo menos um. O arco tangente simples retorna menos pi sobre quatro radianos, o que é geometricamente correto.

Para solucionar essa ambiguidade e cobrir todo o espectro contínuo de menos pi até mais pi radianos, linguagens de programação e processadores de sinal utilizam universalmente a função arco tangente dois, que recebe separadamente as coordenadas b e a, inspecionando os seus sinais individuais antes de calcular o ângulo verdadeiro.

---

### 3. Desafio de Algoritmos de Ultraprecisão sem Funções Prontas

Em sistemas embarcados de controle e processadores dedicados de sinal onde não há bibliotecas matemáticas prontas ou coprocessadores aritméticos, funções transcendentais como o arco tangente devem ser calculadas diretamente a partir de séries de potências fundamentais.

A expansão em série de Maclaurin-Taylor para a função arco tangente de uma variável real u é deduzida integrando termo a termo a série geométrica da derivada de arco tangente de u, que é um dividido por um mais u ao quadrado:

O arco tangente de u é igual à somatória infinita, com o índice n variando de zero a infinito, de menos um elevado a n, multiplicado por u elevado à potência dois n mais um, tudo dividido por dois n mais um.

Expandindo os primeiros termos: arco tangente de u é igual a u menos u ao cubo sobre três, mais u à quinta sobre cinco, menos u à sétima sobre sete, mais u à nona sobre nove, e assim sucessivamente com sinais estritamente alternados.

Contudo, se a variável u possuir módulo próximo da unidade, essa série original converge com lentidão exasperante, exigindo milhares de iterações para fornecer poucos dígitos significativos. Para acelerar o cálculo até atingir a precisão máxima de ponto flutuante de sessenta e quatro bits em apenas meia dúzia de passos, aplicam-se duas transformações analíticas exatas:

Primeira transformação: caso o módulo do argumento u seja estritamente superior a um, inverte-se o argumento utilizando a identidade trigonométrica de reflexão ortogonal: o arco tangente de u é igual ao sinal algébrico de u multiplicado por pi sobre dois, menos o arco tangente do inverso um sobre u. Desta forma, o novo argumento a ser avaliado terá módulo obrigatoriamente menor ou igual a um.

Segunda transformação: aplica-se a identidade de redução de meio ângulo. A partir da relação de arco metade para a tangente — onde a tangente do ângulo dividido por dois é igual ao seno do ângulo dividido por um mais o cosseno —, prova-se analiticamente que:

O arco tangente de u é identicamente igual a duas vezes o arco tangente de uma nova variável comprimida, dada por: u dividido pela soma de um com a raiz quadrada de um mais u ao quadrado.

Ao aplicar essa fórmula de redução de meio ângulo três vezes consecutivas sobre o argumento inicial com módulo menor ou igual a um, o valor de u é comprimido drasticamente para uma vizinhança microscópica próxima da origem: para u igual a um, a primeira redução resulta em aproximadamente zero vírgula quarenta e um quatro; a segunda redução desaba para zero vírgula dezenove oito; e a terceira redução atinge diminutos zero vírgula zero nove oito radianos.

Ao calcular a série de Taylor sobre este valor tão pequeno, os termos de potências superiores decaem exponencialmente a taxas superiores a dez elevado a menos dois por termo. Assim, apenas oito termos da somatória bastam para que a precisão residual atinja o limiar de ponto flutuante do processador — dez elevado a menos dezesseis. Ao término da soma, multiplica-se o resultado final por dois elevado ao cubo — isto é, oito —, desfazendo as três reduções de meio ângulo e recuperando o valor exato do arco tangente com perfeição analítica absoluta.

#### Dedução Analítica da Fórmula de John Machin para a Constante Pi

Para que o algoritmo seja integralmente independente e não dependa de qualquer constante embutida na linguagem, a constante pi deve ser calculada a partir da própria série hiper-acelerada do arco tangente. Utiliza-se a célebre formulação descoberta pelo astrônomo britânico John Machin em mil setecentos e seis.

A dedução analítica é obtida definindo um ângulo auxiliar alfa cujo arco tangente é a fração exata um quinto: tangente de alfa é igual a um quinto.

Aplicando a identidade da tangente do arco duplo: a tangente de duas vezes alfa é igual a duas vezes a tangente de alfa, dividido por um menos o quadrado da tangente de alfa. Substituindo a fração um quinto: duas vezes um quinto resulta em dois quintos no numerador; um menos um sobre vinte e cinco resulta em vinte e quatro vinte e cinco avos no denominador. Dividindo as frações, obtemos dez vinte e quatro avos, que simplifica para cinco doze avos: a tangente de duas vezes alfa é igual a cinco doze avos.

Aplicando novamente a duplicação para quatro vezes alfa: duas vezes cinco doze avos resulta em cinco sextos no numerador; um menos o quadrado de cinco doze avos — vinte e cinco sobre cento e quarenta e quatro — resulta em cento e dezenove sobre cento e quarenta e quatro. Dividindo as frações, obtemos cento e vinte sobre cento e dezenove: a tangente de quatro vezes alfa é igual a cento e vinte dividido por cento e dezenove.

Note que cento e vinte sobre cento e dezenove é um número assombrosamente próximo de um, o que significa que o ângulo quatro vezes alfa está a uma distância microscópica de pi sobre quatro radianos — quarenta e cinco graus.

Calculando a tangente da diferença entre quatro vezes alfa e pi sobre quatro: a tangente da diferença entre dois ângulos é a tangente do primeiro menos a tangente do segundo, tudo dividido por um mais o produto das tangentes. Sabendo que a tangente de pi sobre quatro é igual a um, temos: no numerador, cento e vinte sobre cento e dezenove menos um, resultando em um sobre cento e dezenove; no denominador, um mais cento e vinte sobre cento e dezenove, resultando em duzentos e trinta e nove sobre cento e dezenove.

Dividindo as frações, o denominador comum cento e dezenove cancela-se, revelando a relação de extrema simplicidade aritmética:

A tangente da diferença entre quatro vezes alfa e pi sobre quatro é igual a exatamente um dividido por duzentos e trinta e nove.

Tomando a função arco tangente em ambos os lados da igualdade e isolando a constante pi sobre quatro:

Pi sobre quatro é igual a quatro vezes alfa menos o arco tangente de um sobre duzentos e trinta e nove.

Substituindo o ângulo alfa pelo seu valor original arco tangente de um quinto, e multiplicando todos os termos por quatro, consolida-se a imortal Fórmula de Machin:

A constante pi é igual a dezesseis vezes o arco tangente da fração um quinto, menos quatro vezes o arco tangente da fração um sobre duzentos e trinta e nove.

Como as frações um quinto — zero vírgula dois — e um sobre duzentos e trinta e nove — aproximadamente zero vírgula zero zero quatro um oito — são frações diminutas, a série de potências converge com velocidade supersônica, permitindo sintetizar o valor exato de pi com dezenas de casas decimais em frações de milissegundo sem recorrer a qualquer recurso externo.

---

### 4. O Enigma Matemático da Unidade Imaginária Elevada a Si Mesma

Uma indagação matemática profunda e contra-intuitiva é: o que acontece quando a unidade imaginária j é elevada à sua própria potência imaginária j?

Para resolver esta questão de forma rigorosa, expressamos a operação utilizando a definição formal do logaritmo complexo. Para qualquer número complexo z não nulo, a exponencial de base z elevada a um expoente w é definida analiticamente como a exponencial natural do produto de w pelo logaritmo neperiano de z: z elevado a w é igual à exponencial natural de w multiplicado pelo logaritmo complexo de z.

O logaritmo complexo de z decompõe-se na soma do logaritmo natural do módulo de z com j vezes o argumento angular de z, admitindo infinitos ramos discretos indexados pelo número inteiro k de voltas completas:

O logaritmo complexo de z é igual ao logaritmo natural do módulo de z, mais j vezes abre parênteses o argumento principal teta mais dois pi vezes k fecha parênteses, onde k pertence ao conjunto dos números inteiros.

Avaliando para a unidade imaginária pura j: a magnitude de j é igual a um. Como o logaritmo natural de um é igual a zero, a parte real do logaritmo anula-se completamente. O argumento angular de j sobre o eixo imaginário positivo é pi sobre dois radianos. Portanto, o logaritmo complexo de j resulta em:

O logaritmo de j é igual a j multiplicado por abre parênteses pi sobre dois mais dois pi vezes k fecha parênteses.

Elevando j à potência w igual a j, multiplicamos o expoente j pelo logaritmo de j:

O produto de j pelo logaritmo de j torna-se: j multiplicado por j, que por sua vez multiplica abre parênteses pi sobre dois mais dois pi vezes k fecha parênteses.

Pela propriedade axiomática de que a unidade imaginária multiplicada por si mesma resulta no número real menos um, o produto j vezes j torna-se estritamente menos um. Aplicando este resultado na função exponencial, encontramos a expressão canônica final:

j elevado a j é igual à exponencial natural de menos a quantidade pi sobre dois mais dois pi vezes k.

Avaliando o ramo principal correspondente a k igual a zero, a expressão simplifica-se para:

j elevado a j no ramo principal é igual à exponencial de menos pi sobre dois, cujo valor numérico calculado com altíssima precisão é aproximadamente zero vírgula vinte zero sete oito sete nove cinco sete seis três cinco.

Avaliando outros ramos inteiros: para k igual a um, temos a exponencial de menos cinco pi sobre dois, resultando em aproximadamente zero vírgula zero zero zero three oito oito; para k igual a menos um, temos a exponencial de mais três pi sobre dois, resultando em aproximadamente cento e onze vírgula trinta e um.

Todas as infinitas soluções para k pertencente aos inteiros compartilham uma constatação assombrosa: não existe qualquer parte imaginária. A unidade imaginária pura elevada a si mesma elimina incondicionalmente todas as suas componentes imaginárias e ancora-se com rigor absoluto no conjunto dos números reais estritamente positivos.

---

### 5. Periodicidade em Tempo Discreto e a Condição de Racionalidade

No mundo contínuo da física clássica, uma função senoidal pura x de t igual ao seno de ômega zero vezes t é perpétua e incondicionalmente periódica para qualquer valor real de frequência ômega zero, com período temporal contínuo igual a dois pi dividido por ômega zero.

No entanto, no universo discreto e indexado do computador, a função x de n igual ao seno de ômega zero vezes n entre colchetes só será periódica se, e somente se, ela reencontrar exatamente os mesmos valores numéricos após um número inteiro N de amostras. Isso exige que o argumento ômega zero vezes a soma n mais N seja igual a ômega zero vezes n mais dois pi vezes um número inteiro k de voltas completas: ômega zero vezes N deve ser igual a dois pi vezes k.

Isolando a razão de frequências, estabelece-se a estrita condição de racionalidade:

A razão entre a frequência angular digital ômega zero e dois pi deve ser estritamente um número racional pertencente ao conjunto Q, ou seja, deve poder ser expressa como a divisão entre dois números inteiros k e N.

O período fundamental da sequência discreta, representado pela letra maiúscula N, é o menor inteiro positivo obtido após simplificar a fração k sobre N até que o numerador e o denominador sejam números inteiros primos entre si.

Considere dois exemplos ilustrativos:

No primeiro exemplo, temos uma senoide discreta com ômega zero igual a zero vírgula dois pi radianos por amostra. Dividindo zero vírgula dois pi por dois pi, obtemos a fração dois décimos, a qual simplifica para a fração racional um quinto. Como um quinto é uma fração de inteiros, a senoide é estritamente periódica no computador, repetindo seu padrão idêntico a cada cinco amostras exatas.

No segundo exemplo, temos uma senoide discreta definida ingenuamente como o seno de um vezes n radianos por amostra. Dividindo a frequência angular unitária por dois pi, obtemos a razão um sobre dois pi. Como a constante pi é um número transcendente e irracional, o denominador dois pi jamais poderá ser simplificado como uma razão de inteiros. Portanto, a sequência numérica no computador jamais repetirá exatamente os mesmos valores em nenhuma amostra futura, sendo rigorosa e perpetuamente aperiódica.

#### Roteiro Prático e Instruções para o Jupyter Notebook no Laboratório 5

No repositório do curso, este laboratório está na pasta assets barra labs barra le zero cinco sublinhado complex hífen exponentials, com o notebook le zero cinco sublinhado complex hífen numbers ponto ipynb e os scripts le zero cinco sublinhado desafio um sublinhado modulo sublinhado e sublinhado fase ponto p y e le zero cinco sublinhado desafio dois sublinhado j sublinhado elevado sublinhado a sublinhado j ponto p y. O texto de apoio é LE zero cinco sublinhado EXPLICACAO ponto md, em assets barra labs.

Os scripts rodam no terminal, na pasta do laboratório. O desafio dois importa o desafio um, então os dois precisam estar na mesma pasta.

Primeira etapa: números complexos no Python. Criam-se a igual a três, b igual a quatro, e z um igual a a mais b vezes um j. O tipo de z um é complex. O módulo, por n p ponto abs, vale cinco, e a fase, por n p ponto angle, vale zero vírgula nove dois sete três radianos.

Segunda etapa: módulo e fase em funções. COMPLEXmagnitude tem a versão um, com a raiz da soma dos quadrados, e a versão dois, com n p ponto abs. COMPLEXphase tem três versões: arctan da razão imaginário sobre real, que só enxerga o primeiro e o quarto quadrantes, arctan dois e angle. Para os quatro números de módulo cinco, o notebook imprime: três mais quatro j, arctan igual a cinquenta e três vírgula treze graus; menos três mais quatro j, arctan igual a menos cinquenta e três vírgula treze, contra cento e vinte e seis vírgula oitenta e sete de arctan dois e angle; menos três menos quatro j, arctan igual a mais cinquenta e três vírgula treze, contra menos cento e vinte e seis vírgula oitenta e sete; e três menos quatro j, menos cinquenta e três vírgula treze nas três versões.

Terceira etapa: Desafio um, módulo e fase sem funções prontas. No notebook, os nomes são mySeriesArctan, myArctan, myArctan dois, myMagnitude, myPhase e myRoots, com a constante MY sublinhado PI. No script, os nomes equivalentes são serie sublinhado arctan, meu sublinhado arctan, meu sublinhado arctan dois e a constante PI.
A série de Taylor do arco tangente soma os termos u, menos u ao cubo sobre três, mais u à quinta sobre cinco, e assim por diante, com sinais alternados. Ela não usa um número fixo de termos: o laço continua enquanto o termo for maior que a tolerância de dez elevado a menos dezessete. A constante pi vem da fórmula de Machin, dezesseis arctan de um quinto menos quatro arctan de um sobre duzentos e trinta e nove, que no notebook dá três vírgula um quatro um cinco nove dois seis cinco três cinco oito nove sete nove quatro, contra três vírgula um quatro um cinco nove dois seis cinco três cinco oito nove sete nove três do NumPy. A função myArctan, para u maior que um em módulo, usa a inversão pi sobre dois menos arctan de um sobre u. Depois reduz o argumento três vezes pela fórmula do meio ângulo, u sobre um mais a raiz de um mais u ao quadrado, e multiplica a série por oito, que é dois ao cubo. A função myArctan dois decide o quadrante pelos sinais: soma pi no segundo quadrante, subtrai pi no terceiro, e trata os semieixos imaginários à parte.
Conferência: para três mais quatro j, menos três mais quatro j, menos três menos quatro j, três menos quatro j, j, menos j, menos um e zero, a fase própria coincide com a do NumPy. Com cem mil números complexos aleatórios, de escalas entre dez elevado a menos seis e dez elevado a seis, o notebook imprime erro relativo máximo do módulo de três vírgula oito vezes dez elevado a menos dezesseis, e erro absoluto máximo da fase de um vírgula três vezes dez elevado a menos quinze radianos.

Quarta etapa: potência e raiz. Para z dois igual a z um ao quadrado, o módulo vale vinte e cinco e a fase vale cento e seis vírgula vinte e seis graus, o dobro da fase de z um. Para z três igual a z um elevado a meio, o módulo vale raiz de cinco, cerca de dois vírgula dois quatro, e a fase vale vinte e seis vírgula cinquenta e seis graus, a metade. A função myRoots calcula as n raízes pela fórmula de De Moivre, e o notebook plota as raízes de ordens dois, três e seis de três mais quatro j: um segmento, um triângulo e um hexágono, inscritos num círculo de raio cinco elevado a um sobre n. As raízes quadradas são dois mais j e menos dois menos j.

Quinta etapa: Desafio dois, j elevado a j. Primeiro, antecipa-se o valor: j elevado a j é e elevado a menos a fase de j, ou e elevado a menos pi sobre dois, igual a zero vírgula dois zero sete oito sete nove cinco sete seis três cinco. O Python, ao calcular um j elevado a um j, devolve esse valor, com parte imaginária zero. No notebook, o valor impresso é zero vírgula vinte, zero sete oito sete nove cinco sete seis três cinco zero sete seis um nove três. O ponto cai sobre o eixo real. Como a fase de j é pi sobre dois mais dois pi k, há infinitos valores, e elevado a menos pi sobre dois mais dois pi k, todos reais e positivos. Para k de menos dois até dois, o notebook imprime cerca de cinquenta e nove mil novecentos e sessenta e um, cento e onze vírgula três, zero vírgula dois zero oito, três vírgula oito oito vezes dez elevado a menos quatro e sete vírgula dois cinco vezes dez elevado a menos sete. Eles são plotados sobre o eixo real, em escala logarítmica, e não numa espiral. O script também calcula o exponencial pela própria série de Taylor, com redução do argumento por divisões por dois.

Sexta etapa: periodicidade em tempo discreto. Geram-se cem amostras de cosseno com ômega igual a dois pi vezes um décimo, e outras de cosseno com ômega igual a um radiano por amostra. Procura-se o menor deslocamento P, de um a quarenta e nove, para o qual x de n mais P coincide com x de n, com n p ponto allclose. O primeiro sinal tem período fundamental dez. O segundo não tem nenhum período menor que cinquenta, porque dois pi dividido por um é irracional.

---

## CAPÍTULO VI — A TRANSFORMADA DISCRETA DE FOURIER E PROCESSAMENTO ESPECTRAL

### 1. Definição Canônica da Transformada Discreta de Fourier e Geometria Linear

A Transformada Discreta de Fourier, universalmente conhecida pela sigla DFT (do inglês Discrete Fourier Transform), ergue-se como o instrumento central para a análise e o processamento de sinais discretos no domínio da frequência.

A Equação de Análise decompõe um vetor temporal de N amostras, representado por x de n entre colchetes, em N coeficientes espectrais complexos, representados por X de k entre colchetes:

X de k é igual à somatória, com o índice temporal n variando de zero até N menos um, da amostra temporal x de n multiplicada pela exponencial complexa de menos j vezes dois pi vezes k vezes n dividido por N, onde o índice de frequência discreta k varia de zero até N menos um.

Em termos físicos e geométricos, o coeficiente espectral X de k é a soma de cada amostra temporal x de n multiplicada pelo fasor complexo unitário que gira no sentido horário com velocidade angular discreta de dois pi vezes k vezes n sobre N. O índice de frequência discreta k varia de zero até N menos um.

A Equação de Síntese Inversa, ou Transformada Discreta de Fourier Inversa (IDFT), reconstrói o sinal temporal original a partir de seus coeficientes espectrais ponderados:

A amostra temporal x de n é igual a um dividido por N, multiplicado pela somatória, com o índice de frequência k variando de zero até N menos um, do coeficiente espectral X de k multiplicado pela exponencial complexa de mais j vezes dois pi vezes k vezes n dividido por N, onde o índice temporal n varia de zero até N menos um.

Sob a ótica da álgebra e geometria linear, a Transformada Discreta de Fourier atua como um banco de correlatores de fase. Cada coeficiente X de k calcula a projeção ortogonal do vetor de sinal x sobre a k-ésima função de base exponencial complexa. O módulo de X de k quantifica a intensidade ou energia presente naquela frequência discreta, enquanto o argumento angular ou fase de X de k estabelece o alinhamento temporal e a defasagem da oscilação.

Dedução analítica formal da Ortogonalidade da Base de Fourier:

Definimos as funções de base discretas como vetores no espaço complexo de dimensão N, onde o k-ésimo vetor de base possui elementos e de k de n iguais à exponencial complexa de mais j vezes dois pi vezes k vezes n sobre N. O produto interno complexo canônico entre dois vetores de base com índices de frequência distintos, k e l, sobre o intervalo discreto de zero a N menos um, é expresso por:

O produto interno entre e de k e e de l é igual à somatória de n de zero a N menos um do elemento e de k de n multiplicado pelo conjugado complexo do elemento e de l de n. Como a conjugação inverte o sinal do expoente, isso resulta na somatória de n de zero a N menos um da exponencial de mais j vezes dois pi vezes abre parênteses k menos l fecha parênteses vezes n sobre N. Podemos reescrever cada termo como a enésima potência da razão comum r.

Esta expressão constitui uma progressão geométrica finita de N termos com primeiro termo igual a um e razão comum r dada pela exponencial de j vezes dois pi vezes a diferença k menos l dividido por N.

Pela fórmula da soma de uma progressão geométrica finita, a soma de r elevado a n com n de zero a N menos um é expressa pela razão: a fração cujo numerador é um menos r elevado a N, e cujo denominador é um menos r.

Avaliamos dois casos mutuamente exclusivos:

Caso um: quando os índices k e l são distintos, ou seja, k diferente de l. Sendo k e l inteiros no intervalo de zero a N menos um, a diferença k menos l é um número inteiro não nulo m diferente de zero. Ao elevar a razão r à potência N, os fatores N no numerador e denominador simplificam-se, resultando na exponencial de j vezes dois pi vezes o inteiro m. Pela fórmula de Euler, o cosseno de dois pi vezes m é igual a um e o seno é igual a zero, de modo que r elevado a N vale exatamente um mais zero j, ou seja, um.

Como r elevado a N é rigorosamente igual a um e a razão r é diferente de um, o numerador da soma da progressão torna-se um menos um, que é igual a zero. Conclui-se analiticamente que, para quaisquer frequências distintas k diferente de l, o produto interno entre e de k e e de l anula-se de forma estrita.

Caso dois: quando os índices k e l são rigorosamente idênticos, ou seja, k igual a l. A diferença k menos l é igual a zero, fazendo com que a razão r seja igual à exponencial de zero, que vale um. A soma de r elevado a n reduz-se à soma de N parcelas iguais a um, totalizando exatamente N.

Agrupando ambos os resultados por meio do símbolo delta de Kronecker, estabelece-se a célebre Relação de Ortogonalidade Discreta: o produto interno entre e de k e e de l é igual a N multiplicado pelo delta de Kronecker de k e l, onde o delta vale um se k for igual a l, e vale zero se k for diferente de l.

Esta dedução analítica evidencia por que a Equação de Síntese Inversa exige a presença do fator multiplicativo um sobre N: como a norma ao quadrado de cada vetor de base vale N, a base é puramente ortogonal, porém não ortonormalizada. A divisão por N na síntese neutraliza a amplificação por N resultante da projeção de cada modo próprio sobre si mesmo.

Destaca-se o coeficiente espectral para k igual a zero, denominado Componente de Corrente Contínua ou Componente DC (do inglês Direct Current):

Como a exponencial de menos j vezes zero é igual a um para qualquer instante temporal n, a equação de análise simplifica-se diretamente para a soma algébrica direta de todas as amostras temporais do sinal: X de zero é igual à somatória de x de n com n variando de zero até N menos um.

Dividindo este coeficiente pelo número total de amostras N, obtém-se o valor médio aritmético exato do sinal: a média x barra é igual a um sobre N multiplicado por X de zero, o que equivale a um sobre N vezes a somatória de x de n de zero a N menos um.

Assim, o coeficiente X de zero quantifica o deslocamento médio ou nível de corrente contínua contido na forma de onda temporal.

---

### 2. Propriedades Estruturais, Teoremas de Conservação e Simetrias

Quatro propriedades matemáticas fundamentais regem o comportamento da Transformada Discreta de Fourier:

Primeira propriedade: o Teorema de Conservação de Energia de Parseval.
A energia total calculada no domínio do tempo é matematicamente idêntica à energia total distribuída no espectro de frequência, modulada pelo fator de escala um sobre N: a somatória de n de zero a N menos um do quadrado do módulo de x de n é igual a um sobre N multiplicado pela somatória de k de zero a N menos um do quadrado do módulo de X de k.

Dedução formal do Teorema de Parseval:

Iniciamos expandindo a somatória da energia espectral, lembrando que o quadrado do módulo de um número complexo X de k é o produto de X de k pelo seu conjugado complexo X asterisco de k: a somatória de k de zero a N menos um do quadrado do módulo de X de k é igual à somatória de k de zero a N menos um de X de k multiplicado por X conjugado de k.

Substituímos X de k e X asterisco de k pelas suas respectivas equações de análise no domínio do tempo, empregando variáveis mudas independentes n e m para as somatórias temporais:

X de k é a somatória de n de zero a N menos um de x de n vezes a exponencial de menos j dois pi k n sobre N.

X asterisco de k é o conjugado da somatória de m de zero a N menos um de x de m vezes a exponencial de menos j dois pi k m sobre N, o que resulta na somatória de m de zero a N menos um de x conjugado de m vezes a exponencial de mais j dois pi k m sobre N.

Substituindo ambas as expressões na equação da energia espectral, obtemos a somatória sobre k do produto entre a somatória sobre n de x de n vezes a exponencial de menos j dois pi k n sobre N e a somatória sobre m de x conjugado de m vezes a exponencial de mais j dois pi k m sobre N.

Como todas as somatórias são finitas, invertemos a ordem dos somatórios, agrupando os termos temporais e isolando a soma sobre o índice de frequência k: a somatória sobre n de x de n multiplicada pela somatória sobre m de x conjugado de m, multiplicada pela somatória interna sobre k de zero a N menos um da exponencial de menos j dois pi k vezes abre parênteses n menos m fecha parênteses sobre N.

Reconhecemos na somatória interna a relação de ortogonalidade da base discreta deduzida anteriormente. A soma sobre k de zero a N menos um da exponencial de menos j dois pi k vezes abre parênteses n menos m fecha parênteses sobre N é rigorosamente igual a N multiplicado pelo delta de Kronecker de n e m.

Substituindo este delta de Kronecker na equação, o termo colapsa: o delta de n e m anula todos os termos onde m é diferente de n, sobrevivendo unicamente a parcela onde m é igual a n. Portanto, a somatória sobre m reduz-se ao único termo x conjugado de n, resultando em: N multiplicado pela somatória de n de zero a N menos um de x de n vezes x conjugado de n, o que equivale a N vezes a somatória do quadrado do módulo de x de n.

Dividindo ambos os membros da igualdade pela constante N, estabelece-se com rigor incondicional o Teorema de Parseval: a somatória do quadrado dos módulos de x de n no tempo é igual a um sobre N vezes a somatória do quadrado dos módulos de X de k na frequência.

Esta identidade prova que a Transformada Discreta de Fourier realiza uma rotação unitária de eixos no espaço vetorial complexo, conservando integralmente a energia física da oscilação sem perda nem geração espúria de potência.

Segunda propriedade: a Simetria Conjugada Hermitiana para Sinais Reais.
Na vasta maioria das aplicações de engenharia, os sinais capturados — tais como áudio acústico, tensões de sensores e ondas eletromecânicas — possuem amostras puramente reais, pertencendo ao conjunto dos números reais, x de n pertencente a R.

Dedução formal da Simetria Hermitiana:

Calculamos o coeficiente espectral no índice de frequência espelhado N menos k aplicando a equação canônica de análise: X no índice N menos k é igual à somatória de n de zero a N menos um de x de n multiplicado pela exponencial de menos j dois pi vezes abre parênteses N menos k fecha parênteses vezes n sobre N.

Decompomos a exponencial complexa no produto de duas exponenciais: a exponencial de menos j dois pi vezes N vezes n sobre N, multiplicada pela exponencial de mais j dois pi vezes k vezes n sobre N.

Simplificando a primeira parcela, N sobre N cancela-se, restando a exponencial de menos j dois pi vezes n. Como n é um número inteiro, a exponencial de menos j dois pi vezes n representa n voltas completas no círculo trigonométrico, sendo rigorosamente igual a um mais zero j, ou seja, um.

Portanto, a expressão reduz-se a: X no índice N menos k é igual à somatória de n de zero a N menos um de x de n multiplicado pela exponencial de mais j dois pi vezes k vezes n sobre N.

Sendo o sinal x de n puramente real, temos que x de n é idêntico ao seu conjugado complexo. Logo, podemos expressar a soma inteira como o conjugado complexo da fórmula de análise original de X de k: X no índice N menos k é rigorosamente igual a X conjugado de k.

Em leitura natural contínua: o coeficiente espectral na posição N menos k é exatamente o conjugado complexo do coeficiente espectral na posição k.

Desdobramentos geométricos da simetria hermitiana:
1. Simetria Par da Magnitude: o módulo de X no índice N menos k é igual ao módulo do conjugado de X de k, o que equivale ao próprio módulo de X de k. O gráfico de magnitude do espectro é perfeitamente espelhado em torno da frequência de Nyquist, localizada na gaveta N sobre dois.
2. Simetria Ímpar da Fase: o ângulo de fase de X no índice N menos k é o negativo do ângulo de fase de X no índice k. O espectro de fase comporta-se de forma anti-simétrica.

Consequência fundamental: toda a informação física e matemática independente de um sinal puramente real de N pontos está inteiramente concentrada nas primeiras N sobre dois mais uma gavetas, cobrindo o intervalo de frequência contínua de zero Hertz até a frequência de Nyquist f s sobre dois. A metade superior do espectro, correspondente aos índices de N sobre dois até N menos um, atua meramente como a representação espelhada das frequências negativas do sinal analítico.

Terceira propriedade: a Álgebra Matricial da DFT e a Inversão Unívoca.
A transformação pode ser escrita na forma matricial compacta: o vetor espectral X é igual à matriz de Fourier W de ordem N multiplicada pelo vetor temporal x.

Onde x é o vetor coluna temporal de dimensão N, X é o vetor coluna espectral de dimensão N, e W subscrito N é a Matriz de Fourier de ordem N por N, cujos elementos na linha k e coluna n são definidos pelo fator de rotação complexo W elevado à potência k vezes n, onde W é a exponencial de menos j dois pi sobre N.

Calculando o produto da matriz W pela sua transposta conjugada W hermitiana:

O elemento da linha k e coluna l do produto W vezes W hermitiana é dado pelo produto interno da k-ésima linha de W pela l-ésima linha de W conjugada, que corresponde exatamente à somatória deduzida na ortogonalidade: a somatória de n de zero a N menos um da exponencial de menos j dois pi vezes abre parênteses k menos l fecha parênteses vezes n sobre N, a qual resulta em N multiplicado pelo delta de Kronecker de k e l.

Consequentemente, o produto matricial W vezes W hermitiana resulta na matriz identidade multiplicada pelo escalar N.

Isolando a matriz inversa de Fourier W elevado a menos um, obtemos: a matriz inversa de Fourier é igual a um sobre N multiplicado pela matriz W hermitiana.

Esta relação matricial elegante demonstra que a matriz de Fourier é unitária a menos do fator de escala de raiz quadrada de N, e que a síntese inversa temporal consiste estritamente em multiplicar o espectro pela matriz transposta conjugada W hermitiana e dividir todos os elementos pelo escalar N: o vetor temporal x é igual a um sobre N vezes W hermitiana multiplicada pelo vetor espectral X.

Quarta propriedade: o Princípio de Incerteza Tempo-Frequência.
Assim como na mecânica quântica e na análise harmônica contínua, vigora no processamento de sinais discretos a desigualdade da incerteza: o produto entre a dispersão temporal delta t e a dispersão em frequência delta ômega é limitado inferiormente por meio, isto é, delta t vezes delta ômega é maior ou igual a um sobre dois.

Análise dos casos extremos:
1. O Impulso Unitário Discreto no instante inicial: definindo x de n igual a um para n igual a zero, e zero para todo n maior que zero. Substituindo na fórmula da DFT, todos os termos anulam-se exceto para n igual a zero, onde a exponencial de zero vale um: X de k é igual a x de zero vezes a exponencial de menos j dois pi k vezes zero sobre N, resultando em um para todo k. O sinal está infinitamente concentrado no tempo em uma única amostra, e seu espectro resultante é perfeitamente plano, distribuindo sua energia de modo homogêneo sobre todas as N frequências discretas.
2. A Senoide Pura de Duração Infinita: reciprocamente, uma senoide de frequência única f zero que se estenda no tempo sem interrupção possui dispersão nula em frequência, exigindo uma duração temporal infinita para que não ocorra espalhamento em gavetas laterais.

---

### 3. As Quatro Versões de Implementação da DFT e Análise Assintótica de Complexidade

A literatura acadêmica e os ambientes laboratoriais consagram quatro abordagens distintas para a execução computacional da Transformada Discreta de Fourier:

Versão um, denominada notação de sinal ou signal: implementação canônica em Python puro por meio de laços de repetição aninhados. 
O algoritmo executa um laço externo percorrendo os N valores do índice de frequência k de zero até N menos um, e para cada k executa um laço interno percorrendo os N valores temporais n de zero até N menos um, acumulando a somatória analítica amostra por amostra.
Complexidade computacional: para cada uma das N saídas, são efetuadas N multiplicações complexas e N adições complexas. O custo total é rigorosamente quadrático, representado na notação assintótica por O de N ao quadrado. Para um sinal de áudio com N igual a mil e vinte e quatro amostras, a versão signal demanda um milhão e quarenta e oito mil quinhentas e setenta e seis multiplicações complexas, gerando um tempo de execução perceptível na casa de centenas de milissegundos.

Versão dois, denominada notação de base ou basis: exploração vetorial da projeção ortogonal.
Em vez de laços escalares aninhados, pré-computa-se o vetor de base complexo e de k para cada frequência e projeta-se o sinal temporal x por meio da função de produto interno complexo np ponto vdot de e de k por x. O comando vdot conjuga automaticamente o primeiro argumento, introduzindo nativamente o sinal negativo no expoente da análise de Fourier. A complexidade matemática permanece quadrática O de N ao quadrado, porém o overhead do interpretador Python sobre laços elementares é eliminado, acelerando o cálculo em cerca de quatro vezes em processadores modernos.

Versão três, denominada notação matricial ou matrix: formulação por álgebra linear densa.
Gera-se a tabela de todos os produtos de índices n vezes k em uma única operação matricial utilizando o produto externo vetorial entre o vetor coluna e o vetor linha: n entre colchetes dois pontos vírgula np ponto newaxis multiplicado matricialmente por n entre colchetes np ponto newaxis vírgula dois pontos. 
Aplica-se a exponencial complexa elemento a elemento para sintetizar a Matriz de Fourier W de ordem N por N, e calcula-se a transformação completa por uma única multiplicação de matriz por vetor: X igual a W multiplicado matricialmente por x.
Embora aproveite as rotinas altamente otimizadas de álgebra linear em C e Fortran da biblioteca BLAS e LAPACK, o consumo de memória principal escala com N ao quadrado: para N igual a sessenta e cinco mil quinhentas e trinta e seis amostras, a matriz W requer cerca de sessenta e quatro gigabytes de memória RAM, tornando a abordagem inviável para sinais longos.

Versão quatro, a Transformada Rápida de Fourier, ou FFT (do inglês Fast Fourier Transform), concebida por James Cooley e John Tukey em mil novecentos e sessenta e cinco, sob a arquitetura de Decimação no Tempo com base dois (Radix-2 DIT).

Dedução analítica da decomposição par e ímpar de Cooley-Tukey:

Consideremos uma sequência x de n de comprimento N, onde N é uma potência de dois, N igual a dois elevado a M. Separamos a somatória de análise da DFT em duas somatórias menores: uma acumulando os índices temporais pares n igual a dois vezes m, e outra acumulando os índices temporais ímpares n igual a dois vezes m mais um, com o novo índice m variando de zero até N sobre dois menos um:

X de k é a somatória de m de zero a N sobre dois menos um de x de dois m vezes a exponencial de menos j dois pi k vezes dois m sobre N, somada à somatória de m de zero a N sobre dois menos um de x de dois m mais um vezes a exponencial de menos j dois pi k vezes abre parênteses dois m mais um fecha parênteses sobre N.

Simplificamos o argumento da exponencial no primeiro somatório: o produto dois vezes m dividido por N equivale a m dividido por abre parênteses N sobre dois fecha parênteses.

Reconhecemos neste primeiro somatório exatamente a Transformada Discreta de Fourier de ordem N sobre dois aplicada à subsequência das amostras temporais com índices pares, a qual designamos por E de k (da palavra inglesa Even, par).

No segundo somatório, fatoramos a exponencial constante em relação a m para fora da somatória: a exponencial de menos j dois pi k sobre N.

Definimos o termo fatorado constante como o Fator Twiddle ou Fator de Rotação, representado pelo símbolo W subscrito N elevado à potência k: W subscrito N elevado a k é a exponencial de menos j dois pi k sobre N.

A somatória remanescente representa a Transformada Discreta de Fourier de ordem N sobre dois calculada sobre a subsequência das amostras temporais com índices ímpares, a qual designamos por O de k (da palavra inglesa Odd, ímpar).

Reescrevemos o espectro global X de k como a combinação linear de duas transformadas de metade do tamanho: X de k é igual a E de k mais o fator Twiddle W elevado a k multiplicado por O de k.

Propriedades periódicas cruciais e a Estrutura em Borboleta (Butterfly):

Como E de k e O de k são transformadas de ordem N sobre dois, suas saídas são naturalmente periódicas com período fundamental igual a N sobre dois: E de k mais N sobre dois é igual a E de k, e O de k mais N sobre dois é igual a O de k.

Entretanto, o Fator Twiddle W subscrito N possui período fundamental N. Avaliando o fator para o índice k mais N sobre dois: W elevado a k mais N sobre dois é a exponencial de menos j dois pi k sobre N multiplicada pela exponencial de menos j pi.

Pela relação de Euler, a exponencial de menos j vezes pi é igual ao cosseno de pi menos j vezes o seno de pi, o que resulta exatamente em menos um.

Portanto, o Fator Twiddle para a segunda metade do espectro inverte rigorosamente o seu sinal algébrico: W elevado a k mais N sobre dois é igual a menos W elevado a k.

Substituindo estas identidades para calcular a segunda metade do espectro, correspondente ao intervalo de frequências k mais N sobre dois, com k variando de zero a N sobre dois menos um:

X de k mais N sobre dois é igual a E de k menos o fator Twiddle W elevado a k multiplicado por O de k.

Agrupando as duas saídas fundamentais da Borboleta de Cooley-Tukey:
Para a primeira metade: X de k é igual a E de k mais o fator Twiddle W elevado a k multiplicado por O de k.
Para a segunda metade: X de k mais N sobre dois é igual a E de k menos o fator Twiddle W elevado a k multiplicado por O de k.

Em leitura natural contínua para leitor de tela: o coeficiente espectral da primeira metade X de k é igual a E de k mais o fator Twiddle W elevado a k vezes O de k. O coeficiente correspondente da segunda metade X de k mais N sobre dois é igual a E de k menos o fator Twiddle W elevado a k vezes O de k.

A elegância extraordinária desta formulação reside no fato de que o produto complexo do fator Twiddle W elevado a k pela transformada ímpar O de k é calculado uma única vez e reaproveitado simultaneamente para sintetizar duas gavetas de frequência distintas, bastando efetuar uma adição para a primeira metade e uma subtração para a segunda metade.

Dedução analítica da redução de complexidade assintótica:

A divisão recursiva de um vetor de tamanho N em duas partes de tamanho N sobre dois prossegue em cascata por exatamente logaritmo de N na base dois estágios, até atingir o caso base atômico de dois pontos, onde a DFT reduz-se a uma soma e uma diferença direta das amostras.

Em cada um dos logaritmo de N na base dois estágios, realizam-se N sobre dois operações de borboleta. Cada borboleta requer uma multiplicação complexa e duas adições complexas.

Consequentemente, o número total de multiplicações complexas da FFT é dado por N sobre dois multiplicado pelo logaritmo de N na base dois.

E o número total de adições complexas da FFT é dado por N multiplicado pelo logaritmo de N na base dois.

Comparação de desempenho computacional para N igual a mil e vinte e quatro amostras:
- Na DFT Canônica: N ao quadrado é igual a mil e vinte e quatro elevado ao quadrado, resultando em um milhão e quarenta e oito mil quinhentas e setenta e seis operações complexas.
- Na FFT Cooley-Tukey: N sobre dois vezes logaritmo de N na base dois é quinhentos e doze multiplicado por dez, resultando em cinco mil cento e vinte multiplicações complexas e dez mil duzentas e quarenta adições complexas.

A razão de aceleração teórica atinge N sobre o logaritmo de N na base dois, que para mil e vinte e quatro amostras é mil e vinte e quatro dividido por dez, aproximadamente cento e duas vezes mais rápido. Para blocos de sessenta e cinco mil quinhentas e trinta e seis amostras, a aceleração ultrapassa quatro mil vezes.

A exigência de potência de dois e a técnica de Preenchimento com Zeros (Zero-Padding):
O algoritmo Radix-2 requer que N seja divisível sucessivamente por dois até a unidade, inviabilizando a execução direta sobre vetores com comprimentos primos ou ímpares (por exemplo, um vetor de setecentas amostras).
A solução padrão da engenharia é o Zero-Padding: estende-se o vetor temporal anexando amostras nulas no final até completar a potência de dois imediatamente superior (neste caso, mil e vinte e quatro).
Fundamentação teórica do Zero-Padding: anexar zeros não altera o conteúdo espectral contínuo do sinal nem cria novas frequências. Ele atua como um interpolador ideal no domínio da frequência, amostrando a Transformada de Fourier em Tempo Discreto contínua (DTFT) em uma grade mais densa de gavetas, suavizando o traçado espectral.

Algoritmo de Inversão Rápida (IDFT) reaproveitando a FFT direta:
Para reconstruir o sinal no tempo sem implementar uma rotina separada para a IDFT, utiliza-se a identidade analítica baseada no conjugado complexo: a IDFT de X é igual a um sobre N multiplicado pelo conjugado da DFT calculada sobre o conjugado de X.

Demonstração: conjugar o vetor espectral X inverte o sinal da parte imaginária, transformando a exponencial de mais j dois pi k n sobre N na exponencial de menos j dois pi k n sobre N requerida pela rotina direta da FFT. Ao aplicar a FFT sobre o vetor conjugado e conjugar o resultado final dividindo por N, obtém-se o sinal temporal exato x de n com complexidade idêntica de N logaritmo de N.

---

### 4. Resolução Espectral, Bins e Mecânica do Vazamento Espectral (Spectral Leakage)

Ao calcular a Transformada Discreta de Fourier de N amostras adquiridas a uma cadência de amostragem f s, o contínuo de frequência de zero até a taxa f s é discretizado em N compartimentos de medição, denominados Bins Espectrais ou Gavetas de Frequência.

A frequência exata representada pela k-ésima gaveta espectral é dada pela relação linear: f de k é igual a k multiplicado pela resolução delta f, o que equivale a k vezes a taxa f s dividida por N.

A grandeza delta f expressa a Resolução Espectral do sistema: a resolução delta f é igual à taxa de amostragem f s dividida pelo número total de amostras N, o que corresponde rigorosamente ao inverso da duração total da janela de observação temporal T subscrito janela, expressa em segundos. Conclui-se que para aumentar a acuidade e separar componentes tonais muito próximas, é indispensável observar o sinal por um intervalo de tempo mais longo.

Origem analítica do Vazamento Espectral (Spectral Leakage):

Um sinal contínuo que ingressa no conversor analógico-digital é infinito no tempo. Ao selecionar N amostras para alimentar a DFT, estamos multiplicando implicitamente o sinal original x de n por uma Janela Retangular w de n que vale um para n entre zero e N menos um, e vale zero fora desse intervalo: o sinal janelado x subscrito w de n é o produto amostra por amostra de x de n pela janela retangular w de n.

Pelo teorema da convolução, a multiplicação no domínio do tempo equivale à convolução periódica no domínio da frequência entre o espectro verdadeiro do sinal e a Transformada de Fourier da janela retangular.

Dedução analítica da transformada da janela retangular e o Núcleo de Dirichlet:

A transformada de Fourier em tempo discreto de uma janela retangular de N amostras é expressa pela somatória finita da exponencial de menos j ômega n com n de zero a N menos um, que resulta na fração com numerador um menos a exponencial de menos j ômega N e denominador um menos a exponencial de menos j ômega.

Fatoramos metade do ângulo tanto no numerador quanto no denominador aplicando a fórmula de Euler para o seno:

No numerador: um menos a exponencial de menos j ômega N fatora-se na exponencial de menos j ômega N sobre dois multiplicada por duas vezes j vezes o seno de ômega N sobre dois.

No denominador: um menos a exponencial de menos j ômega fatora-se na exponencial de menos j ômega sobre dois multiplicada por duas vezes j vezes o seno de ômega sobre dois.

Dividindo o numerador pelo denominador, simplificam-se as constantes dois j e subtraem-se os expoentes das exponenciais, resultando na expressão analítica do Núcleo de Dirichlet: a resposta em frequência da janela é a exponencial de menos j ômega vezes abre parênteses N menos um fecha parênteses sobre dois, multiplicada pela fração com numerador seno de ômega N sobre dois e denominador seno de ômega sobre dois.

Em termos físicos e auditivos: a resposta em frequência da janela retangular é uma função sinc discreta periódica modulada por uma fase linear, conhecida como Núcleo de Dirichlet. A função apresenta um lóbulo principal central de altura N e uma infinidade de lóbulos secundários laterais cujos nós de cruzamento por zero ocorrem nos múltiplos inteiros de dois pi sobre N.

Mecânica do alinhamento espectral:
1. Caso Perfeito sem Vazamento: se a frequência física da oscilação f zero for um múltiplo inteiro exato da resolução delta f — isto é, f zero igual a k zero vezes delta f —, o centro da senoide posiciona-se no ápice da gaveta k zero. Nos centros de todas as outras gavetas k diferente de k zero, a frequência angular coincide precisamente com os nós de cruzamento por zero do numerador seno de ômega N sobre dois. Toda a energia do sinal é absorvida exclusivamente pela gaveta k zero e pela sua gaveta simétrica conjugada N menos k zero, sem que nenhuma energia vaze para as gavetas vizinhas.
2. Caso com Vazamento Espectral Severo: se a frequência física f zero cair entre duas gavetas inteiras (por exemplo, na posição k zero mais meio), o sinal temporal é cortado abruptamente em um instante em que a forma de onda não cruzou pelo zero, criando uma descontinuidade em degrau na fronteira periódica do bloco. As outras gavetas discretas da DFT deixam de coincidir com os nós de cruzamento por zero do núcleo de Dirichlet e passam a amostrar os lóbulos secundários da janela. A energia do tom central vaza e espalha-se por dezenas de gavetas adjacentes. Como os lóbulos laterais da janela retangular decaem muito lentamente, à razão de apenas um sobre ômega (com o primeiro lóbulo lateral atenuado em modestos menos treze decibéis), sinais de baixa intensidade vizinhos são completamente mascarados pelo espalhamento.

Mitigação do vazamento através do Janelamento Suave:

Para eliminar a descontinuidade das bordas, multiplica-se o sinal temporal antes da DFT por funções de ponderação suave cujas extremidades convergem gradualmente para zero:
- Janela de Hann: definida pela função cossenoidal elevada, onde cada peso w de n é igual a zero vírgula cinco menos zero vírgula cinco multiplicado pelo cosseno de dois pi vezes n dividido por N menos um. A atenuação do primeiro lóbulo lateral atinge menos trinta e dois decibéis, e a taxa de decaimento assintótico salta para dezoito decibéis por oitava.
- Janela de Hamming: ajusta os coeficientes para otimizar o cancelamento do primeiro lóbulo secundário, onde w de n é igual a zero vírgula cinquenta e quatro menos zero vírgula quarenta e seis multiplicado pelo cosseno de dois pi vezes n dividido por N menos um. Atinge uma atenuação de pico do primeiro lóbulo lateral de menos quarenta e três decibéis.

O compromisso de projeto inalienável: janelas suaves alargam a largura do lóbulo principal (de duas gavetas na janela retangular para quatro gavetas nas janelas de Hann e Hamming), reduzindo levemente a capacidade de separar dois tons extremamente próximos, em troca de extirpar o vazamento espectral sobre componentes distantes.

---

### 5. Aplicações Práticas de Filtragem e Separação Espectral

A transformação para o domínio da frequência converte a intrincada convolução temporal em uma simples multiplicação algébrica pontual, viabilizando o isolamento de instrumentos e a aniquilação de ruídos interferentes que ocupam as mesmas regiões de tempo.

Considere o problema acústico do laboratório: uma gravação contém a emissão harmônica de um violão dedilhado na frequência fundamental de novecentos Hertz, contaminada pela interferência estridente de uma guitarra elétrica na frequência de mil e duzentos Hertz.

Análise das gavetas e parametrização do sistema:
Adotando uma taxa de amostragem f s de oito mil cento e noventa e dois Hertz e um tamanho de bloco de análise N igual a oito mil cento e noventa e dois pontos, a resolução espectral é exatamente: oito mil cento e noventa e dois dividido por oito mil cento e noventa e dois, resultando em delta f igual a um Hertz por gaveta.

Nesta parametrização ideal, os tons posicionam-se com precisão milimétrica em gavetas inteiras:
- O violão em novecentos Hertz reside no índice k igual a novecentos.
- A guitarra em mil e duzentos Hertz reside no índice k igual a mil e duzentos.
- As frequências negativas simétricas residem nos índices N menos k: oito mil cento e noventa e dois menos novecentos igual a sete mil duzentos e noventa e dois para o violão, e oito mil cento e noventa e dois menos mil e duzentos igual a seis mil novecentos e noventa e dois para a guitarra.

Dedução matemática do colapso estrutural da Filtragem Unilateral:

Demonstraremos por que um filtro Notch que zere exclusivamente a gaveta positiva k igual a mil e duzentos falha de forma catastrófica.

Representemos a oscilação da guitarra no domínio do tempo como uma senoide pura de amplitude dois A e frequência angular discreta ômega zero: x da guitarra de n é igual a dois A vezes o cosseno de ômega zero vezes n, o que pela identidade de Euler se decompõe em A vezes a exponencial de mais j ômega zero n somada a A vezes a exponencial de menos j ômega zero n.

Pela propriedade da linearidade da Transformada de Fourier, este sinal decompõe-se em dois impulsos no domínio da frequência: um fasor positivo no índice k zero com amplitude A vezes N, e um fasor negativo no índice N menos k zero com amplitude idêntica A vezes N.

Suponha que um programador desavisado aplique uma máscara de filtragem unilateral, forçando o coeficiente no índice k zero a ser zero, mas mantendo intacto o coeficiente no índice N menos k zero com valor A vezes N.

Aplicando a Equação de Síntese Inversa IDFT para reconstruir o sinal temporal remanescente: a amostra reconstruída é um sobre N multiplicado pela somatória dos coeficientes filtrados pelas exponenciais de síntese.

Como todas as gavetas foram zeradas exceto a gaveta N menos k zero, o sinal reconstruído é dado por um sobre N multiplicado por abre parênteses A vezes N vezes a exponencial de mais j dois pi vezes abre parênteses N menos k zero fecha parênteses vezes n sobre N fecha parênteses. O fator N cancela-se, restando A vezes a exponencial de menos j dois pi vezes k zero vezes n sobre N.

Expandindo esta exponencial complexa pela identidade de Euler, obtemos: a parte reconstruída é igual a A vezes o cosseno de dois pi k zero n sobre N, menos j vezes A vezes o seno de dois pi k zero n sobre N.

A análise desta dedução analítica revela duas anomalias severas:
1. Permanência de metade da amplitude: a parte real remanescente é A vezes o cosseno, enquanto a oscilação original possuía amplitude dois A. Metade da amplitude da guitarra continua vibrando no sinal filtrado, atenuando a potência em meros seis decibéis em vez de extirpá-la.
2. Injeção de componentes imaginárias espúrias: a parte imaginária menos j vezes A vezes o seno é estritamente não nula. Como transdutores de áudio e alto-falantes reproduzem apenas grandezas físicas reais, o descarte descuidado da parte imaginária ou a sua manipulação corrompe a fase original e injeta ruído impulsivo no som.

A Regra de Ouro da Filtragem Notch para Sinais Reais:
Para extirpar integralmente uma componente senoidal preservando o equilíbrio físico da simetria hermitiana, o filtro rejeita-faixa deve zerar de forma simultânea e rigorosa o par conjugado de gavetas: o coeficiente no índice positivo k zero deve ser igual a zero e o coeficiente no índice conjugado N menos k zero deve ser igualmente igual a zero.

Ao zerar simultaneamente os índices mil e duzentos e seis mil novecentos e noventa e dois, ambos os fasores giratórios são removidos. A somatória da IDFT zera rigorosamente a componente indesejada e o sinal resultante recupera a nota de novecentos Hertz do violão com fidelidade absoluta e parte imaginária matematicamente nula.

---

### 6. Roteiro Prático e Instruções para o Jupyter Notebook no Laboratório 6

Esta seção estabelece o procedimento experimental detalhado do Laboratório 6, estruturado a partir dos códigos e dados reais presentes nos arquivos le zero seis sublinhado zero um sublinhado DFT hífen four hífen versions ponto i p y n b, le zero seis sublinhado v um sublinhado signal sublinhado notation ponto p y, le zero seis sublinhado duas sublinhado frequencias ponto p y e le zero seis sublinhado remover sublinhado guitarra ponto p y, localizados no diretório assets barras labs barra le zero seis sublinhado DFT.

Primeira etapa: ambiente computacional, leitura de áudio e reprodução sonora.
No Jupyter Notebook, inicializam-se as bibliotecas fundamentais importando numpy como n p, matplotlib ponto pyplot como p l t, time para cronometria, cmath para exponenciais complexas e IPython ponto display ponto Audio para renderizar reprodutores de som interativos no navegador.
Para scripts autônomos executados no terminal de comando do Linux (onde o IPython não se encontra disponível e o ambiente virtual não requer bibliotecas adicionais de áudio como PyAudio), utiliza-se o reprodutor nativo do sistema operacional. O script le zero seis sublinhado v um inspeciona o sistema e encaminha os dados de áudio ao primeiro utilitário existente: pw hífen play para servidores de áudio modernos PipeWire, paplay para servidores PulseAudio, aplay para arquitetura ALSA direta, ou ffplay com parâmetros que suprimem a exibição gráfica de vídeo.
Lê-se o arquivo train ponto wav, localizado no subdiretório sounds, contendo doze mil oitocentas e oitenta amostras com taxa de amostragem f s de oito mil cento e noventa e dois Hertz (um vírgula cinquenta e sete segundos de áudio mono de dezesseis bits). Converte-se o vetor para números de ponto flutuante dividindo as amplitudes inteiras por sessenta e cinco mil quinhentos e trinta e cinco.

Segunda etapa: teste unitário manual das quatro versões com vetor de quatro elementos.
Na célula de calibração preliminar, define-se o vetor de teste x igual a colchete um vírgula dois vírgula três vírgula quatro fecha colchete com N igual a quatro amostras.
Com N igual a quatro, a exponencial de menos j dois pi vezes n vezes k sobre quatro simplifica-se para menos j elevado a n vezes k, assumindo estritamente os valores cíclicos um, menos j, menos um ou mais j.
Executa-se a função dft sublinhado v um:
- Para k igual a zero: a soma é um mais dois mais três mais quatro, resultando no número dez mais zero j.
- Para k igual a um: a soma é um mais dois vezes menos j mais três vezes menos um mais quatro vezes mais j, resultando em menos dois mais dois j.
- Para k igual a dois: a soma é um mais dois vezes menos um mais três vezes um mais quatro vezes menos um, resultando em menos dois mais zero j.
- Para k igual a três: a soma é um mais dois vezes mais j mais três vezes menos um mais quatro vezes menos j, resultando em menos dois menos dois j.
O console do Jupyter exibe a lista esperada e em seguida executa a síntese inversa idft sublinhado v um, devolvendo com precisão exata o vetor temporal inicial colchete um vírgula dois vírgula três vírgula quatro fecha colchete.

Terceira etapa: benchmarking comparativo de desempenho das quatro versões.
Isolam-se as primeiras mil e vinte e quatro amostras do arquivo train ponto wav, definindo N igual a mil e vinte e quatro e f s igual a oito mil cento e noventa e dois Hertz. A função myDFT recebe o parâmetro version, com as opções signal, basis, matrix, fft e numpy, e a função myIDFT faz o caminho inverso.
Mede-se o tempo de cada abordagem com a função time ponto perf sublinhado counter. Medição de referência no notebook:
1. Versão signal, com laços for duplos: processa mais de um milhão de multiplicações escalares em Python puro, em cerca de seiscentos milissegundos.
2. Versão basis, com produto interno vetorial np ponto vdot: cerca de vinte e oito milissegundos.
3. Versão matrix, com a multiplicação densa pela matriz W: também cerca de vinte e oito milissegundos. Nesta máquina, basis e matrix empatam; os tempos dependem do computador e podem variar.
4. Versão fft, com a recursão de Cooley-Tukey de base dois: cerca de oito milissegundos.
5. Referência n p ponto f f t ponto f f t: cerca de sete centésimos de milissegundo, pois roda em código compilado.
A versão signal é cerca de setenta e quatro vezes mais lenta que a fft, medido no notebook, contra uma previsão teórica de cento e duas vezes menos operações, que é a razão N ao quadrado sobre N vezes logaritmo de N na base dois, para N igual a mil e vinte e quatro.
Verificação de integridade numérica: cada versão é comparada com o resultado de n p ponto f f t ponto f f t por n p ponto allclose, que retorna verdadeiro. O erro máximo é da ordem de dez elevado a menos onze nas versões signal, basis e matrix, e de cerca de três vezes dez elevado a menos quatorze na versão fft. A diferença vem apenas do arredondamento de ponto flutuante.
A mesma verificação vale para a síntese: as quatro versões de myIDFT reconstroem o sinal com erro máximo da ordem de dez elevado a menos treze, e de cerca de dois vezes dez elevado a menos dezesseis na versão fft. A reconstrução do arquivo inteiro, em treze blocos de mil e vinte e quatro amostras, pela versão signal, leva cerca de quinze segundos.
Uma célula adicional varia N de dezesseis até mil e vinte e quatro, em potências de dois, e plota os tempos em escala logarítmica, junto de retas de referência proporcionais a N ao quadrado e a N log N.
Restrição da FFT de base dois: com um vetor de mil amostras, a chamada myDFT com a opção fft gera o erro Signal length must be a power of 2. A saída usual é o zero padding: completar com zeros até a próxima potência de dois, que é mil e vinte e quatro, e conferir que o resultado coincide com np ponto fft ponto fft aplicado com tamanho mil e vinte e quatro.

Quarta etapa: reconstrução por simetria hermitiana e interpretação espectral do apito do trem.
Demonstra-se no notebook que, para o sinal de áudio real do trem, armazenar apenas quinhentos e treze coeficientes (correspondentes ao intervalo de zero até N sobre dois, com N igual a mil e vinte e quatro) preserva a totalidade da informação física.
Cria-se uma rotina de reconstrução que regenera os quinhentos e onze coeficientes restantes aplicando a simetria conjugada X de N menos k igual a X asterisco de k.
Aplica-se a síntese IDFT: o sinal recuperado coincide perfeitamente com o sinal temporal de entrada, apresentando um erro residual máximo da ordem de três vezes dez elevado a menos dezesseis e partes imaginárias nulas.
Inspeção das frequências dominantes do trem: com resolução espectral de oito Hertz por gaveta (oito mil cento e noventa e dois dividido por mil e vinte e quatro), o gráfico de magnitude revela três picos ressonantes nítidos do apito a vapor em setecentos e quatro Hertz (gaveta oitenta e oito), oitocentos e oitenta e oito Hertz (gaveta cento e onze) e mil cento e setenta e seis Hertz (gaveta cento e quarenta e sete), além de um harmônico em dois mil cento e vinte Hertz (gaveta duzentos e sessenta e cinco).

Etapa intermediária: ortogonalidade, Parseval e DFT dos sinais básicos.
Para N igual a dezesseis, constrói-se a matriz W com W de n k igual à exponencial de menos j dois pi n k sobre N. O notebook confirma que W multiplicada pela sua transposta conjugada é igual a N vezes a identidade, que o produto interno do vetor de base três com ele mesmo vale dezesseis, e que o produto interno entre os vetores de base três e cinco vale zero.
Para o trecho de mil e vinte e quatro amostras do trem, a energia no tempo e a energia na frequência dividida por N coincidem em trinta vírgula duzentos e sessenta e quatro mil, quinhentos e oitenta e oito. Essa é a igualdade de Parseval.
Com N igual a sessenta e quatro, o notebook verifica a DFT dos sinais básicos da biblioteca. O impulso tem módulo um em todas as frequências. O degrau de comprimento trinta e dois tem X de zero igual a trinta e dois e coeficientes nulos nos índices pares diferentes de zero. A exponencial com a igual a zero vírgula oito coincide com a soma geométrica fechada, um menos a elevado a N, dividido por um menos a vezes a exponencial de menos j dois pi k sobre N. A oscilação de período oito tem picos apenas em k igual a oito e k igual a cinquenta e seis, com altura trinta e dois. Para ruído gaussiano, a média de módulo ao quadrado de X de k em dois mil sorteios é de cerca de sessenta e quatro, previsto por N.

Quinta etapa: experimento do sinal com duas frequências, vazamento espectral e alinhamento em bins.
O experimento aparece em duas versões, com parâmetros diferentes de propósito.
No notebook, o sinal é a soma de duas senoides de oitocentos e dois mil e quatrocentos Hertz, com f s igual a nove mil e seiscentos Hertz e N igual a dois mil e quarenta e oito amostras. A resolução é nove mil e seiscentos dividido por dois mil e quarenta e oito, ou quatro vírgula seis oito sete cinco Hertz por bin. Os dois tons recebem tratamentos opostos. Dois mil e quatrocentos dividido por quatro vírgula seis oito sete cinco dá exatamente quinhentos e doze, um bin inteiro. Já oitocentos dividido por quatro vírgula seis oito sete cinco dá cento e setenta vírgula seis sete, que não é inteiro. Resultado medido: o tom de dois mil e quatrocentos Hertz aparece limpo no bin quinhentos e doze, com módulo mil e vinte e quatro vírgula cinco e amplitude recuperada de um vírgula zero zero. O tom de oitocentos Hertz vaza: o maior pico cai no bin cento e setenta e um, a oitocentos e dois Hertz, com módulo oitocentos e quarenta e seis e amplitude recuperada de apenas zero vírgula oitenta e três. O maior valor fora dos picos é de cerca de quatrocentos e vinte, em vez de zero. Este é o vazamento espectral: a frequência que não cai no centro de um bin espalha a energia pelos bins vizinhos.
No script le zero seis sublinhado duas sublinhado frequencias ponto p y, os tons são de novecentos e mil e duzentos Hertz, com f s igual a oito mil Hertz e N igual a oitocentas amostras. A resolução é de dez Hertz por bin, e os tons caem nos bins noventa e cento e vinte. O script mostra dois picos de módulo quatrocentos, que é A vezes N sobre dois, amplitude recuperada de um vírgula zero zero, e o maior valor fora dos picos é desprezível, da ordem de dez elevado a menos onze ou menos, só ruído de arredondamento. Aqui não há vazamento.
O aluno ouve sucessivamente os tons separados e depois a soma, e vê a mistura confusa no tempo virar linhas limpas na frequência.

Sexta etapa: tarefa de laboratório, remoção da guitarra e isolamento do violão puro.
O notebook faz isso nas células cinquenta e três a cinquenta e nove. O script le zero seis sublinhado remover sublinhado guitarra ponto p y faz o mesmo em blocos, com outros parâmetros.
1. Geração da mistura: o violão é uma senoide de novecentos Hertz com n p ponto sin, a oito mil cento e noventa e dois Hertz, por um segundo. A guitarra é um oscilador de mil e duzentos Hertz gerado por SIGNALgenerate no modo osc com período igual a f s dividido por mil e duzentos. A mistura é a soma.
2. Análise espectral: com N igual a oito mil cento e noventa e dois, a resolução é de um Hertz por bin. O violão ocupa o bin novecentos e o espelho sete mil duzentos e noventa e dois. A guitarra ocupa o bin mil e duzentos e o espelho seis mil novecentos e noventa e dois.
3. Remoção: zeram-se os dois bins da guitarra, o positivo mil e duzentos e o espelho seis mil novecentos e noventa e dois, que é N menos mil e duzentos. A saída do notebook é bins zerados: k igual a mil e duzentos e k igual a seis mil novecentos e noventa e dois.
4. Síntese e validação: aplica-se a IDFT e confere-se com np ponto allclose que a saída é o violão puro. O erro máximo medido é de cerca de seis vírgula três vezes dez elevado a menos treze.
5. A armadilha: se o aluno zerar só o bin mil e duzentos, esquecendo o espelho, a saída da IDFT fica complexa, com parte imaginária de até zero vírgula cinco, e a parte real ainda traz a guitarra com amplitude zero vírgula cinco, a metade da original. O notebook mostra isso de propósito.
6. Função reutilizável: a função apagar sublinhado frequencia recebe o sinal, f s, a frequência a apagar e uma meia largura opcional. Ela calcula a frequência de cada bin como o mínimo entre k e N menos k, vezes f s sobre N, o que já inclui o espelho, zera os bins dentro da faixa e devolve a IDFT. O notebook usa a função para remover a guitarra e também para remover o violão, deixando só a guitarra, e confere os dois casos.
No script em blocos, f s vale oito mil Hertz e N vale oitocentas amostras, com dez Hertz por bin. O violão cai no bin noventa, a guitarra no bin cento e vinte, e zeram-se os bins cento e vinte e seiscentos e oitenta, que é oitocentos menos cento e vinte. As duas contas com N diferente, oito mil cento e noventa e dois e oitocentos, são casos separados; o espelho é sempre N menos k.
7. Verificação auditiva: ouve-se a mistura e depois a saída, só com o violão.

---

## CAPÍTULO VII — BANCO DE QUESTÕES DE EXAME E PROVAS PRÁTICAS COM GABARITO ANALÍTICO

Abaixo encontram-se doze problemas conceituais e analíticos avançados, com suas respectivas resoluções completas:

---

### Questão 1

Enunciado: Dado um sinal digital de áudio periódico. Explique fisicamente e deduza por que reproduzir o mesmo vetor de amostras inalterado em um conversor digital-analógico com a taxa de amostragem dobrada de f s para duas vezes f s altera o timbre musical e a dimensão espacial audível do evento?

Gabarito Analítico:

A frequência audível emitida f zero relaciona-se de forma incondicional com a taxa de amostragem externa f s e com o número fixo de amostras por ciclo P armazenado no vetor, através da relação: f zero é igual a f s dividido por P. 

O número P de amostras contidas em cada ciclo está gravado de forma imutável no arquivo digital. Ao dobrar a cadência do relógio de leitura no conversor de f s para duas vezes f s, o cálculo da frequência emitida torna-se: duas vezes f s dividido por P, o que resulta exatamente em duas vezes a frequência fundamental original f zero. 

O efeito auditivo resultante é que a nota musical salta exatamente uma oitava inteira para cima na escala tonal. 

Simultaneamente, como a duração total do áudio em segundos é o número total de amostras dividido pela taxa de amostragem, dobrar a taxa reduz o tempo total de execução exatamente pela metade. O andamento do evento dobra de velocidade e as frequências de ressonância do corpo do instrumento são transpostas para cima, produzindo o conhecido efeito esquilo.

---

### Questão 2

Enunciado: Descreva a anomalia do colapso estrutural que ocorre nos cálculos de espectro caso se abandone o pino conjugado analítico na filtragem e se apague apenas o coeficiente positivo X de k em um sinal puramente real.

Gabarito Analítico:

Pela propriedade fundamental da Simetria Conjugada Hermitiana, qualquer sinal puramente real no tempo deve possuir um espectro onde o coeficiente no índice N menos k é o conjugado complexo do coeficiente no índice k. No plano complexo, a soma vetorial dessas duas componentes conjugadas cancela exatamente as partes imaginárias, garantindo que o sinal reconstruído no tempo possua apenas valores reais.

Se um filtro digital zerar apenas o coeficiente da gaveta positiva k, deixando intacto o coeficiente no índice simétrico N menos k, a simetria hermitiana é quebrada. 

Ao aplicar a Transformada Discreta de Fourier Inversa, dois desastres ocorrem simultaneamente:

Primeiro: cinquenta por cento da energia da frequência que se desejava eliminar permanecerá no áudio, pois a componente conjugada não foi atenuada.

Segundo: a falta do cancelamento vetorial fará com que a Transformada Inversa gere valores com partes imaginárias não nulas, injetando distorções de fase e ruídos artificiais severos na reprodução sonora.

---

### Questão 3

Enunciado: Enuncie a restrição analítica incondicional para que uma senoide em tempo discreto seja rigorosa e estritamente periódica no computador.

Gabarito Analítico:

No domínio do tempo contínuo, a função seno de ômega zero vezes t é perpétua e irrestritamente periódica para qualquer valor real de frequência ômega zero. 

Porém, no tempo discreto, a função seno de ômega zero vezes n entre colchetes só repete seus valores se houver um número inteiro N de amostras tal que a forma de onda complete exatamente um número inteiro k de ciclos de oscilação. Isso exige que ômega zero vezes N seja igual a dois pi vezes k.

Isolando os termos, a condição necessária e suficiente é que a razão entre a frequência angular discreta ômega zero e dois pi seja rigorosamente um número racional, podendo ser simplificada como a razão entre dois números inteiros k e N.

Se essa razão for irracional — como ocorre quando definimos a frequência ômega zero como um radiano por amostra, resultando na razão irracional um sobre dois pi —, a sequência discreta jamais repetirá seus valores exatos, sendo estritamente aperiódica.

---

### Questão 4

Enunciado: Qual a armadilha matemática da função arco tangente simples da divisão b sobre a, e como a função arco tangente dois resolve o cálculo de fase nos quatro quadrantes do plano complexo de Argand-Gauss?

Gabarito Analítico:

A fraqueza da função arco tangente simples reside no fato de que a divisão de b por a descarta os sinais independentes das coordenadas. 

Por exemplo, no segundo quadrante, com abscissa negativa menos um e ordenada positiva mais um, a divisão b sobre a resulta em menos um. No quarto quadrante, com abscissa positiva mais um e ordenada negativa menos um, a divisão b sobre a resulta exatamente no mesmo valor menos um. 

A função arco tangente simples é incapaz de discernir entre esses dois quadrantes opostos, retornando sempre menos pi sobre quatro radianos, o que está incorreto para o segundo quadrante. 

O mesmo erro ocorre entre o primeiro e o terceiro quadrantes, onde a divisão resulta em valores positivos idênticos.

A função arco tangente dois recebe as coordenadas b e a como dois parâmetros separados. Ela analisa individualmente os sinais de cada termo: mantendo o resultado no primeiro e quarto quadrantes, somando pi radianos quando a abscissa for negativa e a ordenada for positiva no segundo quadrante, e subtraindo pi radianos quando ambas as coordenadas forem negativas no terceiro quadrante, cobrindo com perfeição o intervalo angular contínuo de menos pi até mais pi radianos.

---

### Questão 5

Enunciado: Efetue a dedução analítica de j elevado a j a partir da Fórmula de Euler e determine o seu valor no ramo principal.

Gabarito Analítico:

Expressamos a unidade imaginária j na forma polar complexa. O número j possui magnitude um e argumento angular de pi sobre dois radianos, admitindo voltas periódicas de dois pi vezes k:

j é igual à exponencial de j multiplicado por pi sobre dois mais dois pi vezes k.

Elevando ambos os membros da igualdade à potência imaginária j, obtemos:

j elevado a j é igual à exponencial de j vezes a soma pi sobre dois mais dois pi vezes k, tudo elevado a j.

Multiplicando os expoentes pela propriedade fundamental das potências, o produto de j por j resulta em j ao quadrado. Como j ao quadrado é igual a menos um, temos:

j elevado a j é igual à exponencial de menos a soma pi sobre dois mais dois pi vezes k.

Para o ramo principal correspondente a k igual a zero, o termo reduz-se à exponencial de menos pi sobre dois, cujo valor numérico é aproximadamente zero vírgula vinte zero sete oito sete nove cinco sete seis três cinco. 

Este resultado demonstra de forma rigorosa que a unidade imaginária elevada a si mesma produz um número puramente real e positivo.

---

### Questão 6

Enunciado: Justifique analiticamente a redução da complexidade computacional de N ao quadrado para N multiplicado pelo logaritmo de N na base dois obtida pelo algoritmo de Cooley-Tukey Radix-2 em comparação com a DFT direta.

Gabarito Analítico:

A Transformada Discreta de Fourier direta requer, para cada um dos N coeficientes de frequência, a avaliação de uma somatória contendo N produtos de amostras por exponenciais complexas, totalizando N multiplicado por N, ou seja, N ao quadrado operações aritméticas complexas.

O algoritmo de Cooley-Tukey com base dois divide recursivamente a sequência temporal de N amostras em duas subsequências de tamanho N sobre dois: a sequência dos índices pares e a sequência dos índices ímpares. 

Através da simetria dos fatores de rotação Twiddle, onde a exponencial com deslocamento de N sobre dois é igual ao negativo da exponencial original, o algoritmo calcula dois pontos do espectro com uma única multiplicação complexa utilizando a estrutura de borboleta.

Essa divisão binária repete-se por logaritmo de N na base dois estágios sucessivos. Como em cada estágio são processadas N amostras, o custo computacional total desaba para N multiplicado pelo logaritmo de N na base dois. 

Para um vetor de mil e vinte e quatro amostras, isso reduz as operações de um milhão e quarenta e oito mil para cerca de dez mil duzentas e quarenta, representando um ganho de velocidade de aproximadamente cem vezes.

---

### Questão 7

Enunciado: Explique por que a arquitetura do algoritmo de Cooley-Tukey Radix-2 exige que o comprimento do vetor seja uma potência de dois, e descreva a técnica de preenchimento com zeros.

Gabarito Analítico:

O princípio estrutural da decimação no tempo no algoritmo Radix-2 exige que a sequência de entrada possa ser dividida exatamente pela metade em partes pares e ímpares, e que essas metades possam ser novamente divididas por dois sucessivamente até que restem borboletas atômicas elementares de apenas duas amostras.

Se o tamanho do vetor contiver fatores primos ímpares — por exemplo, setecentas amostras —, após três divisões sucessivas por dois deparamo-nos com o número oitenta e sete vírgula cinco, impossibilitando a partição binária e colapsando o algoritmo.

Para contornar esta restrição sem distorcer o conteúdo do sinal, o vetor é estendido anexando-se amostras com valor zero no final até atingir a potência de dois mais próxima, que para setecentas amostras seria mil e vinte e quatro. 

Esta técnica é denominada Preenchimento com Zeros, ou Zero-Padding. Ela não altera a informação espectral do sinal original, apenas interpola mais pontos no espectro de frequência, resultando em uma amostragem espectral mais densa e suave.

---

### Questão 8

Enunciado: Deduza a correlação física e matemática do coeficiente espectral X de zero da Transformada Discreta de Fourier e relacione-o com o Teorema de Conservação de Parseval.

Gabarito Analítico:

Avaliando a fórmula de análise da DFT para o índice de frequência k igual a zero, a exponencial de menos j vezes zero torna-se rigorosamente igual a um. 

A expressão simplifica-se para a soma direta de todas as amostras temporais: X de zero é igual à somatória de x de n variando de zero a N menos um. Dividindo esse valor por N, obtemos exatamente a média aritmética das amplitudes temporais do sinal, que representa fisicamente o componente de Corrente Contínua ou nível DC da onda.

O Teorema de Conservação de Parseval estabelece que a energia total calculada no domínio do tempo — dada pela soma dos quadrados dos módulos de todas as amostras x de n — é rigorosamente igual à energia total calculada no domínio da frequência — dada pela soma dos quadrados dos módulos dos coeficientes X de k, escalonada pelo fator um sobre N. 

O coeficiente X de zero contribui para a energia total com a parcela referente à energia da média contínua do sinal, comprovando que a transformação entre os domínios do tempo e da frequência preserva integralmente a energia física do sistema.

---

### Questão 9

Enunciado: Justifique a fundamentação física e acústica da exigência do filtro de média de duas amostras na malha de realimentação do algoritmo de Karplus-Strong, e explique a necessidade da compensação de meio atraso.

Gabarito Analítico:

Modelos primitivos de síntese por repetição direta de ruído produzem um som artificial e estéril, onde os harmônicos de alta frequência continuam vibrando indefinidamente sem qualquer perda de energia.

Em um instrumento real de cordas como o violão, a propagação mecânica da onda na corda e o contato com a ponte de madeira dissipam calor por atrito interno. Como os harmônicos agudos flexionam a corda por muito mais ciclos em um mesmo segundo do que a fundamental grave, as altas frequências perdem energia muito mais rapidamente.

A introdução de um filtro de média de duas amostras adjacentes na malha de realimentação implementa um filtro passa-baixas simples e eficiente. A cada volta na malha, os harmônicos agudos são atenuados muito mais do que os graves, transformando o ruído inicial áspero na ressonância aveludada e quente típica de uma corda dedilhada.

Contudo, calcular a média de duas amostras vizinhas introduz um atraso de fase intrínseco de meia amostra, ou zero vírgula cinco amostras. Para manter a afinação na frequência desejada, esse atraso deve ser subtraído do cálculo do tamanho do buffer, resultando na fórmula de afinação: M é igual à taxa de amostragem dividida pela frequência desejada, menos zero vírgula cinco.

---

### Questão 10

Enunciado: Elucide o vício algorítmico da desafinação em cents nas notas agudas no algoritmo de Karplus-Strong decorrente da quantização do buffer, e descreva a solução proposta por Jaffe e Smith.

Gabarito Analítico:

Na memória de um computador, o tamanho do buffer M deve ser obrigatoriamente um número inteiro de índices. 

Para notas musicais graves, o tamanho do buffer é grande: por exemplo, para a nota Ré dois a quarenta e quatro mil e cem Hertz, o período acústico total é de seiscentos vírgula sessenta e cinco amostras, demandando um atraso ideal do buffer de seiscentos vírgula quinze amostras. Arredondar este valor para o inteiro seiscentos e um introduz um erro de afinação minúsculo de apenas menos dois vírgula seis cents, imperceptível ao ouvido humano.

No entanto, para notas agudas, o tamanho do buffer é muito pequeno: para a nota Sol cinco, o período acústico total é de cinquenta e seis vírgula vinte e cinco amostras, demandando um atraso ideal do buffer de cinquenta e cinco vírgula setenta e cinco amostras. Arredondar para o inteiro cinquenta e seis introduz um desvio severo de menos sete vírgula seis cents, facilmente audível como uma nota desafinada.

Para solucionar essa limitação, David Jaffe e Julius Smith acoplaram à malha um filtro passa-tudo fracionário, ou Fractional Delay Filter. Este filtro digital possui ganho unitário em todas as frequências e permite introduzir um atraso de fase contínuo e fracionário, compensando com precisão a parte decimal descartada pelo arredondamento do índice inteiro.

---

### Questão 11

Enunciado: Explique a mecânica de falha que ocorre ao projetar um filtro Notch espectral caso se zere apenas a gaveta positiva k sem zerar simultaneamente a gaveta simétrica N menos k.

Gabarito Analítico:

Quando representamos um sinal real através da Transformada Discreta de Fourier, as oscilações senoidais no tempo decompõem-se em dois fasores complexos rotacionando em sentidos opostos: um localizado na frequência positiva k e o outro localizado na frequência negativa correspondente ao índice N menos k. 

As partes imaginárias desses dois fasores possuem sinais opostos e cancelam-se mutuamente na soma da Transformada Inversa, garantindo que o sinal no tempo seja puramente real.

Ao eliminar unilateralmente apenas o coeficiente da gaveta positiva k, extirpa-se apenas metade da energia da componente indesejada. Na reconstrução temporal via IDFT, a componente remanescente em N menos k continuará presente, resultando na permanência de metade da amplitude do ruído indesejado no áudio final.

Além disso, como o fasor negativo não terá mais o seu par positivo para cancelar a sua parte imaginária, o sinal temporal resultante apresentará valores complexos com partes imaginárias não nulas. Isso gera ruídos espúrios e corrupção estrutural dos dados, exigindo que qualquer filtro Notch para sinais reais zere simultaneamente os índices k e N menos k.

---

### Questão 12

Enunciado: Aborde a gênese física e matemática do Vazamento Espectral na Transformada Discreta de Fourier e como as janelas de Hann e Hamming atuam para mitigar este defeito.

Gabarito Analítico:

O Vazamento Espectral, ou Spectral Leakage, surge da discrepância entre a natureza contínua dos sinais físicos e a grade rígida e discreta das gavetas da DFT. 

A formulação matemática da DFT assume implicitamente que o bloco de N amostras analisado repete-se ciclicamente ao infinito. Se a frequência do sinal contínuo for um múltiplo exato do espaçamento entre as gavetas, o bloco conterá um número inteiro exato de ciclos e as extremidades conectar-se-ão perfeitamente.

Porém, se a frequência não coincidir exatamente com o centro de uma gaveta, o bloco terminará abruptamente no meio de um ciclo, gerando uma descontinuidade em degrau na transição periódica entre o final e o início do vetor. 

Essa descontinuidade abrupta age matematicamente como um choque de alta frequência, espalhando energia espectral para todas as gavetas vizinhas em lóbulos laterais artificiais.

Para mitigar este espalhamento, aplica-se uma janela de suavização temporal como a janela de Hann ou a janela de Hamming. Estas funções multiplicam o sinal por uma curva suave que força os valores nas bordas inicial e final do bloco a decaírem gradualmente até zero, eliminando o degrau e concentrando a energia espectral na frequência verdadeira do sinal.

---

## REFERÊNCIAS BIBLIOGRÁFICAS CITADAS

Abaixo constam as trinta e duas obras acadêmicas e publicações que fundamentam este tratado. Os títulos originais em inglês e autores são preservados para fins de busca e citação. Para consultar os links diretos, identificadores DOI e endereços web de cada obra, consulte o arquivo anexo chamado referências, sublinhado, d s p, com extensão ponto m d, na raiz do repositório.

Referência um: Artigo de Michael Unser intitulado "Sampling-50 Years After Shannon", publicado no periódico IEEE Transactions on Signal Processing, abordando a teoria moderna de amostragem e reconstrução.

Referência dois: Artigo intitulado "Laser noise residuals in LISA from on-board processing and time", publicado na revista Physical Review D, tratando de ruído estocástico e processamento temporal de alta precisão.

Referência três: Artigo intitulado "Autoregressive Stochastic Clock Jitter Compensation in Analog-to-Digital Conversion", publicado nos anais do IEEE, examinando variações temporais e incertezas em sistemas de amostragem.

Referência quatro: Artigo intitulado "Feasibility of Low Latency, Single-Sample Delay Resampling", publicado na revista científica Algorithms da editora MDPI, analisando interpolação e atraso fracionário.

Referência cinco: Dissertação acadêmica intitulada "Fourier and wavelet analysis of skin laser Doppler flowmetry signals", defendida na Universidade de Southampton, abordando transformadas espectrais e sinais biomédicos.

Referência seis: Artigo técnico intitulado "Real-Time Doppler and Ionospheric Dispersion Correction for Space Applications", disponibilizado no repositório arXiv, sobre filtragem adaptativa e sinais de radiofrequência.

Referência sete: Tese acadêmica intitulada "Extraction of Physical and Expressive Parameters in Sound Modeling", defendida na Universidade Aalto, com foco em respostas ao impulso e síntese acústica.

Referência oito: Publicação técnica intitulada "Splitting the unit delay: FIR and all pass filters design", disponibilizada na plataforma Academia.edu, cobrindo métodos de interpolação e retardo fracionário.

Referência nove: Artigo seminal de Kevin Karplus e Alex Strong intitulado "Digital Synthesis of Plucked-String and Drum Timbres", publicado no Computer Music Journal em mil novecentos e oitenta e três, apresentando o algoritmo original de Karplus-Strong.

Referência dez: Artigo fundamental de David Jaffe e Julius Smith intitulado "Extensions of the Karplus-Strong Plucked-String Algorithm", publicado no Computer Music Journal em mil novecentos e oitenta e três, introduzindo filtros passa-tudo fracionários e dinâmica de decaimento.

Referência onze: Monografia de Ben Lynn intitulada "Sound and Music: The Karplus-Strong Algorithm", disponibilizada pelo Departamento de Ciência da Computação da Universidade de Stanford.

Referência doze: Artigo científico intitulado "Simulation of guitar string sound using the extended Karplus-Strong", publicado na Revista Latam de Tecnologia e Música.

Referência treze: Livro clássico de Stefan Bilbao intitulado "Sound synthesis and physical modeling", publicado pela editora John Wiley and Sons, cobrindo equações diferenciais aplicadas à acústica musical.

Referência quatorze: Artigo técnico intitulado "Exploring Procedural Data Generation for Automatic Acoustic Guitar Synthesis", disponibilizado no repositório arXiv.

Referência quinze: Estudo acadêmico intitulado "Harmonic Modulator Envelope filters: Expanding Acoustic Possibilities", publicado na plataforma Janeway da editora da Universidade da Carolina do Norte.

Referência dezesseis: Artigo científico intitulado "Genetic Algorithm for Plucked String Synthesis", publicado no Journal of the Audio Engineering Society.

Referência dezessete: Notas de pesquisa de síntese sonora intituladas "Max: Audio synthesis, musical temperaments, and GCD buffers", documentadas no portal técnico x37v.com.

Referência dezoito: Manual de referência de Victor Lazzarini e colaboradores intitulado "The Public Csound Reference Manual", disponibilizado pelo Instituto de Matemática e Estatística da Universidade de São Paulo.

Referência dezenove: Livro de David Creasey intitulado "Audio Processes: Musical Analysis, Modulation, and Synthesis", abordando teoria de sinais de áudio e síntese computacional.

Referência vinte: Artigo técnico de Juhan Nam e colaboradores intitulado "Alias-Free Virtual Analog Oscillators Using Polynomial Transition Regions", publicado nas atas da Conferência Internacional de Efeitos de Áudio Digital DAFx no KAIST.

Referência vinte e um: Livro clássico de Dave Benson intitulado "Music: A Mathematical Offering", publicado pela Cambridge University Press e disponibilizado pela Universidade de Aberdeen.

Referência vinte e dois: Documentação técnica intitulada "Welcome to Csound! Manual Floss de Referência", versão oito ponto um, tratando de processamento de sinais e síntese física.

Referência vinte e três: Monografia matemática sobre séries de potências intitulada "Why is using arctan of one equal to pi over four tricky when calculating pi with a Taylor series, and how does Abel's theorem make it possible".

Referência vinte e quatro: Artigo acadêmico intitulado "Algorithmic Determination of a Large Integer in the Two-Term Machin-Like Formulas for Pi", publicado na revista Mathematics da editora MDPI.

Referência vinte e cinco: Artigo científico intitulado "A formula for pi involving nested radicals", publicado na revista de matemática aplicada da plataforma ResearchGate.

Referência vinte e seis: Livro clássico de Jonathan Borwein e Peter Borwein intitulado "Pi and the AGM: A Study in Analytic Number Theory and Computational Complexity", publicado pela editora John Wiley and Sons em mil novecentos e oitenta e sete.

Referência vinte e sete: Apostila e notas de aula intituladas "Fast Fourier Transform in DSP: Implementations, Algorithms and Architecture", detalhando a implementação e a complexidade do algoritmo de Cooley-Tukey.

Referência vinte e oito: Artigo histórico de James Cooley e John Tukey intitulado "An Algorithm for the Machine Calculation of Complex Fourier Series", publicado na revista Mathematics of Computation em mil novecentos e sessenta e cinco.

Referência vinte e nove: Notas de curso de Ivan Selesnick intituladas "Direct Computation, Radix-2 FFT, and Decimation-in-Time Algorithms", da Escola de Engenharia Tandon da Universidade de Nova York.

Referência trinta: Material didático universitário intitulado "Digital Signal Processing: Unit Two - Fast Fourier Transform Algorithms", publicado pelo Colégio de Engenharia e Tecnologia G. Pullaiah.

Referência trinta e um: Guia tutorial de projeto digital intitulado "The Fast Fourier Transform in Hardware: A Tutorial Based on FPGA Implementation", publicado pelo Departamento de Engenharia Elétrica do MIT.

Referência trinta e dois: Artigo de referência de Matteo Frigo e Steven Johnson intitulado "The Design and Implementation of FFTW3", publicado nos anais do IEEE, descrevendo a biblioteca FFTW3.
## Glossário Falado de Termos e Variáveis

Esta seção serve como referência para os nomes de variáveis e letras gregas ditados ao longo deste documento.

* Pi: a constante circular de valor aproximado três vírgula um quatro um cinco nove.
* Tau: a constante de tempo do sistema, que define a velocidade de decaimento ou resposta.
* Delta t: o passo temporal ou intervalo de tempo entre duas amostras consecutivas.
* F s: a frequência de amostragem, ou seja, quantas amostras são coletadas por segundo.
* T s: o período de amostragem, que é o inverso da frequência de amostragem.
* Teta: o ângulo de fase ou argumento de um número complexo.
* Ômega: a frequência angular, geralmente medida em radianos por segundo.
* Lambda: a raiz característica ou autovalor do sistema discretizado.
* N maiúsculo: o número total de amostras em um sinal ou bloco de processamento.
* N minúsculo: o índice da amostra atual no domínio do tempo discreto.
* K minúsculo: o índice da amostra atual no domínio da frequência discreta.
* Jota: a unidade imaginária, cuja raiz quadrada de menos um forma a base dos números complexos.
