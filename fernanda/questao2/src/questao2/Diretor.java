package questao2;

public class Diretor extends Funcionario {
    private int acoes;

    public Diretor(String nome, double salario, int acoes, String funcao) {
        super(nome, salario, funcao);
        this.acoes = acoes;
    }

    public void setAcoes(int acoes) {
        this.acoes = acoes;
    }

    public int getAcoes() {
        return acoes;
    }

    @Override
    public String toString() {
        return "|-----------------FUNCIONÁRIO-----------------|" + "\n" +
                "|Nome: " + getNome() + "|" + "\n" +
                "|Função: "+ getFuncao() + "|" + "\n" +
                "|Salário: "+ getSalario() + "|" + "\n" +
                "|Quantidade de ações: " + acoes + "|";
    }

}
