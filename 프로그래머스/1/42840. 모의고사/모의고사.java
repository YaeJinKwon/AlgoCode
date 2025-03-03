import java.io.*;
import java.util.*;


class Solution {
    public ArrayList<Integer> solution(int[] answers) {
        int[] one = {1, 2, 3, 4, 5};
        int[] two = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] three = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int num1 = 0;
        int num2 = 0;
        int num3 = 0;
        
        for(int i = 0; i<answers.length; i++){
            if(one[i%one.length] == answers[i]){
                num1++;
            }
            if(two[i%two.length] == answers[i]){
                num2++;
            }
            if(three[i%three.length] == answers[i]){
                num3++;
            }
        }
        
        
        int max = Math.max(Math.max(num1, num2), num3);
        
        ArrayList<Integer> answer = new ArrayList<>();
        if(max == num1){
            answer.add(1);
        }
        if(max == num2){
            answer.add(2);
        }
        if(max == num3){
           answer.add(3);
        }
            
        return answer;
    }
}