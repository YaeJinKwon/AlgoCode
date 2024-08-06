import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.PriorityQueue;


public class Main{


	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		PriorityQueue<Integer> pq = new PriorityQueue<>();

		int N = Integer.parseInt(br.readLine());
		for (int i = 0; i < N; i++) {
			pq.add(Integer.parseInt(br.readLine()));
		}
		int ans = 0;

		if (N == 1) ans = 0;
		else{
			while(pq.size() != 2){
				int count = 0;
				count = pq.poll();
				count += pq.poll();
				ans += count;
				pq.add(count);
			}
			ans+= pq.poll() + pq.poll();
		}


		System.out.println(ans);
		br.close();
	}
	}

			
