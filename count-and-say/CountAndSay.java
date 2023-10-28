/**
 * Problem Description:
 *     To determine how you "say" a digit string, 
 *     split it into the minimal number of substrings such that each substring contains exactly one unique digit. 
 *     Then for each substring, say the number of digits, then say the digit. 
 *     Finally, concatenate every said digit.
 */

class countAndSay {

    public String countAndSay(int n) {
        if (n == 1) {
            return "1";
        }

        if (n == 2) {
            return "11";
        }

        String returnString = "11";
        for (int i = 2; i < n; i++) {
            StringBuilder temp = new StringBuilder("");
            char previousCharacter = returnString.charAt(0);
            int occurrence = 1;
            for (int j = 1; j < returnString.length(); j++) {
                if (previousCharacter != returnString.charAt(j)) {
                    temp.append(occurrence).append(previousCharacter);
                    previousCharacter = returnString.charAt(j);
                    occurrence = 0;
                }
                occurrence++;
            }
            returnString =  temp.append(occurrence).append(previousCharacter).toString();
        }
        return returnString;
    }
}