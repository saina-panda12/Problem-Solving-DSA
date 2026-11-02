import java.util.*;

public class Main {

    static int f(int n) {
        // Base cases
        if (n <= 1) {
            return n;
        }

        // Recursive call
        return f(n - 1) + f(n - 2);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int result = f(n);

        System.out.println(result);

        sc.close();
    }
}