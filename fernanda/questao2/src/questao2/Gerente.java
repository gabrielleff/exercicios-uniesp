package questao2;

public class Gerente extends Funcionario {
    private String departamento;

    public Gerente(String nome, double salario, String departamento, String funcao) {
        super(nome, salario, funcao);
        this.departamento = departamento;
    }

    public double calcularBonus() {
        return salario + (getSalario() * 0.10);
    }

    public void setDepartamento(String departamento) {
        this.departamento = departamento;
    }

    public String getDepartamento() {
        return departamento;
    }

    @Override
    public String toString() {
        return "|-----------------FUNCIONÁRIO-----------------|" + "\n" +
                "|Nome: " + getNome() + "|" + "\n" +
                "|Função: "+ getFuncao() + "|" + "\n" +
                "|Departamento: " + departamento + "|" + "\n"+
                "|Salário: "+ getSalario() + "|" + "\n" +
                "|Salário com 10% de bônus: " + calcularBonus() + "|";

    }

}
