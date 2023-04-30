// 10798번
#include <stdio.h>

int main(void){

    char words[5][15] = { 0 }; // 문자열 배열 선언

    for(int i = 0; i < 5; i++){
        scanf("%s", words[i], sizeof(words));
    }

    for(int j = 0; j < 15; j++){
        for(int i = 0; i < 5; i++){
            if(words[i][j] == NULL)
                continue;
            printf("%c", words[i][j]);
        }
    }

    return 0;
}
