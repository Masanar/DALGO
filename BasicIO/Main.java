import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {

    public static int f(int case0, int case1, int number) {
        if (number == 0) {
            return case1;
        } else {
            return f(case1, case0 + case1, number - 1);
        }
    }

    public static void main(String[] args) {
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(System.in))) {
            String nLine;
            while ((nLine = reader.readLine()) != null && !nLine.trim().isEmpty()) {
                int n = Integer.parseInt(nLine.trim());
                String[] cases = reader.readLine().trim().split(" ");
                int x = Integer.parseInt(cases[0]);
                int y = Integer.parseInt(cases[1]);
                System.out.println(f(x, y, n));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
