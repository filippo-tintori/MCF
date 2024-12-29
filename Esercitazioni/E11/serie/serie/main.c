#include <stdio.h>
#include <math.h>

double fibonacci(int n){
    if (n <= 1) {
            fprintf(stderr, "Valore non valido: n deve essere maggiore di 0\n");
            return -1;
        }
    if (n == 2)
        return 1.0;
        
    else {
        double fib = 0;
        double n0 = 1;
        double n1 = 1;
        for (int i = 2; i<=n; i++) {
            fib = n0 + n1;
            n0 = n1;
            
            n1 = fib;
        }
        return fib / n0;
    }
    return -1;
}
