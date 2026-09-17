import json

file_path = "/home/deck/dev/sentinela/assets-main/labs/le03_discrete-time-signals/le03_convolution_impulse-response.ipynb"

with open(file_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = "".join(cell['source'])
        
        # P1
        if "1. Para um sinal stereo" in source or (cell['outputs'] == [] and cell['source'] == []):
            pass # We'll just replace the empty cells that come after the questions
            
    if cell['cell_type'] == 'markdown':
        source = "".join(cell['source'])
        
        if "### 1. Para um sinal stereo" in source:
            cell['source'] = [
                "### 1. Para um sinal stereo, qual será o resultado da conversão anterior?\n",
                "**Resposta:**\n",
                "A operação `np.mean(x, axis=1)` tira a média aritmética das amostras entre o canal esquerdo e o canal direito (Left/Right) para cada instante de tempo. O resultado é a conversão do áudio Stereo (2 dimensões/canais) para um áudio Mono (1 dimensão/canal único). Isso simplifica o processamento da convolução, pois agora operamos sobre um vetor 1D."
            ]
            
        elif "### 2. Qual é o tamanho do sinal resultante da convolução?" in source:
            cell['source'] = [
                "### 2. Qual é o tamanho do sinal resultante da convolução?\n",
                "Assista o vídeo do canal [3Blue1Brown](https://youtu.be/KuXjwB4LzSA) sobre convolução\n",
                "\n",
                "**Resposta:**\n",
                "Na convolução discreta linear, se o sinal de entrada $x[n]$ possui comprimento $N$ e a resposta ao impulso $h[n]$ possui comprimento $M$, o tamanho do sinal resultante $y[n]$ será de $N + M - 1$ amostras."
            ]
            
        elif "### 3. O sinal $y[n]$ tem o mesmo tamanho que $x[n]$? Por que?" in source:
            cell['source'] = [
                "### 3. O sinal $y[n]$ tem o mesmo tamanho que $x[n]$? Por que?\n",
                "**Resposta:**\n",
                "Não. Conforme a resposta anterior, o tamanho final é a soma das durações menos uma amostra ($N + M - 1$). Físicamente, isso ocorre porque a operação de convolução \"espalha\" a energia do sinal $x[n]$ ao longo da resposta do ambiente $h[n]$. Se tocarmos uma nota seca num salão (sinal curto), o som que escutaremos durará o tempo da nota original mais o tempo que a reverberação/eco demora para desaparecer (a cauda do IR)."
            ]
            
        elif "### 4. O que acontece se tenta reproduzir" in source:
            cell['source'] = [
                "### 4. O que acontece se tenta reproduzir $y[n]$ com o dobro de $f_s$? E com a metade $\\left (\\frac{f_S} {2}\\right)$? Por que?\n",
                "**Resposta:**\n",
                "- **Com o dobro de $f_s$ ($2 \\cdot f_s$):** O áudio será reproduzido **duas vezes mais rápido** e soará com as frequências **mais agudas** (efeito esquilo). Como as amostras digitais $y[n]$ são as mesmas, dizer à placa de som para tocar o dobro de amostras por segundo espreme o áudio no tempo.\n",
                "- **Com a metade de $f_s$ ($f_s / 2$):** O áudio será reproduzido **duas vezes mais devagar** e soará **mais grave**. \n",
                "Isso ocorre porque o vetor discreto $y[n]$ não contém informações de tempo real, apenas amplitudes brutas ordenadas. Quem dita a \"velocidade do tempo\" na conversão digital para analógico é exclusivamente a taxa de amostragem ($f_s$)."
            ]
            
        elif "### 5. O que é uma resposta ao impulso (IR)? Como podemos obté-la?" in source:
            cell['source'] = [
                "### 5. O que é uma resposta ao impulso (IR)? Como podemos obté-la?\n",
                "**Resposta:**\n",
                "A Resposta ao Impulso (IR) é a impressão digital acústica de um sistema Linear Invariante no Tempo (LTI). É o sinal de saída que o sistema produz quando alimentado por um impulso ideal (Sinal Delta de Dirac $\\delta[n]$).\n",
                "\n",
                "**Como obter na prática:** Pode ser gravada empiricamente estourando um balão, batendo palmas ou disparando um tiro de festim num ambiente (que atuam como um pulso abrupto de energia, simulando o Delta) e gravando a reverberação resultante com microfones. Outra forma moderna é aplicar a técnica de varredura de frequência (Sine Sweep) e usar a Deconvolução matemática para encontrar o IR com maior precisão e menos ruído."
            ]
            
        elif "### 6. Compare respostas ao impulso diferentes." in source:
            cell['source'] = [
                "### 6. Compare respostas ao impulso diferentes. Que diferenças pode reconhecer na comparação?\n",
                "**Resposta:**\n",
                "Comparando diferentes respostas ao impulso (como uma Igreja vs. uma Sala Pequena), notam-se diferenças em três pilares principais:\n",
                "1. **Tempo de Decaimento (RT60):** O tempo que a cauda de reverberação leva para desaparecer é muito longo na igreja e bem curto em espaços fechados e secos.\n",
                "2. **Reflexões Iniciais (Early Reflections):** A distância temporal entre o som direto e os primeiros ecos; salas maiores têm reflexões iniciais mais espaçadas.\n",
                "3. **Coloração (Resposta em Frequência):** Alguns IRs absorvem mais os agudos (ambientes com cortinas/carpetes), soando abafados; outros realçam graves ou médios (ressonâncias metálicas/madeira de caixas de guitarra acústica)."
            ]
            
        elif "#### 7.2. Com qual IR considera que ficou melhor? Por que?" in source:
            cell['source'] = [
                "#### 7.2. Com qual IR considera que ficou melhor? Por que?\n",
                "**Resposta:**\n",
                "*(Resposta Pessoal Baseada no Teste)*: Depende da aplicação estética. A utilização de um IR de *Cabinet* (Caixa de Guitarra) cria uma distorção agradável focada nos médios, tirando agudos excessivos. Por outro lado, IRs de *Hall/Church* acrescentam uma espacialidade grandiosa, fazendo o som soar épico, mas perdendo inteligibilidade devido à longa cauda de reverberação."
            ]

# Inject code for 7.1
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown' and '#### 7.1. Projete seu sinal com acústicas de salas diferentes' in "".join(cell['source']):
        # Replace the next code cell with the actual code
        if i + 1 < len(nb['cells']) and nb['cells'][i+1]['cell_type'] == 'code':
            nb['cells'][i+1]['source'] = [
                "# 7.1. Código para testar IRs diferentes\n",
                "from IPython.display import display, Audio\n",
                "\n",
                "# Lista de IRs que temos disponíveis para testar (Adicione na pasta se quiser mais)\n",
                "# Exemplo usando o arquivo freddy.wav (como voz) passando por diferentes IRs\n",
                "x_voz, fs_voz = audioread(os.path.join(SOUND_PATH, 'freddy.wav'))\n",
                "if x_voz.ndim > 1: x_voz = np.mean(x_voz, axis=1)\n",
                "\n",
                "ir_teste = 'Direct Cabinet N1.wav' # Você pode baixar IRs de igrejas na internet e colocar aqui!\n",
                "h_teste, fs_h = audioread(os.path.join(IR_PATH, ir_teste))\n",
                "if h_teste.ndim > 1: h_teste = np.mean(h_teste, axis=1)\n",
                "\n",
                "# Convolução da Voz/Instrumento com a nova Sala\n",
                "y_novo = np.convolve(x_voz, h_teste, mode='full')\n",
                "\n",
                "print('Voz Original:')\n",
                "display(Audio(data=x_voz, rate=fs_voz))\n",
                "print(f'Voz com Acústica da sala ({ir_teste}):')\n",
                "display(Audio(data=y_novo, rate=fs_voz))\n"
            ]

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook atualizado!")
