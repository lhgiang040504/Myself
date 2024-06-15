#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Cách sử dụng: %s <command>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    struct timeval start, end;
    pid_t pid;
    int status;

    gettimeofday(&start, NULL); // Lấy thời gian bắt đầu

    pid = fork(); // Tạo tiến trình con

    if (pid == -1) {
        // Không thể tạo tiến trình con
        perror("fork");
        exit(EXIT_FAILURE);
    } else if (pid > 0) {
        // Tiến trình cha
        waitpid(pid, &status, 0); // Đợi tiến trình con kết thúc
        gettimeofday(&end, NULL); // Lấy thời gian kết thúc

        double time_taken;
        time_taken = (end.tv_sec - start.tv_sec) * 1e6;
        time_taken = (time_taken + (end.tv_usec - start.tv_usec)) * 1e-6;

        printf("Thời gian thực thi: %.6f giây\n", time_taken);
    } else {
        // Tiến trình con thực thi lệnh
        execvp(argv[1], &argv[1]);
        // Nếu execvp trả về, có lỗi đã xảy ra
        perror("execvp");
        exit(EXIT_FAILURE);
    }

    return 0;
}