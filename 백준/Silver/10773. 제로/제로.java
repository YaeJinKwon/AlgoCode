
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;


public class Main{
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			int K = Integer.parseInt(br.readLine());
			ArrayDeque<Integer> stack = new ArrayDeque<>();
			
			for (int i = 0; i < K; i++) {
				int N = Integer.parseInt(br.readLine());
				if(N == 0) {
					stack.pop();	
				}
				else{
					stack.push(N);	
				}
			}
			
			int sum = 0;
			
			while(stack.isEmpty() != true){
				sum += stack.pop();
			}
			
			System.out.println(sum);
	}
}