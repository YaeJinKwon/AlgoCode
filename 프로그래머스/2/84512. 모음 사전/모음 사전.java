import java.util.*;
class Solution {
    char[] alpha;

    int c = 0;
    int ans = 0;
    public void find(int cnt, String w, String word){
        if(w.equals(word)){
            ans = c;
            return;
        }
        if(cnt==5){
            return;
        }
        for(int i = 0; i<5; i++){
            c++;
            find(cnt+1,w+alpha[i],word);
        }
        
        
    }
    public int solution(String word) {
        alpha = new char[]{'A','E','I','O','U'};
        
        find(0,"",word);
        return ans;
    }
}