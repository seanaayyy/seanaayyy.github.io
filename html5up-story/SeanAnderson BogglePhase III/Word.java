/*Word class represents a word that was entered by a player and stores the characters
in the word and points the word is worth
Sean Anderson
CS110C
*/

import java.util.ArrayList;

public class Word
{
   //instance variables
   private String word;
   private int points;
   private boolean compare;
   
   /**This constructor takes an array list of tiles and makes it into a word
      @param tileList the array list of tiles to be read through
   */
   public Word(ArrayList<Tile> tileList) 
   {
      points = 0;
      word = "";
      for (Tile tile : tileList)
      {
         if (tile.getLetter() == 'Q')
         {
           word = word + "Qu";
         } 
         else
         {
            word = word + tile.getLetter();
         }
      }
      
      //adjust points based on word length
      if (word.length() == 3 || word.length() == 4)
         points = 1;
      else if (word.length() == 5)
         points = 2;
      else if (word.length() == 6)
         points = 3;
      else if (word.length() == 7)
         points = 5;
      else if (word.length() >= 8)
         points = 11;
      else
         points = 0;
   
   }
   
   /**getWord returns the word made from the tiles
      @return word the word created
   */
   public String getWord()
   {
      return word;
   }
   
   /**getPoints returns the points made from a word
      @return points the amount of points
   */
   public int getPoints()
   {
      return points;
   }
   
   /**toString method provides the word as a string
      @return word the word created
   */
   public String toString()
   {
      return word;
   }
   
   /**equals method compares two instances of the word class
      @param otherWord a word to compare to 
      @return compare whether the words are identical
   */
   public boolean equals(Word otherWord)
   {
      //there are equals methods in both class Word and Tile
      //equals in word checks if words have same address and
      //if the words spell the same thing
      if (otherWord == null || word == null)
         compare = false;
      else if (otherWord.getWord() == word)
         compare = true;
      else if (otherWord.getWord().equals(word))
         compare = true;
      else
         compare = false;
      return compare;
   
   }
   
}