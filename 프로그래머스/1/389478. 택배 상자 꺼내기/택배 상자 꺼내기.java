import java.io.*;
import java.util.*;


class Solution {
    public int solution(int n, int w, int num) {
        int answer = 0;
        int numH = num/w;
        if(num % w != 0){
            numH++;
        }
        
        int H = n/w;
        if(n%w !=0){
            H++;
        }
        
        int cur = num;
        for(int i = 0; i<H; i++){
            int numL = cur % w;
            if(cur > n){
                  break;
            }
            answer++;
            if(numL == 0){
                cur += 1;
            }else{
                cur += (w - numL)*2 + 1;
            }


        }
        
        return answer;
    }
}