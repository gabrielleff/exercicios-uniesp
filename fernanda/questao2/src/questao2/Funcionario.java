package questao2;

public class Funcionario {
	
	 protected String nome;
	    protected double salario;
	    protected String funcao;

	    public Funcionario(String nome, double salario, String funcao) {
	        this.nome = nome;
	        this.salario = salario;
	        this.funcao = funcao;
	    }

	    public void setNome(String nome) {
	        this.nome = nome;
	    }

	    public String getNome() {
	        return nome;
	    }

	    public void setSalario(double salario) {
	        this.salario = salario;
	    }

	    public double getSalario() {
	        return salario;
	    }

	    public void setFuncao(String funcao) {
	        this.funcao = funcao;
	    }

	    public String getFuncao() {
	        return funcao;
	    }

}
