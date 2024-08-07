
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;



public class Main {
		
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = null;
		int N = Integer.parseInt(br.readLine());
		
		st =  new StringTokenizer(br.readLine(), " "); // 거리
		int[] d = new int[N-1];
		for (int i = 0; i < N-1; i++) {
			d[i] = Integer.parseInt(st.nextToken());
		}
		
		st =  new StringTokenizer(br.readLine(), " ");// 가역
		int[] w = new int[N];
		for (int i = 0; i < N; i++) {
			w[i] = Integer.parseInt(st.nextToken());
		}

		//구현
		long ans = 0;
		long min = w[0];

		for (int i = 0; i < N-1; i++) {
				min = Math.min(min,w[i]);
				ans += min * d[i];
			}
		
		System.out.println(ans);
		br.close();
	}}
