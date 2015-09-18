#Cálculo da área de objetos

A idéia deste algoritmo é fazer o calculo da área de objetos em uma imagem de entrada, a qual é binária, onde os objetos são representados pelas áreas preenchidas pela cor branca e o fundo pela cor preta.

Para encontrar as áreas destes objetos, utilizou-se dos princípios de grafos, onde ao encontrar uma região inexplorada, ou seja, objeto que não teve sua área calculada, faz-se uma busca em profundidade e atribui um mesmo nível de cinza a todos pixels alcançáveis, ou seja, que pertencem ao mesmo objeto.
Este processo é repetido para toda a imagem, sendo que ao ser reiniciada a busca em profundidade - um novo objeto foi encontrado, preenche-se com um nível de cinza diferente, para ser possível diferencia-los posteriormente.

Quando é terminado este processo, plota-se o histograma da imagem final, o qual possui um valor no eixo Y que corresponde a quantidade de pixels de cada objeto, ou seja, a área de cada um.

A seguir estão alguns exemplos testados, onde tem-se a imagem de entrada em preto e branco, como saída tem-se a imagem com cada um dos objetos preenchidos com um nível diferente, além do histograma correspondente.

### Exemplo de execução:


Input:

![](https://raw.githubusercontent.com/rodrigogiraldi/areaObjetos/master/inputs/objetos1.png)

Output:

![](https://raw.githubusercontent.com/rodrigogiraldi/areaObjetos/master/outputs/objetos1.png)

Histograma:

![](https://raw.githubusercontent.com/rodrigogiraldi/areaObjetos/master/histogramas/objetos1.png)
