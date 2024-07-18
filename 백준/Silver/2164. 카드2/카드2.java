import java.io.BufferedReader;

import java.io.InputStreamReader;
import java.util.ArrayDeque;


public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			int N = Integer.parseInt(br.readLine());
			ArrayDeque<Integer> card = new ArrayDeque<>();
			
			for (int i = 1; i < N+1; i++) {
				card.offer(i);	
			}
			while(card.size() != 1) {
				card.pop();
				card.offerLast(card.pop());;
			}
			
			
			System.out.println(card.peek());
	}
}
