class multiplicaçao{

public static void main (String[] args){
    int x = 5;
    int y = 2, z = 2, resultado;
    try {
        resultado = (x + z) * y;
        System.out.println("Resultado: " + resultado);


    }
    catch(ArithmeticException ex){
        System.out.println("ERROR! Insira um número.");
        }
    }

}