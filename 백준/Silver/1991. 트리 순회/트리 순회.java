
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;



public class Main {
	static String[][] node;
	static int N;
	static StringBuilder sb = new StringBuilder();
	
	
	static void preOrder(String C) {
		if(C.equals(".")) {
			return;
		}
		for (int i = 0; i < N; i++) {
			if(node[i][0].equals(C)){
				sb.append(C);
				preOrder(node[i][1]);
				preOrder(node[i][2]);
				return;
			}
		}
	}
	
	static void inOrder(String C) {
		if(C.equals(".")) {
			return;
		}
		for (int i = 0; i < N; i++) {
			if(node[i][0].equals(C)){
				inOrder(node[i][1]);
				sb.append(C);
				inOrder(node[i][2]);
				return;
			}
		}
	}
	static void postOrder(String C) {
		if(C.equals(".")) {
			return;
		}
		for (int i = 0; i < N; i++) {
			if(node[i][0].equals(C)){
				postOrder(node[i][1]);
				postOrder(node[i][2]);
				sb.append(C);
				return;
			}
		}
	}
	
	
		
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		
		N = Integer.parseInt(br.readLine());
		node = new String[N][3];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			node[i][0] = st.nextToken();
			node[i][1] = st.nextToken();
			node[i][2] = st.nextToken();
		}

		preOrder(node[0][0]);
		sb.append("\n");
		inOrder(node[0][0]);
		sb.append("\n");
		postOrder(node[0][0]);
		System.out.println(sb);
		
		br.close();
		}

	
	}