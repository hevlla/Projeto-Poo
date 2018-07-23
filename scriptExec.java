
import java.io.IOException; 

public class scriptExec {

    public static void main(String args[]) { 
        String path = null;
        System.out.print("\n#Executando script#"); 
        System.out.print("\n##Inciando processo"); 

        try {
        
            String[] commands = {"/bin/bash","-c",
                                "python3", "home/claudio/PycharmProjects/Projetos/main.py", "--image", 
                                "home/claudio/PycharmProjects/Projetos/placa3.jpg"};

            //Process proc = new ProcessBuilder(commands).start();
            Runtime.getRuntime().exec("/bin/bash -c python3 home/claudio/PycharmProjects/Projetos/main.py --image "
                    + "home/claudio/PycharmProjects/Projetos/placa3.jpg");

            System.out.print("\n##Processo Finalizado.");
        } 

        catch (IOException e) { 
            e.printStackTrace(); 
        } 
    } 
}


