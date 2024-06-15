#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>
#define SORT_BY_ARRIVAL 0
#define SORT_BY_PID 1
#define SORT_BY_BURST 2
#define SORT_BY_START 3
#define SORT_BY_REMANING 4
typedef struct
{
int iPID;
int iArrival, iBurst, iRemaning;
int iStart, iFinish, iWaiting, iResponse, iTaT;
} PCB;
void inputProcess(int n, PCB P[]);
void printProcess(int n, PCB P[]);
void pushProcess(int *n, PCB P[], PCB Q);
void removeProcess(int *n, int index, PCB P[]);
void swapProcess(PCB *P, PCB *Q);
int partition(PCB P[], int low, int high, int iCriteria);
void quickSort(PCB P[], int low, int high, int iCriteria);
void calculateTaT(int n, PCB P[]);
int findJ(int i, int A[]);
void exportGanttChart(int n, int A[]);
void printInfor(int iTerminated,PCB TerminatedArray[]);
int main()
{
PCB Input[10];
PCB ReadyQueue[10];
PCB TerminatedArray[10];
int GanttChart[100];
int iNumberOfProcess;
printf("Please input number of Process: ");
scanf("%d", &iNumberOfProcess);
// Khởi tạo giá trị cho Remain, Ready và iTerminated
int iRemain = iNumberOfProcess, iReady = 0, iTerminated = 0;
inputProcess(iNumberOfProcess, Input);
quickSort(Input, 0, iNumberOfProcess - 1, SORT_BY_ARRIVAL);
int t = 0;
while (iTerminated < iNumberOfProcess)
{
while (iRemain > 0)
{
if (Input[0].iArrival <= t)
{
pushProcess(&iReady, ReadyQueue, Input[0]);
removeProcess(&iRemain, 0, Input);
continue;
}
else
break;
}
if (iReady > 0)
{
quickSort(ReadyQueue, 0, iReady - 1, SORT_BY_REMANING);
GanttChart[t] = ReadyQueue[0].iPID;
t++;
ReadyQueue[0].iRemaning--;
ReadyQueue[0].iFinish = t;
ReadyQueue[0].iWaiting = ReadyQueue[0].iFinish -
ReadyQueue[0].iBurst - ReadyQueue[0].iArrival;
if (ReadyQueue[0].iRemaning == 0)
{
pushProcess(&iTerminated, TerminatedArray, ReadyQueue[0]);
removeProcess(&iReady, 0, ReadyQueue);
}
}
else
{
GanttChart[t] = 0;
t++;
}
}
printInfor(iTerminated,TerminatedArray);
exportGanttChart(t, GanttChart);
}
void printInfor(int iTerminated,PCB TerminatedArray[])
{
printf("\n");
calculateTaT(iTerminated, TerminatedArray);
printf(" P\t\t"
"iArrival\t"
"iBurst\t\t"
"iWaiting\t"
"iTAT\t\t\n");
quickSort(TerminatedArray, 0, iTerminated - 1, SORT_BY_PID);
// Calculate total waiting time and total turnaround time
int total_wt = 0, total_tat = 0;
for (int i = 0; i < iTerminated; i++)
{
total_wt = total_wt + TerminatedArray[i].iWaiting;
total_tat = total_tat + TerminatedArray[i].iTaT;
printf(" %d\t\t"
"%d\t\t %d\t\t %d\t\t %d\n",
TerminatedArray[i].iPID, TerminatedArray[i].iArrival,
TerminatedArray[i].iBurst, TerminatedArray[i].iWaiting,
TerminatedArray[i].iTaT);
}
printf("\nAverage waiting time = %.2f", (float)total_wt /
(float)iTerminated);
printf("\nAverage turn around time = %.2f", (float)total_tat /
(float)iTerminated);
printf("\n");
}
void exportGanttChart(int n, int A[])
{
printf("Gantt Chart:\n");
for (int i = 0; i < n;)
{
if (A[i] == 0)
{
printf(" ");
i++;
continue;
}
int start = i;
while (i < n && A[i] == A[start])
{
i++;
}
printf("P%d|%d", A[start], start);
for(int j = start; j < i; j++)
{
printf("-");
}
printf("%d| ", i);
}
printf("\n");
}
void calculateTaT(int n, PCB P[])
{
for (int i = 0; i < n; i++)
P[i].iTaT = P[i].iBurst + P[i].iWaiting;
}
void inputProcess(int n, PCB P[])
{
srand((unsigned int)time(NULL));
for (int i = 0; i < n; i++)
{
P[i].iArrival = 0 + (int)( rand() * (20 - 0 + 1.0) / (1.0 +
RAND_MAX) );
P[i].iBurst = 2 + (int)( rand() * (12 - 2 + 1.0) / (1.0 + RAND_MAX)
);
P[i].iPID = i + 1; // Gán PID tăng dần từ 1
P[i].iRemaning = P[i].iBurst;
}
}
void pushProcess(int *n, PCB P[], PCB Q)
{
if (*n < 10)
{
P[*n] = Q;
(*n)++;
}
else
printf("Hang doi da day!\n");
}
void removeProcess(int *n, int index, PCB P[])
{
for (int i = index; i < *n - 1; i++)
{
P[i] = P[i + 1];
}
(*n)--;
}
int partition(PCB P[], int low, int high, int iCriteria)
{
int pivot;
// Sắp xếp theo Arrival Time
if (iCriteria == 0)
{
pivot = P[high].iArrival;
int i = low - 1;
for (int j = low; j < high; j++)
{
if (P[j].iArrival <= pivot)
{
i++;
swapProcess(&P[i], &P[j]);
}
}
i++;
swapProcess(&P[i], &P[high]);
return i;
}
// Sắp xếp theo PID
else if (iCriteria == 1)
{
pivot = P[high].iPID;
int i = low - 1;
for (int j = low; j < high; j++)
{
if (P[j].iPID <= pivot)
{
i++;
swapProcess(&P[i], &P[j]);
}
}
i++;
swapProcess(&P[i], &P[high]);
return i;
}
// Sắp xếp theo Burst Time
else if (iCriteria == 2)
{
pivot = P[high].iBurst;
int i = low - 1;
for (int j = low; j < high; j++)
{
if (P[j].iBurst <= pivot)
{
i++;
swapProcess(&P[i], &P[j]);
}
}
i++;
swapProcess(&P[i], &P[high]);
return i;
}
// Sắp xếp theo Remaning Time
else if (iCriteria == 4)
{
pivot = P[high].iRemaning;
int i = low - 1;
for (int j = low; j < high; j++)
{
if (P[j].iRemaning <= pivot)
{
i++;
swapProcess(&P[i], &P[j]);
}
}
i++;
swapProcess(&P[i], &P[high]);
return i;
}
// Sắp xếp theo Start Time
else if (iCriteria == 3)
{
pivot = P[high].iStart;
int i = low - 1;
for (int j = low; j < high; j++)
{
if (P[j].iStart <= pivot)
{
i++;
swapProcess(&P[i], &P[j]);
}
}
i++;
swapProcess(&P[i], &P[high]);
return i;
}
}
void quickSort(PCB P[], int low, int high, int iCriteria)
{
if (low < high)
{
int q = partition(P, low, high, iCriteria);
quickSort(P, low, q - 1, iCriteria);
quickSort(P, q + 1, high, iCriteria);
}
else
return;
}
void swapProcess(PCB *P, PCB *Q)
{
PCB temp = *P;
*P = *Q;
*Q = temp;
}
