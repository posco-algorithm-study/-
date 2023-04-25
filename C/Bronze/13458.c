#include <stdio.h>

int main(void){

    int n, b, c;
    long long int result = 0;
    scanf("%d", &n);
    long long int arr[n];

    for(int i = 0; i < n; i++){
        scanf("%lld", &arr[i]);
    }
    scanf("%d %d", &b, &c);

    for(int i = 0; i < n; i++){
        if(arr[i] >= b)
            result++;
        else{
            result++;
            continue;
        }
        int tmp = arr[i] - b;
        result += tmp / c;
        if(tmp % c > 0)
            result++;
    }
    printf("%lld", result);

    return 0;
}
