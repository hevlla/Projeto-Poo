
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException; 
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class scriptExec {

    public static void main(String args[]) throws IOException { 
        String path = null;
        System.out.print("\n#Executando script#"); 
        System.out.print("\n##Inciando processo\n"); 
        String s = null;
        
        try {
            
            
            Process p = Runtime.getRuntime().exec("python3 //home//claudio//PycharmProjects//Projetos//main.py --image  //home//claudio//PycharmProjects//Projetos//placa3.jpg");

            BufferedReader stdInput = new BufferedReader (new InputStreamReader (p.getInputStream ()));
            System.out.println ("Aqui está a saída padrão do comando: \n");
            
            while ((s = stdInput.readLine())!= null){ 
                System.out.println(s);
            }
            System.out.print("\n##Processo Finalizado.");
    }

        catch (IOException e) { 
            e.printStackTrace(); 
        } 
    } 
}


