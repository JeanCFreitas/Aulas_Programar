#include <stdio.h>

int main()
{
    float V, T, D, LU;
    printf("Entre com a velocidade:");
    scanf("%f", &V);
    printf("Entre com o tempo:");
    scanf("%f",&T);
    D=V*T;
    LU=D/12;
    printf("Os valores são: %.2f %.2f %.2f %.2f", T,V,D,LU);
}
