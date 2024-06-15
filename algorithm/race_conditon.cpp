#include <iostream>
#include <thread>
#include <semaphore.h>

using namespace std;

int x = 0;
sem_t mutex;

void processB() {
    while (true) {
        sem_wait(&mutex);
        x = x + 1;
        if (x == 20) {
            x = 0;
            cout << "x = " << x << endl;
        }
        sem_post(&mutex);
    }
}

void processA() {
    while (true) {
        sem_wait(&mutex);
        processB();
        sem_post(&mutex);
    }
}

int main() {
    // Khởi tạo semaphore
    sem_init(&mutex, 0, 1);

    // Tạo và chạy hai thread
    thread t1(processA);
    thread t2(processB);
    t1.join();
    t2.join();

    // Hủy semaphore
    sem_destroy(&mutex);
    return 0;
}