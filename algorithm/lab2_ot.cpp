#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/shm.h>
#include <sys/stat.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/wait.h>

int main(int argc, char* argv[])
{
    if (argc != 2)
    {
        printf("Sai cu phap ./collatz <mot_so_nguyen_duong>\n");
        return 1;
    }
    int n = atoi(argv[1]);
    if(n <= 0)
    {
        printf("Vui long nhap so nguyen duong\n");
        return 1;
    }
    const int SIZE = 4096;
    const char *name = "OS";
    int fd = shm_open(name, O_CREAT | O_RDWR,0666);
    ftruncate(fd, SIZE);
    int *ptr = mmap(0, SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    // Fork tiến trình con
    pid_t pid = fork();

    if (pid < 0) {
        printf("Loi fork\n");
        return 1;
    }
    else if (pid == 0) { // Tiến trình con
        int index = 0;
        while (n != 1) {
            ptr[index++] = n;
            if (n % 2 == 0) {
                n /= 2;
            } else {
                n = 3 * n + 1;
            }
        }
        ptr[index] = 1;
        exit(0);
    } else { // Tiến  trình cha
        wait(NULL);
        printf("Chuoi Collatz: ");
 for (int i = 0; ptr[i] != 0; i++) {
            printf("%d ", ptr[i]);
        }
        printf("\n");
        printf("Hoan thanh!\n");
        munmap(ptr, SIZE);
        close(fd);
    }
 return 0;
}