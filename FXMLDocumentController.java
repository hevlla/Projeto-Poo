package pdi;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;
import javafx.embed.swing.SwingFXUtils;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.stage.FileChooser;
import javafx.stage.FileChooser.ExtensionFilter;
import javax.imageio.ImageIO;

public class FXMLDocumentController implements Initializable {
    @FXML
    private Label label;
    
    @FXML
    private ListView listview;
    
    @FXML
    private Button button; 
    
    @FXML
    private ImageView imageview;
    
    @FXML
    private ImageView imageview2;
    
    @FXML
    private ImageView imageview3;
    
    @FXML
    private ImageView imageview4;
    
    @FXML
    private ImageView imageview5;
    
    public void ButtonAction(ActionEvent event) throws IOException {
        FileChooser fc = new FileChooser();
        
        fc.setInitialDirectory(new File("C:\\Users\\Hevlla\\Documents\\POO\\Banco de Imagens"));    //Alterar o diretorio
        fc.getExtensionFilters().addAll(new ExtensionFilter("Image Files", "*.jpg"));
        
        File selectedFile = fc.showOpenDialog(null);
        File arquivo2 = new File(("C:\\Users\\Hevlla\\Pictures\\Escala.jpg"));
        File arquivo3 = new File(("C:\\Users\\Hevlla\\Pictures\\Desfocada.jpg"));
        File arquivo4 = new File(("C:\\Users\\Hevlla\\Pictures\\Possiveis_caracteres.jpg"));
        File arquivo5 = new File(("C:\\Users\\Hevlla\\Pictures\\caracteres_Binario.jpg"));
        
        Image image2 = new Image(arquivo2.toURI().toString());
        Image image3 = new Image(arquivo3.toURI().toString());
        Image image4 = new Image(arquivo4.toURI().toString());
        Image image5 = new Image(arquivo5.toURI().toString());
        
        if (selectedFile != null){
            listview.getItems().add(selectedFile.getName());
            
            BufferedImage bufferedImage = ImageIO.read(selectedFile);
            
            Image image = SwingFXUtils.toFXImage(bufferedImage, null);
            
            imageview.setImage(image);
            imageview2.setImage(image2);
            imageview3.setImage(image3);
            imageview4.setImage(image4);
            imageview5.setImage(image5);
            
        } else{
            System.out.println("Arquivo inválido");
        }
    }
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        // TODO
    } 
}

