# include <stdio.h>

int main(void){

    int a, b[3];
    int i = 0;
    scanf("%d", &a);
    scanf("%1d%1d%1d", &b[0], &b[1], &b[2]);
    
    int num2;
    num2  = 100*b[0] + 10*b[1] + b[2];

    printf("%d\n", a * b[2]);
    printf("%d\n", a * b[1]);
    printf("%d\n", a * b[0]);
    printf("%d\n", a * num2);

    return 0;
}
