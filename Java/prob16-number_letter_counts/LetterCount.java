public class LetterCount { 

	static String[] tens = {"ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"}; 
	static String[] hundreds = {"onehundred", "twohundred", "threehundred", "fourhundred", "fivehundred", "sixhundred", "sevenhundred", "eighthundred", "ninehundred"}; 

	public static void main(String[] args) {
		System.out.println(countOneThroughNinetyhundredninetunine() + "onethousand".length());
	}

	public static int countOneThroughNine() { 
		String[] nums = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}; 

		int count = 0; 

		for(String num : nums) { 
			count += num.length();
		}

		return count;
	}

	public static int countTenThroughNineteen() { 
		String[] nums = {"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"}; 

		int count = 0; 

		for(String num : nums) { 
			count += num.length();
		}

		return count;
	}

	public static int countOneThroughNinetynine() { 

		int count = 0; 

		count += countOneThroughNine();
		count += countTenThroughNineteen(); 

		// 20 -> 99
		for (int i = 1; i < tens.length; i++) { 
			count += (10 * tens[i].length()) + countOneThroughNine();
		}

		return count; 
	}

	public static int countOneThroughNinetyhundredninetunine() { 
		int count = 0; 

		count += countOneThroughNinetynine(); 

		// 100 => 999
		for (int i = 0; i < hundreds.length; i++) { 
			count += hundreds[i].length() + (99 * (hundreds[i].length() + "and".length())) + countOneThroughNinetynine();
		}

		return count; 
	}
}