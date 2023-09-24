package atividade3;

public class Carro extends Veiculo {
    private int numPortas;
    public int getNumPortas() {
        return numPortas;
    }
    public void setNumPortas(int numPortas) {
        this.numPortas = numPortas;
    }

    public String imprimirDetalhes() {
        return "|-----------------DESCRIÇÃO DO VEÍCULO-----------------|" + "\n" +
                "|Marca: " + getMarca()  + "|" + "\n" +
                "|Modelo: "+ getModelo() + "|" + "\n" +
                "|Ano de fabricação: "+ getAnoFabricacao() + "|" + "\n" +
                "|Quantidade de portas: " + numPortas + "|";

    }

}
