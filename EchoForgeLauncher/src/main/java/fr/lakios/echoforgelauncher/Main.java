package fr.lakios.echoforgelauncher;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.layout.StackPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;
import javafx.stage.StageStyle;

public class Main extends Application {

    @Override
    public void start(Stage primaryStage) {
        try {
            FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("/fr/lakios/echoforgelauncher/tiles.fxml"));
            StackPane root = fxmlLoader.load();

            // Créez un clip rectangulaire pour découper les coins
            Rectangle clip = new Rectangle();
            clip.setArcWidth(40); // Largeur des coins arrondis
            clip.setArcHeight(40); // Hauteur des coins arrondis
            clip.widthProperty().bind(root.widthProperty());
            clip.heightProperty().bind(root.heightProperty());
            root.setClip(clip);

            Scene scene = new Scene(root);
            scene.setFill(Color.TRANSPARENT); // Transparence pour les bords

            primaryStage.initStyle(StageStyle.TRANSPARENT); // Fenêtre sans bords natifs
            primaryStage.setScene(scene);
            primaryStage.setTitle("EchoForge Launcher");
            primaryStage.setResizable(false);
            primaryStage.show();
        } catch (Exception e) {
            System.err.println("Erreur lors du chargement : " + e.getMessage());
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        launch(args);
    }
}
