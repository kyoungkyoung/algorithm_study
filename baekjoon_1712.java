import java.util.Scanner;
 
public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
 
 
		int fixedCost = scanner.nextInt();
        int variableCost = scanner.nextInt();
        int price = scanner.nextInt();

        if(variableCost >= price) {
            System.out.println(-1);
        }else {
            System.out.println((fixedCost/(price-variableCost))+1);
        }
	}
}