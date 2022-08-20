import java.io.*;


class emp implements Serializable {

    transient int x;
    int y;
    String nome;
    int id;

    public emp(String string, int i, int j, int k) {
    }

    public void Emp(String nome, int id, int a, int b){
        this.nome = nome;
        this.id = id;
        this.x = x;
        this.y = y;

    }

}

class Serial{

        public static void printdados(emp object1){
            System.out.println("nome: " + object1.nome);
            System.out.println("idade: " + object1.id);
            System.out.println("x: " + object1.x);
            System.out.println("y: " + object1.y);
        }


        /**
         * @param args
         * @throws ClassNotFoundException
         */
        public static void main(String[] args) throws ClassNotFoundException{
            emp object = new emp("Rodrigo", 17, 12, 2007);
            String filenome = "rodrigo.txt";

            try {
                FileOutputStream file = new FileOutputStream(filenome);

                ObjectOutputStream saida = new ObjectOutputStream(file);

                saida.writeObject(object);

                saida.close();
                file.close();

                System.out.println("Objeto foi serializado\n"
                                   + "Antes da deserialização");
                
                    printdados(object);

                    object.y = 2007;

            }

            catch (IOException ex) {
                System.out.println("IOException!!");
            }

            object = null;

            try {
                FileInputStream file = new FileInputStream(filenome);

                ObjectInputStream in = new ObjectInputStream(file);

                object = (emp)in.read.Object();

                in.close();
                file.close();
                System.out.println("Objeto foi deserializado\n"
                                   + "Dados depois da deserialização");

                printdados(object);
            }
            catch (IOException ex) {
                System.out.println("IOException !!");
            }
            catch (ClassNotFoundException ex){
                System.out.println("ClassNotFoundException !!");
            }
        }
    }