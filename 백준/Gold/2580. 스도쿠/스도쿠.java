

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
	static int[][] sd= new int[9][9];	

	static void Sdk(int i, int j) {
		if (i == 9) {
            printSolution();
            System.exit(0); // 결과를 찾으면 프로그램 종료
        }
		if(sd[i][j] == 0) {
			boolean[] num = new boolean[10];
			for (int a = 0; a < 9; a++) {
				if(sd[i][a] != 0) num[sd[i][a]] = true;
			}
			
			for (int a = 0; a < 9; a++) {
				if(sd[a][j] != 0) num[sd[a][j]] = true;
			}
			
			int i_r = (i/3) * 3;
			int j_r = (j/3) * 3;
			
			for (int a = i_r; a < i_r + 3; a++) {
				for (int b = j_r; b < j_r +3; b++) {
					 if (sd[a][b] != 0) {
						 num[sd[a][b]] = true;}
				}
			}

			
			for (int a = 1; a <= 9; a++) {
				 if (!num[a]) {
					 sd[i][j] = a;
					 if (j == 8) {
	                        Sdk(i + 1, 0);
	                    } else {
	                        Sdk(i, j + 1);
	                    }
	                    sd[i][j] = 0; // 백트래킹
	                }
				 }
			}else {
				if (j == 8) {
		            Sdk(i + 1, 0);
		        } else {
		            Sdk(i, j + 1);
		        }
			}

	}
	
    static void printSolution() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                sb.append(sd[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.print(sb);
    }

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		for (int i = 0; i < 9; i++) {
			st = new StringTokenizer(br.readLine()," ");
			for (int j = 0; j < 9; j++) {
				sd[i][j] = Integer.parseInt(st.nextToken());
				}
			}
		Sdk(0,0);
			
	
	}

}