import java.util.*;

public class codes {

    public static int countPossibleHouses(int s0, int n, int k, int b, int m, int a) {
        List<Integer> sideLengths = generateSideLengths(s0, n, k, b, m);
        Set<String> uniqueConfigurations = new HashSet<>();

        for (int i = 0; i < sideLengths.size(); i++) {
            for (int j = 0; j < sideLengths.size(); j++) {
                int length = sideLengths.get(i);
                int width = sideLengths.get(j);
                if (length * width <= a) {
                    int[] sortedSides = new int[]{length, width};
                    Arrays.sort(sortedSides);
                    uniqueConfigurations.add(sortedSides[0] + "," + sortedSides[1]);
                }
            }
        }

        return uniqueConfigurations.size();
    }

    private static List<Integer> generateSideLengths(int s0, int n, int k, int b, int m) {
        List<Integer> sideLengths = new ArrayList<>();
        sideLengths.add(s0);

        for (int i = 1; i < n; i++) {
            int previous = sideLengths.get(i - 1);
            int next = ((k * previous + b) % m) + 1 + previous;
            sideLengths.add(next);
        }

        return sideLengths;
    }

    public static void main(String[] args) {
        int s0 = 2;
        int n = 3;
        int k = 3;
        int b = 3;
        int m = 2;
        int a = 15;

        int result = countPossibleHouses(s0, n, k, b, m, a);
        System.out.println("Number of possible house configurations: " + result); // Expected output: 4
    }
}
