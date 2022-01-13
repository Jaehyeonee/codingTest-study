#include <stdio.h>
#include <stdlib.h>

// 문제 설명: M의 요소가 N에 있는 요소들 중 해당 수가 있는가? 
// 참고 문헌: https://daydreamx.tistory.com/entry/baekjoon1920 
// 교훈: 이진 탐색 사용할 때는 배열을 정렬 후 사용하는 것 추천 
// 요약: n 배열 오름차순 정렬 후 m 배열에 있는지 qsort로 확인

// 오름차순 비교 함수 
int compare(const void *a, const void *b)
{
    return *(int*)a > *(int*)b ? 1 : (*(int*)a < *(int*)b ? -1 : 0);
}

// 이진 탐색: 정령된 리스트에서 사용하면 좋음, 시간복잡도가 O(log2n)
int binary_search(int arr[], int num, int size)
{
    int front, rear, pivot;
    front = 0;
    rear = size - 1;
    while (1) {
    	// return 1 사용: 찾는 숫자가 배열에 존재 
        pivot = (front + rear) / 2;
        if (arr[pivot] == num) return 1;
        if (arr[front] == num) return 1;
        if (arr[rear] == num) return 1;

        if (arr[pivot] < num)
            front = pivot + 1;
        else 
            rear = pivot - 1;
        if (front >= rear)
            return 0;     // return 0: 찾는 숫자가 배열에 존재하지 않음   
				          // 평소에: return 0은 정상적으로 종료 의미 (운영체제로 값 반환) 
    }
}

int main(void){
    int n, m, i, j;
    scanf("%d", &n);             // N 입력 받기 
    int *arr = (int*)malloc(n * sizeof(int));   // N 개의 수 입력 받을 배열 포인터 

    for(i = 0; i < n; i++){
        scanf("%d", &arr[i]);    // N 개의 수 입력 받기 
    }
    
    scanf("%d", &m);             // M 입력 받기 
    int *arr2 = (int*)malloc(m * sizeof(int));   // M 개의 수 입력 받을 배열 포인터 

    for(i = 0; i < m; i++){     // M 개의 수 입력 받기 
        scanf("%d", &arr2[i]);
    }
	
	// qsort(정렬할배열, 요소개수, 요소크기, 비교함수) 
	// stdlib.h에 qsort()라는 함수로 구현
    qsort(arr, n, sizeof(int), compare);

	//이진 탐색 
    for(j = 0; j < m; j++){
        printf("%d\n", binary_search(arr, arr2[j], n));
    }
    return 0;
}
