// 특이한 풀이법 공유 목적.
/*메달 총개수가 100만개 이므로 금은동 매달 
1개마다의 점수 차이의 적정선을 찾는다.
금메달 1개는 은메달 99만9999개를 땄을 때
금메달의 점수가 은메달의 점수보다 100만배 이상
차이가 나도록 한다.
동메달 : 1점/ 은메달 : 10^6점 / 금메달 : 10^12점
으로 메달별 점수를 디폴트.
*/

#include <stdio.h>

long long a[1001]; 
int main() {
    int N, K;
    scanf("%d%d", &N, &K);
    for (int i = 1; i<=N; ++i) {
        int n, g, s, b;
        scanf("%d%d%d%d", &n, &g, &s, &b);
        a[n] = g* 1e12 + s* 1e6 + b;
    }
    int ans = 1;
    for (int i = 1; i <=N; ++i) {
        if (a[i] > a[K]) ++ans;
    }
    printf("%d", ans);
    return 0;
}




## -- Another Solution -- ##



information=input()
real_information=information.split(' ')
intreal_information=list(map(int,real_information))

#국가의 수
countries=intreal_information[0]

#구하고자 하는 국가의 등수
rank=intreal_information[1]

#나라 정보 입력받는 함수
def inputcountry():
    infor=input()
    realinfor=infor.split(' ')
    intinfor=list(map(int,realinfor))
    return intinfor

#리스트에 나라 정보 저장 (이중 리스트 이용)
c=[]
for i in range(countries):
    c.append(inputcountry())

#금은동 순 내림차순 정렬
c.sort(key=lambda x: (x[1],x[2],x[3]), reverse=True)

#등수를 찾아, index 변수에 저장
for i in range(countries):
    if c[i][0]==rank:
        index=i

#등수가 같은 나라(=공동순위까지 모두 적용) => i+1시켜 출력 (i가 0부터 시작해서)
for i in range(countries):
    if c[index][1:] == c[i][1:]:
        print(i+1)
        break
