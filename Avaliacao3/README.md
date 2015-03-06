## Enunciado da Avaliação 3 

Este projeto diz respeito ao conteúdo visto até a Prática 04 da apostila. Crie um Toolbox que peça ao usuário: 
* (1) a pasta de entrada com os arquivos a serem cortados; 
* (2) um Shapefile do tipo polígono para máscara de corte; 
* (3) uma pasta de saída para salvar os arquivos resultantes. 
O script em Python pegará todos os arquivos ESRI Shapefile (*.shp) e Tagged Image Format File (*.tif) 
contidos nessa pasta de entrada e cortará pela máscara fornecida. Se o arquivo for Shapefile, corte-o 
utilizando o comando Clip. Se o arquivo for TIF, corte-o com o comando Extract By Mask do Spatial Analyst. 
Todos os arquivos resultantes do Clip e do Extract By Mask devem ser salvos na pasta de saída indicada pelo usuário.


Observação: O comando ListFeatureClass visto na Prática 04 apenas lista dados vetoriais em uma pasta, 
há outro comando similar para listar rasters. Olhem na documentação.

Como validação a ser feita na janela do Toolbox que chama o script, faça:
* a) A pasta de input não pode ser igual à pasta de output;
* b) O Feature Class fornecido como máscara de corte deve ter as geometriais do tipo polígono (não pode ser linha ou ponto, 
por exemplo);
Caso uma das condições acima não seja atendida, um erro deve ser emitido ao usuário imediatamente na janela de configuração 
da Toolbox e o script não pode ser executado. Para isto, use os recursos de validação (Validation) vistos na Prática 04.

Para facilitar, foi fornecido um arquivo ZIP com uma base de dados de teste para a construção do script.

A pontuação para essa avaliação fica:
* a) Listar os Shapefiles e os TIFs na pasta: 1,0 ponto
* b) Cortar os Shapefiles: 2,5 pontos
* c) Cortar os TIFs: 2,5 pontos
* d) Salvar os resultados corretamente na pasta de saída: 1,0 ponto
* e) Realizar as validações: 1,5 ponto cada validação

