EchoForge Launcher

EchoForge Launcher is a JavaFX application featuring a custom UI with a styled top bar, rounded corners, a blurred background, and interactive buttons (close, minimize, etc.). This project is built using JavaFX and Maven.
🛠️ Technologies Used

    JavaFX: Framework for building the user interface.
    Maven: Build and dependency management tool.
    Java 21: Java version used for this project.
    TilesFX: Library for creating dynamic visual elements.

📂 Project Structure

EchoForgeLauncher/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── fr/
│   │   │       └── lakios/
│   │   │           └── echoforgelauncher/
│   │   │               ├── Main.java
│   │   │               ├── TilesController.java
│   │   ├── resources/
│   │       └── fr/
│   │           └── lakios/
│   │               └── echoforgelauncher/
│   │                   ├── tiles.fxml
│   │                   ├── back-launcher.png
│   │                   ├── app-icon.png
│   │                   └── style.css
├── pom.xml
└── README.md

🚀 How to Run the Application
Prerequisites

    Java 21 or later
        Ensure Java is installed and correctly set up:

    java --version

Maven

    Install Maven if not already done:

        mvn --version

Steps to Run

    Clone this repository or download the source code:

git clone https://github.com/your-repo/EchoForgeLauncher.git
cd EchoForgeLauncher

Compile the project:

mvn clean compile

Run the application:

    mvn javafx:run

📦 Maven Dependencies

All dependencies are managed in the pom.xml file. Key dependencies include:

<dependencies>
    <dependency>
        <groupId>org.openjfx</groupId>
        <artifactId>javafx-controls</artifactId>
        <version>21</version>
    </dependency>
    <dependency>
        <groupId>org.openjfx</groupId>
        <artifactId>javafx-fxml</artifactId>
        <version>21</version>
    </dependency>
    <dependency>
        <groupId>eu.hansolo</groupId>
        <artifactId>tilesfx</artifactId>
        <version>21.0.3</version>
    </dependency>
</dependencies>

📜 Features

    Custom Interface:
        Rounded corners.
        Custom title bar with no native window decorations.
        Blur and transparency effects on the background.

    Interactive Top Bar:
        Minimize button.
        Close button.
        Dragging the window by clicking and holding the top bar.

    Main Container with a Button:
        "Connect" button with a sample action.

🛠️ Customization

    Change the Background Image: Replace the back-launcher.png file in the resources/fr/lakios/echoforgelauncher directory.

    Change the Application Icon: Replace the app-icon.png file in the same directory.

    Modify Styles: The style.css file contains the style rules. You can adjust colors, border radii, transparency, and more.

🚑 Troubleshooting

    Error FXML file not found:
        Make sure the tiles.fxml file exists in src/main/resources/fr/lakios/echoforgelauncher/.

    Maven Compatibility Issues:
        Ensure your JAVA_HOME is set correctly:

        echo $JAVA_HOME

    Transparency/Blur Issues:
        Ensure your operating system supports transparent and blurred windows.

📜 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it, as long as proper credit is given.
✨ Author

Lakios
Feel free to reach out for questions or suggestions. 😊
