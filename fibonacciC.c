#include <stdio.h>

int main()
{
    int fib = 0;
    printf("Ingrese el numero de fibonacci ");
    scanf("%d", &fib);

    int num1 = 0;
    int num2 = 1;
    int num3 = 0;

    for(int i=0; i<fib-1; i++)
    {
        num3 = num+num2;
        num = num2;
        num2 = num3;    
    }

    printf("Resultado: %d", num3);
    printf("char = 13th fibonacci para overflow")
    printf("short = 24th fibonacci para overflow")
    printf("Int = 47th fibonacci para overflow")
    printf("long = 47th fibonacci para overflow")
    printf("long long = 93th fibonacci para overflow")
    return 0;
}
