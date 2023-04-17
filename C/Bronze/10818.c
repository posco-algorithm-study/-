// 10818
# include <stdio.h>

int arr[1000001];
int main(void){

    int n, max, min;
    scanf("%d", &n);

    for (int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }

    max = arr[0];
    min = arr[0];
    for (int i = 0; i < n; i++){
        if (arr[i] > max){
            max = arr[i];
        }
        if (arr[i] <= min){
            min = arr[i];
        }
    }
    printf("%d %d\n", min, max);

    return 0;
}
