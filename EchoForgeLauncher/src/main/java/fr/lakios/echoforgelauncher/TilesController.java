package fr.lakios.echoforgelauncher;

import javafx.fxml.FXML;
import javafx.scene.effect.BoxBlur;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;

public class TilesController {

    @FXML
    private HBox customBar; // Barre noire personnalisée

    @FXML
    private ImageView backgroundImage;

    @FXML
    private ImageView logoImage;

    private double xOffset = 0;
    private double yOffset = 0;

    public void initialize() {
        // Charger l'image de fond
        Image bgImage = new Image(getClass().getResource("/fr/lakios/echoforgelauncher/back-launcher.png").toExternalForm());
        backgroundImage.setImage(bgImage);

        // Appliquer un effet de flou à l'image de fond
        BoxBlur blurEffect = new BoxBlur(20, 20, 3);
        backgroundImage.setEffect(blurEffect);

        // Charger le logo
        Image logo = new Image(getClass().getResource("/fr/lakios/echoforgelauncher/app-icon.png").toExternalForm());
        logoImage.setImage(logo);

        // Configuration de la barre personnalisée pour déplacer la fenêtre
        configureDraggableWindow();
    }

    private void configureDraggableWindow() {
        customBar.setOnMousePressed(event -> {
            Stage stage = (Stage) customBar.getScene().getWindow();
            xOffset = event.getSceneX();
            yOffset = event.getSceneY();
        });

        customBar.setOnMouseDragged(event -> {
            Stage stage = (Stage) customBar.getScene().getWindow();
            stage.setX(event.getScreenX() - xOffset);
            stage.setY(event.getScreenY() - yOffset);
        });
    }

    @FXML
    public void handleConnect() {
        System.out.println("Bouton 'Se connecter' cliqué !");
    }

    @FXML
    public void handleMinimize() {
        Stage stage = (Stage) backgroundImage.getScene().getWindow();
        stage.setIconified(true);
    }

    @FXML
    public void handleClose() {
        Stage stage = (Stage) backgroundImage.getScene().getWindow();
        stage.close();
    }
}
