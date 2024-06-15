#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

pid_t child_pid;

void handleCtrlC(int signum) {
    // Gửi tín hiệu dừng cho tiến trình con
    kill(child_pid, SIGTERM);
    // Đợi tiến trình con kết thúc
    waitpid(child_pid, NULL, 0);
    // In ra dòng chữ: "count.sh has stopped"
    printf("\ncount.sh has stopped\n");
    exit(0);
}

int main() {
    // In ra dòng chữ 
    printf("Welcome to IT007 , I am 22521341 \n");
    signal(SIGINT, handleCtrlC);

    // Tạo tiến trình con 
    child_pid = fork();
    if (child_pid == 0) {
        // Tiến trình con thực thi count.sh với số lần đếm là 120
        // và ghi kết quả vào file count.txt
        execlp("./count.sh", "./count.sh", "120", NULL);
        perror("exec");
        exit(1);
    } else if (child_pid < 0) {
        perror("fork");
        exit(1);
    }

    // Chờ tiến trình con kết thúc
    int status;
    waitpid(child_pid, &status, 0);
    return 0;
}