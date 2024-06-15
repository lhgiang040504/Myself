#include<stdio.h>
#include <stdbool.h>

typedef struct {
    int pid;
    float at, wt, bt, ta, st;
    bool isComplete;
} process;

void sort(process p[], int start, int end) {
    for (int i = start; i < end - 1; i++) {
        for (int j = start; j < end - 1 - i + start; j++) {
            if (p[j].bt > p[j + 1].bt) {
                process temp = p[j];
                p[j] = p[j + 1];
                p[j + 1] = temp;
            }
        }
    }
}

void inputProcesses(int n, process p[]) {
    for (int i = 0; i < n; i++) {
        printf("\nEnter process details: \n");
        printf("Process ID : ");
        scanf("%d", &p[i].pid);
        printf("Arrival Time : ");
        scanf("%f", &p[i].at);
        printf("Burst Time : ");
        scanf("%f", &p[i].bt);
        p[i].isComplete = false;
    }
}

void calculateMetrics(int n, process p[], float *avgwt, float *avgta) {
    float tst = 0.0;
    for (int i = 0; i < n; i++) {
        if (!p[i].isComplete) {
            int k = i;
            while (p[i].at <= tst && i < n)
                i++;
            // Assuming sort function is correctly implemented
            sort(p, i, k);
            i = k;
            if (p[i].at <= tst)
                p[i].st = tst;
            else
                p[i].st = p[i].at;
            p[i].st = tst;
            p[i].isComplete = true;
            tst += p[i].bt;
            p[i].wt = p[i].st - p[i].at;
            p[i].ta = p[i].bt + p[i].wt;
            *avgwt += p[i].wt;
            *avgta += p[i].ta;
        }
    }
    *avgwt /= n;
    *avgta /= n;
}

void printScheduleTable(int n, process p[]) {
    printf("Process Schedule Table: \n");
    printf("\tProcess ID\tArrival Time\tBurst Time\tWait Time\tTurnaround Time\n");
    for (int i = 0; i < n; i++)
        printf("\t%d\t\t%f\t%f\t%f\t%f\n", p[i].pid, p[i].at, p[i].bt, p[i].wt, p[i].ta);
}

int main() {
    int n;
    printf("Enter number of processes : ");
    scanf("%d", &n);
    process p[n];
    inputProcesses(n, p);
    float avgwt = 0.0, avgta = 0.0;
    calculateMetrics(n, p, &avgwt, &avgta);
    printScheduleTable(n, p);
    printf("\nAverage wait time: %f", avgwt);
    printf("\nAverage turnaround time: %f\n ", avgta);
    return 0;
}