import java.io.File;
import java.util.Scanner;

public class prob22 {
	public static boolean compNames(String name1, String name2){
		//Returns true if name1 > name2 alphabettically
		int len = Math.max(name1.length(), name2.length());
		for (int i = 0; i < len; i++){
			if (name1.length() < i+1) return false;
			else if (name2.length() < i+1) return true;

			if (name1.charAt(i) > name2.charAt(i)) return true;
			else if (name1.charAt(i) < name2.charAt(i)) return false;
		}
		return false;
	}

	public static void sortNames(String[] names){
		int i, j;
		String key;

		for (j = 1; j < names.length; j++){
			key = names[j];
			for (i = j - 1; (i >= 0) && (compNames(names[i], key)); i--){
				names[i+1] = names[i];
			}
			names[i+1] = key;
		}
	}

	public static int scoreName(String name){
		int score = 0;
		for (int i = 0; i < name.length(); i++){
			int charScore = name.charAt(i);
			score += charScore - 64;
		}
		return score;
	}

	public static void main(String[] args) throws Exception{
		String filename = "names.txt";
		File file = new File(filename);
		Scanner s = new Scanner(file);
		String[] unfiltNames = s.nextLine().split(",");
		String[] names = new String[unfiltNames.length];

		//Fill the names array with the unsorted names
		for (int i = 0; i < names.length; i++){
			names[i] = unfiltNames[i].split("\"")[1];
		}
		sortNames(names);
		System.out.println("");
		int totalScore = 0;
		for (int i = 0; i < names.length; i++){
			System.out.println("Scoring names... " + names[i]);//i);
			totalScore += (i+1) * scoreName(names[i]);
		}
		System.out.println("Total Score: " + totalScore);
	}
}
