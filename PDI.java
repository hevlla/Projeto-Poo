package pdi;

import java.io.IOException;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.image.ImageView;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class PDI extends Application {
    ImageView imageview;

    @Override
    public void start(Stage stage) {
        try {
            Parent root = FXMLLoader.load(getClass().getResource("FXMLDocument.fxml"));
            imageview = new ImageView();
            VBox rootBox = new VBox();
            rootBox.getChildren().addAll(imageview);

            Scene scene = new Scene(root);
            stage.setScene(scene);
            stage.show();                       //Show the window
        } catch (IOException e){
        }
    }

    public static void main(String[] args) {
        launch(args);
    }
    
}
