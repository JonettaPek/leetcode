import java.util.List;
import java.util.ArrayList;

class FizzBuzz {
    static List<String> fizzBuzz(int n) {
        List<String> returnList = new ArrayList<>();
        for (int i = 1; i <= n; i++){
            if (i % 15 == 0) {
                returnList.add("FizzBuzz");
            } else if (i % 5 == 0) {
                returnList.add("Buzz");
            } else if (i % 3 == 0) {
                returnList.add("Fizz");
            } else {
                returnList.add(String.valueOf(i));
            }
        }
        return returnList;
    }

    public static void main(String[] args) {
        fizzBuzz(100).forEach(string -> System.out.println(string));
    }
}