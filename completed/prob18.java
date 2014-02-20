
public class prob18 {
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
		int[][] triangle = {
				{75},
				{95, 64},
				{17, 47, 82},
				{18, 35, 87, 10},
				{20, 4, 82, 47, 65},
				{19, 1, 23, 75, 3, 34},
				{88, 2, 77, 73, 7, 63, 67},
				{99, 65, 4, 28, 6, 16, 70, 92},
				{41, 41, 26, 56, 83, 40, 80, 70, 33},
				{41, 48, 72, 33, 47, 32, 37, 16, 94, 29},
				{53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14},
				{70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57},
				{91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48},
				{63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31},
				{4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23}
		};
		System.out.println("Sum: " + maxSumPath(triangle));
	}
}
