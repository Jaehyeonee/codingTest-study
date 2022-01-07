//정렬왕 2108번
// 최빈값 구하기는 아직 해결 x 

#include<stdio.h>
#include<stdlib.h>

//https://dojang.io/mod/page/view.php?id=638 퀵정렬 함수 사용을 위한 compare 함수 작성 법.

int num[500001] = { 0, };
int cnt[8001] = { 0, };	// 최빈값 세기 위한 배열

int compare(const void* a, const void* b) {
	if (*(int*)a > *(int*)b)
		return 1;
	else if (*(int*)a < *(int*)b)
		return -1;
	else
		return 0;

}

int maxnum(int* arr, int arr_size) {
	int max = arr[0];
	for (int i = 0; i < arr_size; i++)
		if (max < arr[i])
			max = arr[i];
	
	return max;
}

int main() {
	int N, sum = 0;
	
	int minrange = 4000;
	int maxrange = -4000;	// 절대값

	scanf_s("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf_s("%d", &num[i]);	// 산술평균 구하기 위한 합
		sum += num[i];
		

		if (minrange > num[i])
			minrange = num[i];

		if (maxrange < num[i])
			maxrange = num[i];

	}

	qsort(num, N, sizeof(int), compare);
	printf("중앙값: %d\n", num[(N + 1) / 2 - 1]);
	printf("산술평균: %.0f\n", (double)sum / N);
	printf("범위 : %d\n", maxrange - minrange);

}
