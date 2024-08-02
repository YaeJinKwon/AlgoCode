import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int N, C;
	static int[] node;
	static ArrayList<Integer>[] ans;


	static void Node(int n, int f , int e){
		int mid = (e + f)/2;
		if(f>e) {
			return;}
		ans[n].add(node[mid]);
		Node(n+1, f , mid-1);
		Node(n+1, mid+1 , e);
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		
		N = Integer.parseInt(br.readLine());
		C = (int) Math.pow(2,N) - 1;
		node = new int[C];
		st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < C; i++) {
			node[i] = Integer.parseInt(st.nextToken());
		}
		ans = new ArrayList[N];
		for (int i = 0; i < N; i++) {
			ans[i] = new ArrayList<>();
		}
		Node(0,0,C-1);

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < N; i++) {
			for(int j = 0; j < ans[i].size(); j++){
				sb.append(ans[i].get(j) + " ");
			}
			sb.append("\n");
		}
		System.out.println(sb);

	}
}
