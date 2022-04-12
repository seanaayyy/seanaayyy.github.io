/**Board class randomly assigns dice and letters for each square of the board
Sean Anderson
CS110C
*/

import java.util.ArrayList;
import java.util.Random;

public class Board
{
   private Tile tile;//for return in getTile method
   //set 16 dice as constant lists
   
   private final String DIE0 = "RIFOBX"; 
   private final String DIE1 = "IFEHEY"; 
   private final String DIE2 = "DENOWS"; 
   private final String DIE3 = "UTOKND"; 
   private final String DIE4 = "HMSRAO"; 
   private final String DIE5 = "LUPETS"; 
   private final String DIE6 = "ACITOA"; 
   private final String DIE7 = "YLGKUE"; 
   private final String DIE8 = "QBMJOA"; //u taken out, will display and coint points for qu
   private final String DIE9 = "EHISPN"; 
   private final String DIE10 = "VETIGN"; 
   private final String DIE11 = "BALIYT"; 
   private final String DIE12 = "EZAVND"; 
   private final String DIE13 = "RALESC"; 
   private final String DIE14 = "UWILRG"; 
   private final String DIE15 = "PACEMD"; 
   
   //instance variables for the array lists of rows and the board itself
   private ArrayList<ArrayList<Tile>> boardTiles;
   private ArrayList<Tile> row0;
   private ArrayList<Tile> row1;
   private ArrayList<Tile> row2;
   private ArrayList<Tile> row3;
   //instance variable used in toString method
   private String board;
   
   /**Board constructor creates a list of dice and randomly assigns dice
      and sides up for each row and column of the board
   */
   public Board()
   {
      //add all dice into an arraylist
      ArrayList<String> diceList = new ArrayList<String>();
      diceList.add(DIE0);
      diceList.add(DIE1);
      diceList.add(DIE2);
      diceList.add(DIE3);
      diceList.add(DIE4);
      diceList.add(DIE5);
      diceList.add(DIE6);
      diceList.add(DIE7);
      diceList.add(DIE8);
      diceList.add(DIE9);
      diceList.add(DIE10);
      diceList.add(DIE11);
      diceList.add(DIE12);
      diceList.add(DIE13);
      diceList.add(DIE14);
      diceList.add(DIE15);
      
      boardTiles = new ArrayList<>();
      Random rand = new Random();
      
      //set dice and letters for the first row randomly
      row0 = new ArrayList<Tile>();
      char letter;
      int column; //= 0;
      //do
      for (column = 0; column <=3; column++)
      {
         int chooseDie = rand.nextInt(diceList.size());
         String die = diceList.get(chooseDie);
      
         int chooseSide = rand.nextInt(6);
         letter = die.charAt(chooseSide);
         
         diceList.remove(chooseDie);
         row0.add(new Tile(letter, 0, column));
         //column++;
         
         
      } //while (column < 4);
      
      boardTiles.add(row0);
      
      //set second row
      row1 = new ArrayList<>();
       column = 0;
      //do
      for (column = 0; column <=3; column++)
      {
         int chooseDie = rand.nextInt(diceList.size());
         String die = diceList.get(chooseDie);
      
         int chooseSide = rand.nextInt(6);
         letter = die.charAt(chooseSide);
         
         diceList.remove(chooseDie);
         row1.add(new Tile(letter, 1, column));
         //column++;
         
         
      } //while (row1.size() < 4);
      
      boardTiles.add(row1);
      
      //set third row
      row2 = new ArrayList<>();
       column = 0;
      //do
      for (column = 0; column <=3; column++)
      {
         int chooseDie = rand.nextInt(diceList.size());
         String die = diceList.get(chooseDie);
      
         int chooseSide = rand.nextInt(6);
         letter = die.charAt(chooseSide);
         
         diceList.remove(chooseDie);
         row2.add(new Tile(letter, 2, column));
         //column++;
         
         
      } //while (row2.size() < 4);
      
      boardTiles.add(row2);
      
      //set final row
      row3 = new ArrayList<>();
       column = 0;
      //do
      for (column = 0; column <=3; column++)
      {
         int chooseDie = rand.nextInt(diceList.size());
         String die = diceList.get(chooseDie);
      
         int chooseSide = rand.nextInt(6);
         letter = die.charAt(chooseSide);
         
         diceList.remove(chooseDie);
         row3.add(new Tile(letter, 0, column));
         //column++;
         
         
      } //while (row3.size() < 4);
      
      boardTiles.add(row3);
   }
   
   /**toString method shows the letters on the board in their locations
      as a string
      @return board the 4x4 board of letters
   */
   public String toString()
   {
      board = "";
      for (Tile tile : row0)
      {
         if (tile.getLetter() == 'Q')
            board = board + tile.getLetter() + "u" + "\t";
         else
            board = board + tile.getLetter() + "\t";
      }
      board = board + "\n";
      
      for (Tile tile : row1)
      {
         if (tile.getLetter() == 'Q')
            board = board + tile.getLetter() + "u" + "\t";
         else
            board = board + tile.getLetter() + "\t";
      }
      board = board + "\n";
      
      for (Tile tile : row2)
      {
         if (tile.getLetter() == 'Q')
            board = board + tile.getLetter() + "u" + "\t";
         else
            board = board + tile.getLetter() + "\t";
      }
      board = board + "\n";
      
      for (Tile tile : row3)
      {
         if (tile.getLetter() == 'Q')
            board = board + tile.getLetter() + "u" + "\t";
         else
            board = board + tile.getLetter() + "\t";
      }
      board = board + "\n";
      
      return board;
   }
   
   /**getTile returns a tile based on its position
      @param row position
      @param column position
      @return Tile with the correct row and column
   */
   public Tile getTile(int row, int col)
   {
      if (row == 0)
         tile = new Tile( row0.get(col));
      else if (row == 1)
         tile = new Tile ( row1.get(col));
      else if (row == 2)
         tile = new Tile( row2.get(col));
      else if (row == 3)
         tile = new Tile( row3.get(col));
      return tile;
   }
   
}