/**TilePane class is an extension of HBox, it creates panes that displays a tile
   Sean Anderson
   CS110C
*/

import javafx.scene.layout.HBox;
import javafx.geometry.Pos;
import javafx.scene.paint.Color;
import javafx.scene.text.Text;
import javafx.scene.text.Font;
//import javafx.

public class TilePane extends HBox
{
   //instance variables
   private Tile tile;
   private int row, column;
   private String letter = "";
   private Color color;
   private Text text;
   private boolean selected;
   
   /**TilePane constructor takes a tile and sets variables
      @param tile to be displayed
   */
   public TilePane(Tile tile)
   {
      this.tile = tile;
      letter = letter + tile.getLetter();
      row = tile.getRow();
      column = tile.getColumn();
      
      setUnselected();
      
      this.setAlignment(Pos.CENTER);
      if (letter.charAt(0) == 'Q')
         text = new Text("Qu");
      else
         text = new Text(letter);
      this.setPrefSize(100,100);
      this.getChildren().add(text);
   }
   
   /**setSelected sets a tiles status to selected and changes its color
   */
   public void setSelected()
   {
      this.setStyle("-fx-background-color: pink;"
      + "-fx-border-width: 5;" +
                  "-fx-border-color: blue;");
      selected = true;
      tile.selectTile();
   }
   
   /**setUnselected unselects a tile and changes its color back to yellow
   */
   public void setUnselected()
   {
      this.setStyle("-fx-background-color: white;"
            +"-fx-border-width: 5;" +
                  "-fx-border-color: blue;");
      selected = false;
      tile.unselectTile();

   }
   
   /**getSelected returns if a tile is selected
      @return selected status of tile
   */
   public boolean getSelected()
   {
      return selected;
   }
   
   /**getRow returns row number of tile
      @return row 
   */
   public int getRow()
   {
      return tile.getRow();
   }
   
   /**getColumn returns column number of tile
      @return column
   */
   public int getColumn()
   {
      return tile.getColumn();
   }
   
   /**getTile returns the tile of the pane
      @return tile
   */
   public Tile getTile()
   {
      return tile;
   }
}
      

