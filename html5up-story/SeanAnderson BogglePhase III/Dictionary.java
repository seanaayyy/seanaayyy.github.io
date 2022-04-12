/**Dictionary class loads an array list of words from a dictionary file
Sean Anderson
CS110C
*/

import java.util.ArrayList;
import java.io.*;
import java.util.Scanner;


public class Dictionary
{

   //instance variables
   private ArrayList<String> dictionary;
   private boolean valid = false;
   private String word;
   
   /**Dictionary constructor takes a filename, reads the file, and creates and
      array list of String words
      @param filename the name of the dictionary file
   */
   public Dictionary(String filename) throws IOException
   {
      //open file
      File file = new File(filename);
      Scanner inputFile = new Scanner(file);
      
      //create an array of strings to store dictionary in
      dictionary = new ArrayList<String>();
            
      int lineNum = 1;
      String line = "";
      
      //copy words to ArrayList from file
      do
      {
         line = inputFile.nextLine();
         dictionary.add(line);
         lineNum++;
      } while(inputFile.hasNext());
      inputFile.close(); 
   }
   
   /**getDictionary returns the dictionary
      @return dictionary the arraylist of words
   */
   public ArrayList<String> getDictionary()
   {
      return dictionary;
   }
   
   /**isValidWord checks if a word is in the dictionary
      @param tileList a list of tiles to be converted to a word
      @return valid if the word is in the dictionary
   */
   public boolean isValidWord(ArrayList<Tile> tileList)
   {
      word = "";
      valid = false;
      for (Tile tile : tileList)
      {
         if (tile.getLetter() == 'q')
           word = word + "qu";
         else
            word = word + tile.getLetter();
      }
      for (String dictWord : dictionary)
      {
         if (dictWord.equals(word))
            valid = true;
      }
      if (word.length() <= 2)
         valid = false;
      return valid;
   }
   
   /**isValidWord overloads other method, but accepts a word object instead
      @param word to be compared with dictionary
      @return valid if word is valid
   */
   public boolean isValidWord(Word wordObj)
   {
      valid = false;
      for (String dictWord : dictionary)
      {
         if (dictWord.equalsIgnoreCase(wordObj.getWord()))
            valid = true;
      }
      if (wordObj.getWord().length() <= 2)
         valid = false;
      return valid;
   }
      


}