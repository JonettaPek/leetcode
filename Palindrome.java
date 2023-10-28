class Palindrome {
    static boolean isPalindrome(int x) {
        String string = String.valueOf(x);
        StringBuilder sb = new StringBuilder(string);
        StringBuilder reverseSb = sb.reverse();
        if (string.equals(reverseSb.toString())) {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println(isPalindrome(123454321));
    }
}