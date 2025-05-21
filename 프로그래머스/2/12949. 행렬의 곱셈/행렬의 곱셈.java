import java.io.*;
import java.util.*;


class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        
        int[][] answer = new int[arr1.length][arr2[0].length];
        
        int a = 0;
        for(int i = 0; i<arr1.length; i++){
            for (int j =0; j<arr2[0].length; j++){
                for(int k = 0; k<arr1[0].length; k++){
                    a += arr1[i][k] * arr2[k][j];
                }
                answer[i][j] = a;
                a = 0;
            }
            
        }
        
        
        return answer;
    }
}