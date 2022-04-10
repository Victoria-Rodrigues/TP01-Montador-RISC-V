<p align="center">
  <img width="350" height="350" alt="montador-risc-v" src="https://user-images.githubusercontent.com/81054281/162596242-55a0fdeb-4888-4cad-a8d7-25eb163fc326.png">
</p>


<h1 align="center">Trabalho prático - Organização de Computadores I</h1>

<p align="center">Montador RISC-V</p>

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=FINALIZADOO&color=GREEN&style=for-the-badge)


## Descrição do Projeto

O presente trabalho consiste na implementação de um Montador RISC-V, o qual receberá as instruções em assembly e as converterá para binário seguindo os critérios vistos em sala de aula. As instruções serão recebidas por um arquivo com extensão "asm", uma por linha, enquanto a saída dependerá da escolha do usuário, que pode optar por visualizar os dados no terminal ou em um arquivo. Caso a escolha seja por arquivo, os resultados serão armazenados, um por linha, em um arquivo com extensão "txt".


## ✔️ Técnicas e tecnologias utilizadas

- ``Linguagem de programação Python``
- ``Visual Studio Code (VS Code)``

## 🔨 Funcionalidades do projeto

O código do Montador foi denominado como "codigo.py" e, para melhor entendimento e visualização, foi estruturado em funções. A primeira função a ser chamada é responsável pela leitura do arquivo de entrada. Para cada linha do arquivo, a instrução selecionada é enviada como parâmetro para outra função, a qual a converte para seu correspondente em binário. Feita a conversão, analisa-se, de acordo com o comando informado pelo usuário, qual formato de saída deve ser seguido e, a partir disso, o resultado é printado no terminal ou armazenado em um arquivo.

Para obter os parâmetros informados pelo usuário no terminal, utilizou-se a biblioteca "sys". Esta biblioteca armazena tais parâmetros em um vetor, o qual foi utilizado para verificar a presença do termo "-o", que é o indicativo de que a saída deve ser informada por arquivo. Caso o termo for encontrado, obtém-se o nome do arquivo de saída desejado para realizar a abertura, ou criação, e armazenamento dos resultados.
 
