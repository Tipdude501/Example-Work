import java.util.Scanner;
import java.util.Random;


public class AreaOrCircumference {
	public static void main(String[] args) {

	// definitions	
	double radius;
	double area;
	double circumference;
	int calculation;
	String string1 = "R";
	String string2;
	Random out1 = new Random();


	// request radius
	System.out.println("Enter radius: ");
	System.out.println("(or type 'R' to generate random)");
	Scanner in1 = new Scanner(System.in);

	// assign radius
	if(in1.hasNextDouble()) {
		radius = in1.nextDouble();
		System.out.println();
	}
	else {
		string2 = in1.nextLine();
		if(string1.equals(string2)) {
			radius = out1.nextInt(101);
			System.out.println();
			System.out.println("radius = " + radius);
		}
		else {
			System.out.println("Invalid entry");
			return;
		}
	}
	

	// choose calculation
	System.out.println("What would you like to calculate?");
	System.out.println("To find area, type '1'");
	System.out.println("To find circumference, type '2'");
	calculation = in1.nextInt();


	// execute calculation
	if(calculation == 1) {
		area = radius * radius * 3.14159;
		System.out.println();
		System.out.println("Area for circle with radius " + radius + " = " + area);
		System.out.println();
	}
	else {
		if (calculation == 2) {
			circumference = radius * 2 * 3.14159;
			System.out.println();
			System.out.println("Circumference for circle with radius " + radius + " = " + circumference);
			System.out.println();
		}
	}


	}// end main method
}// end class AreaOrCircumference