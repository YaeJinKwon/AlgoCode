
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;



public class Main{
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer sw = null;
	
		int N = Integer.parseInt(br.readLine());
		int[][] ans = new int[N][2];
		
		
		for (int i = 0; i < N; i++) {
			sw = new StringTokenizer(br.readLine(), " ");
			ans[i][0] = Integer.parseInt(sw.nextToken());
			ans[i][1] = Integer.parseInt(sw.nextToken());
			}
		
		Arrays.sort(ans,(o1,o2)-> o1[0] == o2[0] ? Integer.compare(o1[1], o2[1]): Integer.compare(o1[0], o2[0]));
		PriorityQueue<Integer> pq = new PriorityQueue<>((o1,o2)-> Integer.compare(o1, o2));
		
		pq.offer(ans[0][1]);
		for (int i = 1; i < N; i++) {
			if(pq.peek() <= ans[i][0]) pq.poll();
			pq.offer(ans[i][1]);
			
		}
		System.out.println(pq.size());
		br.close();
		
	}
}
