import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


public class prob67 {
	/*#####Thinking to myself...############################################################
	#Actual solution::!
	#0. Make an array of length n, and set it to the bottom row of the triangle
	#1. Create a new array with a length one less than the existing array
	#2. Set array equal to the triangle row of equal length
	#3. For each index, sum the number with the largest possible connecting number in the existing array
	#4. Replace the current array with this new array
	#5. Repeat steps 1 through 4 until the length of the array is 1
	#6. The value of this array will be the max path sum
	###################################################################################*/
	public static void printTriangle(int[][] triangle){
		for (int i = 0; i < triangle.length; i++){
			for (int j = 0; j < triangle[i].length; j++){
				System.out.print(triangle[i][j]+ ", ");
			}
			System.out.print("\n");
		}
	}
	
	public static int maxSumPath(int[][] triangle){
		//printTriangle(triangle);
		int[] temp = triangle[triangle.length-1];
		while (temp.length > 1){
			int[] temp2 = triangle[temp.length-2];
			for (int i = 0; i < temp2.length; i++){
				int pot1 = temp[i];
				int pot2 = temp[i+1];
				if (pot1 > pot2)
					temp2[i] += pot1;
				else
					temp2[i] += pot2;
			}
			temp = temp2;
		}
		return temp[0];
	}
	
	public static void main(String[] args){
		int[][] triangle = new int[100][];
		String filename = "triangle.txt";
		File file = new File(filename);
		Scanner s;
		try {
			s = new Scanner(file);
		
			for (int i = 0; i < 100; i++){
				String[] line = s.nextLine().split(" ");
				triangle[i] = new int[line.length];
				for (int j = 0; j < line.length; j++){
					triangle[i][j] = Integer.parseInt(line[j]);
				}
			}
			s.close();
			System.out.println("Sum: " + maxSumPath(triangle));
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}	
	}
}
	