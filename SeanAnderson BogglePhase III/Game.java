/**Game class implements all aspects of Boggle:
   classes Dictionary, Board, Tile, and Word are used
   This class enforces rules of the Boggle game
   Sean Anderson
   CS100C
*/

import java.util.ArrayList;
import java.io.*;

public class Game
{
   //instance variables
   private ArrayList<Tile> selected;
   private ArrayList<String> selectedLetters;
   private ArrayList<ArrayList> usedWords;
   private String string;
   private Tile last;
   private Tile tile;
   private Board board;
   private Word word;
   private ArrayList<String> words;
   private int points;
   private boolean isValid;
   private Dictionary dictionary;
   
   /**Game constructor initializes variables
   */
   public Game() throws IOException
   {
      board = new Board();
      points = 0;
      dictionary = new Dictionary("dictionary.txt");
      words = new ArrayList<String>();
      selected = new ArrayList<Tile>();
      selectedLetters = new ArrayList<String>();
   }
   
   /**isValidSelection tests if a tile is a valid selection
      @param r row of the selected tile
      @param c column of the selected tile
      @return isValid if tile is valid
   */
   public boolean isValidSelection(int r, int c)
   {
      if (selected.size() == 0)
         isValid = true;
      else if (r>3 || r<0 || c>3 || c<0)
         isValid = false;
      else if (r==3)
      {
         System.out.println("hello");
         isValid = true;
      }
      else if ((last.getRow()>= r-1 && last.getRow()<=r+1) &&
             (last.getColumn()>= c-1 && last.getColumn()<=c+1))
      {
         isValid = true;
      }
      else if (r==3)
      {
         System.out.println("hello");
         isValid = true;
      }
      else
         isValid = false;
      for (Tile tile : selected) //cannot select an already selected tile
      {
         if (tile.equals(getTile(r,c)))
            isValid = false;
      }
      return isValid;
   }
   
   /**addToSelected adds a tile based on coordinates to selected list
      @param r int representing row
      @param c int representing column
   */
   public void addToSelected(int r, int c)
   {
      tile = new Tile(board.getTile(r,c));
      selected.add(tile);
      last = new Tile(tile);
      if (tile.getLetter() == 'Q')
         selectedLetters.add("Qu");
      else
         selectedLetters.add(""+tile.getLetter());
   }
   
   /**removeFromSelected removes a tile based on coordinates from list
      @param r int representing row
      @param c int representing column
   */
   public void removeFromSelected(int r, int c)
   {
      if (last.equals(getTile(r,c)) && selected.size() >=1)
      {
         selected.remove(selected.size()-1);
         selectedLetters.remove(selectedLetters.size()-1);
         if (selected.size() > 0)
            last = new Tile(selected.get(selected.size()-1));
      }
   }
   
   /**getSelectedTiles returns the arraylist of selected tiles
      @return selected list of selected tiles
   */
   public ArrayList<Tile> getSelectedTiles()
   {
      return selected;
   }
   
   /**clearSelected clears selected list of all tiles
   */
   public void clearSelected()
   {
      selected.clear();
      selectedLetters.clear();
   }
   
   /**testSelected tests to see if the selected words create a valid new word
   */
   public void testSelected()
   {
      word = new Word(selected);
      if (dictionary.isValidWord(word) && !(words.contains(word.getWord())))
      {
         words.add(word.getWord().toUpperCase());
         points += word.getPoints();
      }
      clearSelected();
      
         
   }
   
   /**toString returns the information for the game as a string
      @return string containing info on board, selected, words, and score
   */
   public String toString()
   {
      string = board.toString() + 
               "\nselected" + selectedLetters +
               "\nwords: " + words +
               "\nscore: " + points;
               
      
      return string;
   }
   
   /**getTile gets tile object based on coordinates from the board
      @return Tile object from board
   */
   public Tile getTile(int r, int c)
   {
      return board.getTile(r, c);
   }
   
   /**getWords returns completed words 
      @return words arraylist of strings
   */
   public ArrayList<String> getWords()
   {
      return words;
   }
   
   /**getPoints returns total points for the game
      @return points
   */
   public int getPoints()
   {
      return points;
   }
}