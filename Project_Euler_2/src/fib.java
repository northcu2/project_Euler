public class fib {
	public static void main(String[] args) {
		int a = 1;
		// Declaring variable integer a
		int b = 1;
		// Declaring variable integer b
		int c = 0;
		// Declaring variable integer c
		int evenTerm = 0;
		// Declaring variable integer evenTerm
		while( b < 4000000){ 
		// Start While loop, problem constraints are that the largest prime factor must be under 4,000,000.
			c = a+b;
			// Start the sequence.
				if (c%2 == 0) {
					evenTerm = evenTerm + c;
					//If c is even, then add it to evenTerm.
				}
			a = b+c;
			    if (a%2 == 0) {
			    	evenTerm = evenTerm + a;
			    	//If a is even, then add it to evenTerm.
	        }
			b = c+a;
			    if (b%2 == 0) {
			    	evenTerm = evenTerm + b;
			    	//If b is even, then add it to evenTerm.
	        }
		}
	System.out.println(evenTerm);
		//Prints the sum of all the even terms of the sequence under 4,000,000.
	}
	

}
