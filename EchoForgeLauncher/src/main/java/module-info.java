module fr.lakios.echoforgelauncher {
    requires javafx.controls;
    requires javafx.fxml;
    requires eu.hansolo.tilesfx;

    opens fr.lakios.echoforgelauncher to javafx.fxml;
    exports fr.lakios.echoforgelauncher;
}