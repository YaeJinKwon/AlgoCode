class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {};
        for(int i = 1; i<=yellow; i++){
            if(yellow%i == 0){
                int h= yellow/i;
                int size = (h+2)*(i+2) - yellow;
                if(brown == size){
                    if(h+2 >= i+2){
                        answer = new int[]{h+2, i+2};
                        break;
                    }
                }
            }
        }
        return answer;
    }
}