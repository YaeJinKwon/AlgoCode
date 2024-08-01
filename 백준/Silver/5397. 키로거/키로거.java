import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.LinkedList;


public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());



		ArrayDeque<Character> cL;
		ArrayDeque<Character> cR;
		StringBuilder sb;
		for (int i = 0; i < N; i++) {
			cL = new ArrayDeque<>();
			cR = new ArrayDeque<>();
			String Insert = br.readLine();
			for (int j = 0; j < Insert.length(); j++) {
				switch (Insert.charAt(j)) {
					case '<':
						if(cL.isEmpty()) continue;
						cR.offer(cL.pollLast());
						break;
					case '>':
						if(cR.isEmpty()) { continue;}
						cL.offer(cR.pollLast()); break;
					case '-':
						if(!cL.isEmpty()) cL.pollLast();
						break;
                    default:
                       cL.offer(Insert.charAt(j));
                }
			}
			sb = new StringBuilder();
			while(!cL.isEmpty()) {
				sb.append(cL.poll());
			}
			while(!cR.isEmpty()) {
				sb.append(cR.pollLast());
			}
			System.out.println(sb);
		}
	}
}
