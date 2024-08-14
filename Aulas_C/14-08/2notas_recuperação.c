 #include <stdio.h>

 int main(){
    float N1, N2, R, nmedia, media;
    printf("Entre com a primeira nota:\n");
    scanf("%f", &N1);
    printf("Entre com a segunda nota:\n");
    scanf("%f", &N2);
    media=(N1+N2)/2;
    if (media>=6.0)
    {
        printf("Aprovou! %.2f", media);
        }
    else
        printf("Entre com a nota de recuperação:\n", R);
        scanf("%f", &R);
        nmedia=(media+R)/2;
        if (nmedia>=5.0)
        {
            printf("Aprovou! %.2f", nmedia);
            }
        else
        {
            printf("Reprovou! %.2f", nmedia);
            }
 }