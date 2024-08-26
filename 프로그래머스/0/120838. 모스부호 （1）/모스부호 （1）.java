import java.util.*;
import java.io.*;
class Solution {
    public String solution(String letter) {
                StringTokenizer st = new StringTokenizer(letter, " ");
        Map<String, Character> morse = new HashMap<>();
        String[] morse1 = new String[]{".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."};
        for (int i = 0; i < morse1.length; i++) {
            morse.put(morse1[i], (char) (97+i));
        }
        StringBuilder sb = new StringBuilder();
        while(st.hasMoreTokens()){
            sb.append(morse.get(st.nextToken()));
        }
    
        return sb.toString();
    }
}