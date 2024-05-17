class Roupa {
    constructor() {
        this.marca = '';
        this.cor = '';
        this.tam = 0;
        this.quant = 0;
        this.preco = 0.0;
        this.total = 0.0;
    }

    get_Marca() {
        return this.marca;
    }

    get_Cor() {
        return this.cor;
    }

    get_Tam() {
        return this.tam;
    }

    get_Quant() {
        return this.quant;
    }

    get_Preco() {
        return this.preco;
    }

    get_Total() {
        return this.total;
    }

    set_Marca(marca) {
        this.marca = marca;
    }

    set_Cor(cor) {
        this.cor = cor;
    }

    set_Tam(tam) {
        this.tam = tam;
    }

    set_Quant(quant) {
        this.quant = quant;
    }

    set_Preco(preco) {
        this.preco = preco;
    }

    calcula_Total() {
        this.total = this.quant * this.preco;
    }

    toString() {
        return `Marca: ${this.marca}\nCor: ${this.cor}\nTamanho: ${this.tam}\nQuantidade: ${this.quant}\nPreço: ${this.preco}\n\nTotal: ${this.total}\n`;
    }
}

function Limpar() {
    document.getElementById('id_marca').value = '';
    document.getElementById('id_cor').value = '';
    document.getElementById('id_tam').value = '';
    document.getElementById('id_quant').value = '';
    document.getElementById('id_preco').value = '';
    document.getElementById('id_total').value = '';
    document.getElementById('id_console').value = '';
}

function Executar() {
    var marca = document.getElementById('id_marca').value;
    var cor = document.getElementById('id_cor').value;
    var tam = document.getElementById('id_tam').value;
    var quant = parseFloat(document.getElementById('id_quant').value);
    var preco = parseFloat(document.getElementById('id_preco').value);

    var roupa = new Roupa();
    
    roupa.set_Marca(marca);
    roupa.set_Cor(cor);
    roupa.set_Tam(tam);
    roupa.set_Quant(quant);
    roupa.set_Preco(preco);
    
    roupa.calcula_Total();
    document.getElementById('id_total').value = roupa.get_Total();
    document.getElementById('id_console').value = roupa.toString();
}
