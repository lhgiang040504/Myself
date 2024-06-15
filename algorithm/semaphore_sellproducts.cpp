#include <stdio.h>
#include <stdlib.h>
#include <semaphore.h>
#include <pthread.h>
#include <unistd.h>

const int MSSV = 22520356;
int sells = 0, products = 0;
sem_t sem, sem1;

void *processA(void* mess){
    while (1){
        sem_wait(&sem);
        sells++;
        printf("SELL: %d\n", sells);
        printf("SELL1: %d\n", sells + MSSV);
        sem_post(&sem1);
    }
}

void *processB(void *mess){
    while (1){
        sem_wait(&sem1);
        products++;
        printf("PRODUCT: %d\n", products);
        sem_post(&sem);
    }
}

int main(){
    sem_init(&sem, 0, 0);
    sem_init(&sem1, 0, sells + MSSV);

    pthread_t pA, pB;

    pthread_create(&pA, NULL, &processA, NULL);
    pthread_create(&pB, NULL, &processB, NULL); 

    while (1){
        if (sells > 10000) break;
    }

    return 0;  
}