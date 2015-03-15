## Enunciado da Avaliação 4 

Todos os arquivos na pasta do Add-In que será criado para resolver este projeto devem ser compactados em um único arquivo ZIP 
e enviados para avaliação. Antes de enviar o código para correção, teste-o exaustivamente. Este projeto diz respeito ao 
conteúdo visto em todo o curso. Para facilitar, foi fornecido um arquivo ZIP com uma base de dados de teste para a construção 
do script.
 
Crie um Toolbox com uma Tool, uma Combobox e um Button. A Combobox deve exibir uma lista com duas opções: WITHIN e INTERSECT. 
A Tool deve desenhar um retângulo e selecionar por localização (Select By Location) as feições de todas as camadas vetoriais 
adicionadas no projeto. A regra da seleção por localização deve ser a opção selecionada na Combobox. Ao ser pressionado, o 
Button deve determinar entre todas as camadas vetoriais adicionadas no projeto, aquelas que possuem um conjunto de feições 
selecionadas. Essas camadas devem ter suas feições selecionadas copiadas para um novo Shapefile. O novo arquivo deve ser 
gerado na mesma pasta do arquivo original, mas com um Selection_of_ antes. Por exemplo, as feições selecionadas de 
C:\Projeto\Bairros.shp devem ser copiadas ao caminho C:\Projeto\Selection_of_Bairros.shp. Para realizar a cópia, utilize via 
script o comando Copy Features.
 
Seguem algumas dicas:

* a)     Se houver seleção sobre a camada, o comando Copy Features copiará automaticamente apenas as feições selecionadas, 
ou seja, não há necessidade de nenhuma ação ou configuração adicional para copiar somente a seleção;
 
* b)     Para montar a variável string com o caminho e nome do arquivo de saída da operação Copy Features, se utilize das 
propriedades de pasta e nome de arquivo da camada de entrada que são retornadas pelo arcpy.Describe;
 
* c)      Ao contrário do que foi visto nos exemplos das últimas práticas do curso, a Combobox solicitada neste projeto tem 
seus itens fixos. Para alimentar as suas opções, basta no método __init__ iniciar a variável self.items já com os itens WITHIN 
e INTERSECT;
 
* d)     Para fazer a Tool desenhar retângulo ao pressionar, arrastar e soltar o botão esquerdo do mouse, é necessário colocar a
variável self.shape com o valor ‘Rectangle’ no método __init­­__ da Tool. Automaticamente retângulos poderão ser construídos,
invocando o método onRectangle;
 
* e)     O método onRectangle já fornece como entrada o retângulo construído pelo usuário com o mouse por meio da variável 
rectangle_geometry. Entretanto, para utilizar este retângulo na seleção por localização, é necessário transformá-lo em um 
polígono geográfico. Segue o código que deve ser colocando logo no início do método onRectangle para realizar esta conversão:
 
mxd = arcpy.mapping.MapDocument('current')
apenas para abreviar o nome da variavel que define o retangulo gerado
rec = rectangle_geometry
cria um array baseado nas posições dos vertices do retangulo
array = arcpy.Array([rec.lowerLeft, rec.lowerRight, rec.upperRight,  rec.upperLeft])
gera o poligono no sistema de coordenadas do Data Frame ativo
a variavel poly deve ser utilizada na selecao por localizacao mais a frente
poly = arcpy.Polygon(array,mxd.activeDataFrame.spatialReference)

#Critérios de pontuação:

* a) Criar o projeto do AddIn com as componentes (independe de código inserido pelo aluno): 1,0 ponto
* b) Criar corretamente o código para a Combobox: 1,0 ponto
* c) Criar corretamente o código para a Tool: 2,5 pontos
* d) Criar corretamente o código o Button: 2,5 pontos
* e) As componentes do AddIn estarem cumprindo corretamente com os objetivos do enunciado, ou seja, corretude pelo conjunto da 
obra: 3,0 pontos

