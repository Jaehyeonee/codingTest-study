//정렬왕 11399번

#include<stdio.h>

int main() {
	int N;
	int pi[10001];
	int sum = 0;
	int ans = 0;
	int i, j, temp;

	scanf_s("%d", &N);
	for (i = 0; i < N; i++) {
		scanf_s("%d", &pi[i]);
	}

	//선택정렬//

	for (i = 0; i < N-1; i++) {
		for (j = i; j < N; j++) {

			if (pi[i] > pi[j]) {
				temp = pi[i];

				pi[i] = pi[j];
				pi[j] = temp;

			}
			

		}
	}

	

	for (i = 0; i < N; i++) {
		
		sum += pi[i];        
		ans += sum;         //누적
	
	}

	printf("%d", ans);

}
