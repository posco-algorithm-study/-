#include <stdio.h>
#include <stdlib.h>

int main(void){

    int n;

    while(1){
        scanf("%d", &n);
        if(n == -1)
            return 0;
        
        int sum = 0, j = 0;
        int* arr = malloc(sizeof(int) * n);

        for(int i = 1; i < n; i++){
            if(n % i == 0){
                sum += i;
                arr[j++] = i;
            }
        }
        if(sum == n){
            printf("%d = ", n);
            for(int i = 0; i < j; i++){
                printf("%d", arr[i]);
                if(i != j - 1)
                    printf(" + ");
            }
            printf("\n");
        }
        else
            printf("%d is NOT perfect.\n", n);
    }

    return 0;
}
