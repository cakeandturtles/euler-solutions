import java.util.Scanner;
import java.io.File;

public class prob11{
  static int[][] myGrid = new int[20][20];

  static int horizontal(int i,int j){
    return myGrid[i][j]*myGrid[i][j+1]*myGrid[i][j+2]*myGrid[i][j+3];
  }

  static int vertical(int i,int j){
    return myGrid[i][j]*myGrid[i+1][j]*myGrid[i+2][j]*myGrid[i+3][j];
  }
  
  static int diagonalRight(int i, int j){
    return myGrid[i][j]*myGrid[i+1][j+1]*myGrid[i+2][j+2]*myGrid[i+3][j+3];
  }

  static int diagonalLeft(int i, int j){
    return myGrid[i][j]*myGrid[i+1][j-1]*myGrid[i+2][j-2]*myGrid[i+3][j-3];
  }

  public static void main(String[] args) throws Exception
  {
	String fileName = "grid11.txt";
	File file = new File(fileName);
    Scanner s = new Scanner(file);
    int maxProd=0;

    for (int i=0; i<20; i++){ //Enter the input into the grid
      for (int j=0; j<20; j++){
        myGrid[i][j]=s.nextInt();
      }
    }

    for (int i=0; i<20; i++){ //search for the largest product
      for (int j=0; j<20; j++){
        if (j+4<20){
          if (horizontal(i,j)>maxProd){ maxProd = horizontal(i,j); }

          if (i+4<20){
            if (diagonalRight(i,j)>maxProd){ maxProd = diagonalRight(i,j); } } }

        if (i+4<20){
          if (vertical(i,j)>maxProd){ maxProd = vertical(i,j); } }

        if (i+4<20 && j-4>=0){
          if (diagonalLeft(i,j)>maxProd){ maxProd = diagonalLeft(i,j); } }
      }
    }
    System.out.println(maxProd);
  }
}
