/*Tile class represents one tile on a board and stors the letter, column and row
numbers, and whether the tile is selected by the player
Sean Anderson
CS110C
*/

public class Tile
{
   //instance variables tile, row, column, flag
   private char letter = ' ';
   private int row, column;
   private boolean selected;
   private boolean compare;
   private String string;
   
   /**This Tile constructor accepts a string and two integers
      @param s a String, for when tile is qu and not a single letter
      @param r integer signifying the row position of the tile
      @param c integer signifying the column position of the tile
   */
   public Tile(String s, int r, int c)
   {
      
      setLetter(s);
      row = r;
      column = c;
   }
   
   /**This default constructor creates a tile object without initializing variables
   */
   public Tile()
   {
   }
   
   /**This tile constructor accepts a character and two integers
      @param l character for when tile is a single letter, not qu
      @param r integer signifying the row position of the tile
      @param c integer signifying the column position of the tile
   */
   public Tile(char l, int r, int c)
   {
      letter = l;
      row = r;
      column = c;
   }
   
   /**This copy constructor takes another tile and copies its attributes
      @param other tile to be copied
   */
   public Tile(Tile other)
   {
      setLetter(other.getLetter());
      row = other.getRow();
      column = other.getColumn();
   }
   /**setLetter method sets qu input as single character q
      @param s String that is "qu"
   */
   public void setLetter(String s)
   {
      if (s.equalsIgnoreCase("qu")||s.equalsIgnoreCase("q"))
         letter = 'Q';
      else
         letter = s.charAt(0);
   }
   
   /**setLetter method sets all letters except q
      @param l letter appearing on the tile
   */
   public void setLetter(char l)
   {
      letter = l;
   }
   
   /**getLetter returns letter to user
      @return letter on the tile
   */
   public char getLetter()
   {
      return letter;
   }
   
   /**setRow sets the row the tile is in 
      @param r the row number of the tile
   */
   public void setRow(int r)
   {
      row = r;
   }
   /**getRow returns the row number to user
      @return row the row number of the tile
   */
   public int getRow()
   {
      return row;
   }
   
   /**setColumn sets the column number of the tile
      @param c the column number of the tile
   */
   public void setColumn(int c)
   {
      column = c;
   }
   
   /**getColumn returns the column number of the tile
      @return column the column number for the tile
   */
   public int getColumn()
   {
      return column;
   }
   
   /**selectTile sets the tile selected as true
   */
   public void selectTile()
   {
      selected = true;
   }
   
   /**unselectTile sets tile selected as false
   */
   public void unselectTile()
   {
      selected = false;
   }
   
   /**getSelected returns whether the tile is selected or not
      @return selected the flag that indicates status of selection
   */
   public boolean getSelected()
   {
      return selected;
   }
   
   /**equals method checks if two tiles are the same
      @param otherTile tile to compare with
      @return compare if the tiles are the same
   */
   public boolean equals(Tile otherTile)
   {
      if (otherTile == null || letter == ' ')//if both tiles haven't been initialized
         compare = false;
      //tiles are the same if they have same location and letter
      else if (otherTile.getLetter() == letter &&
               otherTile.getRow() == row &&
               otherTile.getColumn() == column)
         compare = true;
      else
         compare = false;
      return compare;
      
   }
   
   /**toString method displays letter, column, and row of a tile
      @return string contains info of a tile
   */
   public String toString()
   {
      if (letter == 'Q')
      {
         string = "letter: " + "Qu" +
                  "\trow: " + row +
                  "\tcolumn: " + column + "\n";
      }
      else
      {  
         string = "letter: " + letter +
                  "\trow: " + row +
                  "\tcolumn: " + column + "\n";
      }
      return string;
   }
}