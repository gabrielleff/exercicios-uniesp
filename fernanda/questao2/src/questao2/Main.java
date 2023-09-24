package questao2;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		 try (Scanner sc = new Scanner(System.in)) {
	            System.out.println("Digite seu nome: ");
	            String nome = sc.next();

	            System.out.println("Digite seu salário: ");
	            double salario = sc.nextDouble();

	            System.out.println("Você é um Gerente ou o Diretor? ");
	            String funcao = sc.next();

	            Funcionario f = new Funcionario(nome, salario, funcao);


	            if ("Gerente".equalsIgnoreCase(funcao)) {
	                System.out.println("Digite seu departamento: ");
	                String departamento = sc.next();

	                Gerente g = new Gerente(nome, salario, departamento, funcao);

	                System.out.println(g);

	            } else if ("Diretor".equalsIgnoreCase(funcao)) {
	                System.out.println("Digite o número de ações da empresa PetShop Mundo animal pertencentes a você: ");
	                int acoes = sc.nextInt();

	                Diretor d = new Diretor(nome, salario, acoes, funcao);

	                System.out.println(d);
	            } else {
	                System.out.println(f);
	            }
	        }
	    }

	}
