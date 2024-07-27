import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayDeque;


public class Main {
	
//string builder 써도 됨
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


		ArrayDeque<Character> cL = new ArrayDeque<>();
		ArrayDeque<Character> cR = new ArrayDeque<>();
		
		String cL_first = br.readLine();
		for (int i = 0; i < cL_first.length(); i++) {
			cL.offer(cL_first.charAt(i));
		}
		int N = Integer.parseInt(br.readLine());

		for (int i = 0; i < N; i++) {
			String st = br.readLine();
			switch(st.charAt(0)) {
			case 'L':
				if(!cL.isEmpty()) {
					char c1 = cL.pollLast();
					cR.offerFirst(c1);} // 의문.
				break;
			case 'D':
				if(!cR.isEmpty()) {
					char c2 = cR.poll(); 
					cL.offer(c2);
}
				break;
			case 'B':
				if(!cL.isEmpty()) cL.pollLast();

				break;
			case 'P':
				cL.offer(st.charAt(2));

				break;

			}	
		} 

		StringBuilder sb = new StringBuilder();
		while(!cL.isEmpty()) {
			sb.append(cL.poll());
		}
		while(!cR.isEmpty()) {
			sb.append(cR.poll());
		}
		System.out.println(sb);
		br.close();

	}}