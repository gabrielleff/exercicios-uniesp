const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function nivelarPessoas() {
  let menorAltura = Infinity;
  let maiorAltura = -Infinity;
  let mediaHomens = 0;
  let qtdHomens = 0;
  let qtdMulheres = 0;
  let contador = 0;

  function registrarAltura() {
    rl.question('Digite seu gênero (M/F): ', (genero) => {
      if (genero !== 'M' && genero !== 'F') {
        console.log('Gênero inválido. Digite M ou F.');
        registrarAltura();
        return;
      }

      rl.question('Digite sua altura (em metros): ', (altura) => {
        const alturaNum = parseFloat(altura);

        if (isNaN(alturaNum) || alturaNum <= 0) {
          console.log('Altura inválida. Digite um número positivo.');
          registrarAltura();
          return;
        }

        if (alturaNum < menorAltura) {
          menorAltura = alturaNum;
        }

        if (alturaNum > maiorAltura) {
          maiorAltura = alturaNum;
        }

        if (genero === 'M') {
          mediaHomens += alturaNum;
          qtdHomens++;
        } else {
          qtdMulheres++;
        }

        contador++;

        if (contador < 15) {
          console.log(`Altura ${contador} registrada.`);
          registrarAltura();
        } else {
          rl.close();

          if (qtdHomens > 0) {
            mediaHomens /= qtdHomens;
          } else {
            mediaHomens = 0;
          }

          console.log(`Maior altura é: ${maiorAltura.toFixed(2)} m, e a menor é: ${menorAltura.toFixed(2)} m`);
          console.log(`Média de altura dos homens: ${mediaHomens.toFixed(2)} m`);
          console.log(`Quantidade de mulheres: ${qtdMulheres}`);
        }
      });
    });
  }

  registrarAltura();
}

nivelarPessoas();
