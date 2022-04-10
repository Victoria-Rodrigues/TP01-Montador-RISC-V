# Exemplos de execução
make printarNoTerminal:
	python3 ./codigo.py entrada.asm
make printarNoArquivo:
	python3 codigo.py entrada.asm -o saida.txt
	python3 codigo.py entrada2.asm -o saidaArquivo2
	python3 codigo.py novosTestes.asm -o saidaNovosTestes