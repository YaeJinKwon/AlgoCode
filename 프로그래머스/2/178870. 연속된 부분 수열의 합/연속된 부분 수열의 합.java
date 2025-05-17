import java.io.*;
import java.util.*;

class Solution {

    public int[] solution(int[] sequence, int k) {


        ArrayList<int[]> ans = new ArrayList<>();
        int right = 0;
        int left = 0;
        int sum = sequence[0];
        
        while(right < sequence.length){
            if(sum == k){
                int last = right;
                int first = left;
                int d = last-first;
                ans.add(new int[]{first,last, d});
                sum-= sequence[left++];
            }else if(sum < k){
                right++;
                if(right < sequence.length){
                sum += sequence[right];
                }
            }else{
                sum -= sequence[left++];
            } 
        }
              
            ans.sort((a,b) -> {
                    if(a[2] == b[2]){
                        return a[0]-b[0];
                    }
                    return a[2]-b[2];
                    });
        
        int[] answer = {ans.get(0)[0],ans.get(0)[1]};
    
  
        
        return answer;
    }
}