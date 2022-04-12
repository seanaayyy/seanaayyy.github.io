/**BoggleGUI si the graphic user interface for the boggle game and uses tilepane, board,
   dictionary, game, tile, and word classes. A grid of tiles is displayed, user can 
   select tiles and spell words, points are counted and displayed
   Sean Anderson
   CS110C
*/

import javafx.application.Application; 
import javafx.application.Platform;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.Node;
import javafx.scene.layout.VBox;
import javafx.scene.layout.HBox;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.scene.input.MouseEvent;
import javafx.event.EventHandler;
import javafx.event.ActionEvent;

import java.util.ArrayList;
import javafx.scene.control.Button;
import javafx.scene.text.Text;
import javafx.scene.text.Font;
import javafx.geometry.Pos;
import java.io.*;

public class BoggleGUI extends Application
{
   private Game game; // the "guts" of the game
   private GridPane grid;  // the board of squares
   private BorderPane mainPane;  // primary layout of application
   private HBox buttonPane;  //start and end game
   private VBox infoPane;
   private VBox titlePane;
   private Text scoreWords;
   private Text title;
   private Button exit, newGame, check;
   private Board board;
   private Tile tile;
   private TilePane tilePane;
   private ArrayList<TilePane> tilePanes;
   private Word word;
   private ArrayList<String> wordList;
   private Text exitMessage;
   private Text invalidMessage;
   private Dictionary dictionary;
   private VBox msgPane;
   
   
   @Override
   public void start(Stage primaryStage)  {
   try
   {
      dictionary = new Dictionary("dictionary.txt");
      primaryStage.setTitle("Sean's Boggle");
      // set up panes
      mainPane = new BorderPane();
      grid = new GridPane();
      tilePanes = new ArrayList<>();
      
      // intialize game and set boggle board
      msgPane = new VBox();
      titlePane = new VBox();
      game = new Game();
      setBoggleBoard(); 
      mainPane.setCenter(grid);
      infoPane = new VBox();
      title = new Text("Let's Play Boggle!");
      title.setFont(Font.font("Arial",24));
      infoPane.setAlignment(Pos.CENTER);
      msgPane.setAlignment(Pos.CENTER);
      
      scoreWords = new Text("Points: " + game.getPoints() + "\n\nUsed Words:\n" + getWords());
      titlePane.getChildren().add(title);
      infoPane.getChildren().add(scoreWords);
      
      invalidMessage = new Text("\t\t\t");
      msgPane.getChildren().add(invalidMessage);
      
      mainPane.setRight(msgPane);
      mainPane.setTop(titlePane);
      mainPane.setLeft(infoPane);
      
      buttonPane = new HBox(10);
      buttonPane.setAlignment(Pos.CENTER);
      exit = new Button("End Game");
      exit.setOnAction( new EventHandler<ActionEvent>() {
         public void handle(ActionEvent e)
         {
            grid.getChildren().clear();
            buttonPane.getChildren().clear();
            exitMessage = new Text("GAME ENDED\nFinal Score: " + game.getPoints());
            grid.add(exitMessage, 0, 0);
            mainPane.setCenter(exitMessage);
         }
       });
      buttonPane.getChildren().add(exit);
      
      check = new Button("Check word");
      check.setOnAction( new EventHandler<ActionEvent>() {
         public void handle(ActionEvent e)
         {
            word = new Word(game.getSelectedTiles());
            msgPane.getChildren().remove(invalidMessage);
            if (dictionary.isValidWord(word))
               invalidMessage = new Text("");
            else
               invalidMessage = new Text("Invalid Word");
            msgPane.getChildren().add(invalidMessage);
            
            game.testSelected();
            infoPane.getChildren().remove(scoreWords);
            scoreWords = new Text("Points: " + game.getPoints() + "\n\nUsed Words:\n" + getWords());
            infoPane.getChildren().add(scoreWords);
            game.clearSelected();
            for (TilePane tp : tilePanes)
            {
               tp.setUnselected();
               tile = tp.getTile();
               game.removeFromSelected(tile.getRow(), tile.getColumn());
            }
            
         }
       });
      buttonPane.getChildren().add(check);

      
      newGame = new Button("New Game");
      newGame.setOnAction( new EventHandler<ActionEvent>()  {
         public void handle(ActionEvent e)
         {
         try
         {
            game = new Game();
            setBoggleBoard();
         }
         catch (IOException ioe)
         {
      System.out.println("IO Exception");
           } 
         }
       });
      buttonPane.getChildren().add(newGame);

      mainPane.setBottom(buttonPane);
      //add mainPane to scene and show stage with scene
      Scene scene = new Scene(mainPane);
      primaryStage.setScene(scene);
      primaryStage.show();
   }
   catch(FileNotFoundException e)
   {
      System.out.println("File not found.");
   } 
   
   catch(IOException e)
   {
      System.out.println("IOException found");
   }
   
   catch(Exception e)
   {
      System.out.println("Exception found");
   }
      
   }
   
   // event handler for user clicking on a tile
   
   /**handleClick changes the status of a tile based on its validity and prior status
   */
   public void handleClick(MouseEvent e)
   {  
      TilePane tp = (TilePane)(e.getSource());
      tile = tp.getTile();
      msgPane.getChildren().remove(invalidMessage);
      invalidMessage = new Text("");
      if (tp.getSelected() && tilePanes.get(tilePanes.size()-1).getTile().equals(tile))//if tile is already selected
      {
         game.removeFromSelected(tile.getRow(), tile.getColumn());
         tp.setUnselected();
         tilePanes.remove(tilePanes.size()-1);
      }
      else if (game.isValidSelection(tile.getRow(), tile.getColumn()))//if tile is valid selection
      {
         game.addToSelected(tile.getRow(), tile.getColumn());
         tp.setSelected();
         tilePanes.add(tp);
      }
      else
      {
         invalidMessage = new Text("Invalid Selection");
      }
      msgPane.getChildren().add(invalidMessage);
      
   }   
   // using information from game, create cell panes
   public void setBoggleBoard()
   {
      grid.getChildren().clear(); // clear the board
      mainPane.setCenter(grid);
      for (int row = 0; row <= 3; row++)
      {
         for (int col = 0; col <= 3; col++)
         {
            tile = new Tile(game.getTile(row,col));
            tilePane = new TilePane(tile);
            tilePane.setOnMouseClicked(this::handleClick);
            grid.add(tilePane, col, row);
            
         }
      }
      
   }
   
   public String getWords()
   {
      String s = "";
      for(String word : game.getWords())
      {
         s = s + "\n" + word;
      }
      return s;
      
   }
   
   public static void main(String [] args) {
      launch(args);
   }
   
}