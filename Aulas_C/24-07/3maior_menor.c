#include <stdio.h>

 int main(){
    float N1, N2;
    printf("Entre com o primeiro numero:\n");
    scanf("%f", &N1);
    printf("Entre com o segundo numero:\n");
    scanf("%f", &N2);
    if (N1>N2)
    {
        printf("Maior Numero: %f", N1);
        printf("\nMenor Numero: %f", N2);
        }
    else
    {
        printf("Maior Numero: %f", N2);
        printf("\nMenor Numero: %f", N1);
        }
}