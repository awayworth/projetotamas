/* ************************************************** */

function Limpar() {
	// Questão 01: (Construa uma função para limpar o formulário e o console na tela)
	document.getElementById('id_x').value='';
	document.getElementById('id_y').value='';
	document.getElementById('id_resultado').value='';
	document.getElementById('id_console').value = '';
}

function Adicionar(x, y) {
	// Questão 02: (Construa uma função para adicionar dois valores x e y e retornar o resultado)
	return x + y;
}

function Subtrair(x, y) {
	// Questão 03: (Construa uma função para subtrair dois valores x e y e retornar o resultado)
	return x - y;
}

function Multiplicar(x, y) {
	// Questão 04: (Construa uma função para multiplicar dois valores x e y e retornar o resultado)
    return x * y
}

function Dividir(x, y) {
	// Questão 05: (Construa uma função para dividir dois valores x e y e retornar o resultado)
    return (x / y);
}

function Executar(op) {
    // Questão 06: (Extraia da tela os valores de x e y e armazene em variáveis para posterior utilização)
    var x = parseFloat(document.getElementById('id_x').value);
    var y = parseFloat(document.getElementById('id_y').value);
    var resultado;
    
    // Questão 07: (De acordo com a opção 'op' chame a função para realizar o cálculo entre os valores x e y)
    switch(op){
        case "Adic":
            resultado = Adicionar(x, y);
            break;
        case "Sub":
            resultado = Subtrair(x, y);
            break;
        case "Mult":
            resultado = Multiplicar(x,y);
            break;
        case "Div":
            resultado = Dividir(x, y);
            break;
        default:
            resultado = 0;
            break;
    }

    // Questão 08: (Apresente o resultado da operação no componente identificado como: id_resultado)
    document.getElementById('id_resultado').value = resultado.toFixed(2);

    // Questão 09: (Escreva em uma string os valores de x, y e o resultado. Em seguida,
    //              imprima essa string no componente identificado como: id_console)
    var str = "Variável Valor1 = " + x + "\nVariável Valor2 = " + y + "\nVariável Resultado = " + resultado.toFixed(2) + "\n";
    document.getElementById('id_console').value = str;
}

/* ************************************************** */
