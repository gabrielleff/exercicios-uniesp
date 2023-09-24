package atividade3;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		 try(Scanner sc = new Scanner(System.in)){

	            System.out.println("Selecione um de tipo de veículo, Carro ou Moto: ");
	            String opcao = sc.next();

	            switch (opcao){
	                case "Carro":
	                    Carro carro = new Carro();

	                    System.out.println("Digite a marca do carro: ");
	                    carro.setMarca(sc.next());

	                    System.out.println("Digite o modelo do carro: ");
	                    carro.setModelo(sc.next());

	                    System.out.println("Digite o ano de fabricação do carro: ");
	                    carro.setAnoFabricacao(sc.nextInt());

	                    System.out.println("Digite a quantidade de portas do carro: ");
	                    carro.setNumPortas(sc.nextInt());

	                    System.out.println(carro.imprimirDetalhes());
	                    break;

	                case "Moto":
	                    Moto moto = new Moto();

	                    System.out.println("Digite a marca da moto: ");
	                    moto.setMarca(sc.next());

	                    System.out.println("Digite o modelo da moto: ");
	                    moto.setModelo(sc.next());

	                    System.out.println("Digite o ano de fabricação da moto: ");
	                    moto.setAnoFabricacao(sc.nextInt());

	                    System.out.println("Digite a quantidade de cilíndradas: ");
	                    moto.setCilindradas(sc.nextInt());

	                    System.out.println(moto.imprimirDetalhes());
	                    break;

	                default:
	                    System.out.println("Opção inválida!");
	            }
	        }
	    }

	}
