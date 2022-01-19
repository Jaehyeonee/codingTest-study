// 정렬왕 2309번 문제
// 9명중 2명 빼야 함.

#include<stdio.h>


int main() {

	int height[9] = { 0, };
	int sum=0;
	int no[2] = { 0, }; //뺄 2명
	int temp;

	for (int i = 0; i < 9; i++) {
		scanf_s("%d", &height[i]);

		if (height[i] > 100) {
			break;
		}

		else
			sum += height[i];

	}

	
	for (int i = 0; i < 8; i++) {
		for (int j = i+1; j < 9; j++) {
			if (i != j && sum - height[i] - height[j] == 100) {
			
				no[0] = height[i];
				no[1] = height[j];
				

			}
		}
		
	}
//선택정렬
	for (int i = 0; i < 8; i++) { 
		for (int j = i + 1; j < 9; j++) {

			if (height[i] > height[j]) {
				temp= height[i] ;
				height[i] = height[j];
				height[j] = temp;
			}
		}
	}

	

	


	for (int i = 0; i <=8; i++) {

		if (no[0] != height[i] && no[1] != height[i]) {

			printf("%d\n", height[i]);
		}
			

	}
		

			
}
