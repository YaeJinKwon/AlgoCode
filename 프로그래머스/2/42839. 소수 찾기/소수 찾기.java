import java.util.*;

class Solution {
    int answer;
    char[] nums;
    boolean[] v;
    HashSet<Integer> all; 
    
    public void find(int cnt, String str){
        if(cnt>=nums.length){
            if(str != ""){
                all.add(Integer.parseInt(str));                
            }            
            return;
        }
        for(int i = 0; i<nums.length; i++){
            if(v[i]){
                continue;
            }
            v[i] = true;
            find(cnt+1, str+nums[i]);
            find(cnt+1, str);
            v[i] = false;
        }
    }
    public boolean isPrime(int n){
        if(n<2){
            return false;
        }
        
        for(int i = 2; i<n; i++){
            if(n%i == 0){
                return false;
            }
        }
        return true;
        
    }
    
    public int solution(String numbers) {
        answer = 0;
        nums = new char[numbers.length()];
        all = new HashSet<>();
        for(int i = 0; i< numbers.length(); i++){
            nums[i] = numbers.charAt(i);
        }
        v = new boolean[nums.length];
        find(0,"");
        
        Iterator<Integer> iter = all.iterator();
        while(iter.hasNext()){
            if(isPrime(iter.next())){
                answer++;
            }
        }
       

        
        
        return answer;
    }
}