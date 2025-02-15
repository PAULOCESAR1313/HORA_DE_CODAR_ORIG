/* 1 - CRIANDO UMA FUNÇÃO */

/*function minhaFuncao()
{
    console.log("Testando minha função");
}

minhaFuncao();

let minhaFuncaoEmVariavel = function ()
{
    console.log("Testando função em uma variavel");
};

minhaFuncaoEmVariavel();

function funcaoComParamentro(txt)
{
    console.log(`Imprimindo: ${txt}`);
};

funcaoComParamentro("teste 1");
funcaoComParamentro("outro teste");*/

// 2 - Retorn

const a = 10;
const b = 20;
const c = 30;
const d = 40;

function soma(n1, n2)
{
    return n1 + n2;
}

const resultados = soma(a, b);

console.log(resultados);
console.log(soma(c, d));