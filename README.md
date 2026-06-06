# SISTEMA-SOLAR

## Sobre o Projeto

Este projeto consiste em um script de automação de imagem e design procedural focado na manipulação e rotulagem de mapas astronômicos. Desenvolvido em Python, o script `solarsystem.py` realiza a leitura de uma imagem base do espaço (`solar-system.jpg`) contida no diretório local e edita seus pixels utilizando recursos de processamento visual para renderizar textos informativos.

O programa atua injetando caracteres de texto diretamente sobre coordenadas vetoriais bidimensionais ($X$ e $Y$) previamente calibradas e específicas para cada elemento celeste. Dessa forma, o script mapeia a posição exata da estrela central (Sol) e de cada um dos planetas do sistema solar, escrevendo seus respectivos nomes na imagem e exportando o resultado final como um novo arquivo em formato `.png` salvo diretamente na pasta de mídias do projeto.

---

## Funcionalidades

* Leitura e manipulação de arquivos de imagem em formato comprimido (`.jpg`).
* Mapeamento de coordenadas cartesianas precisas ($X, Y$) para a inserção geométrica de elementos textuais.
* Renderização de fontes e textos customizados aplicados diretamente sobre a matriz de pixels da imagem original.
* Exportação e salvamento automatizado do novo arquivo modificado em formato de alta qualidade (`.png`) dentro da estrutura do repositório.

---

## Tecnologias Utilizadas

* **Python 3**
* Biblioteca principal: `OpenCV` (módulo `cv2`)
* Bibliotecas nativas auxiliares: `os`

---

## Objetivo

O principal objetivo deste projeto é explorar o desenho de primitivas gráficas e textos utilizando a biblioteca de visão computacional OpenCV. O foco técnico está em compreender o funcionamento de sistemas de coordenadas de imagens (onde a origem $(0,0)$ localiza-se no canto superior esquerdo) e aplicar funções de escrita (como o método `cv2.putText`) configurando tipos de fontes, escalas, cores em canais BGR e espessuras de traço de forma automatizada.

---

## Aprendizados

Durante o desenvolvimento deste projeto, foram aplicados conceitos como:

* Utilização de matrizes multidimensionais (NumPy arrays, que estruturam as imagens no OpenCV) para modificação direta de canais de cor e pixels.
* Calibração de pontos de acoplamento textuais baseando-se nas dimensões de largura e altura da imagem original.
* Uso prático de funções de escrita em imagens locais sem a necessidade de softwares externos de edição gráfica.
* Gerenciamento de caminhos relativos de arquivos usando o módulo `os` para garantir a portabilidade do salvamento do arquivo final dentro da pasta de destino (`assets\img/`).

---

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale a dependência do OpenCV através do seu terminal:
```bash
pip install opencv-python
```

3. Acesse a pasta do projeto:

```bash
cd SISTEMA-SOLAR
```

4. Execute o script principal para gerar a imagem rotulada:

```bash
python solarsystem.py
```

---

## Estrutura do Projeto
Nota: Mantive o formato de barra invertida (assets\img) exatamente como exibido na árvore de diretórios enviada para garantir a fidelidade à estrutura criada no seu repositório.

```text
SISTEMA-SOLAR/
│
├── assets\img/
│   ├── solar-system.jpg
│   └── (O novo arquivo .png gerado será salvo aqui)
│
├── solarsystem.py
├── README.md
└── index.html
```

---

## Licença
Este projeto foi desenvolvido exclusivamente para fins educacionais e de aprendizado.

Desenvolvido como prática de processamento digital de imagens e automação de design com Python, aplicando anotações textuais e coordenadas espaciais com OpenCV (cv2).
