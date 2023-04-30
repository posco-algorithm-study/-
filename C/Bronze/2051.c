#include <stdio.h>
#include <stdlib.h>

int main(void){

    int n, k, cnt = 1;
    scanf("%d %d", &n, &k);
    int* arr = (int*)malloc(sizeof(int) * n);

    for(int i = 1; i <= n; i++){
        if(n % i == 0){
            arr[cnt] = i;
            cnt++;
        }
    }
    printf("%d\n", arr[k]);

    return 0;
}
