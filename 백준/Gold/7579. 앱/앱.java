import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); // 앱의 개수
        int M = sc.nextInt(); // 필요한 최소 메모리
        int[] memories = new int[N]; // 앱이 사용하는 메모리
        int[] costs = new int[N]; // 앱을 비활성화할 때의 비용

        for (int i = 0; i < N; i++) {
            memories[i] = sc.nextInt();
        }

        for (int i = 0; i < N; i++) {
            costs[i] = sc.nextInt();
        }

        int maxCost = 10000; // 문제의 조건에서 비용의 합의 최대가 10000
        int[] dp = new int[maxCost + 1]; // dp 배열 초기화

        // 동적 계획법으로 해결
        for (int i = 0; i < N; i++) {
            int memory = memories[i];
            int cost = costs[i];

            // 내림차순으로 비용을 처리하여 중복 업데이트 방지
            for (int j = maxCost; j >= cost; j--) {
                dp[j] = Math.max(dp[j], dp[j - cost] + memory);
            }
        }

        // 최소 비용을 찾기 위해 dp 배열을 순회
        int answer = Integer.MAX_VALUE;
        for (int i = 0; i <= maxCost; i++) {
            if (dp[i] >= M) {
                answer = i;
                break;
            }
        }

        System.out.println(answer);
        sc.close();
    }
}
