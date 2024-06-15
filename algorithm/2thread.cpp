#include <iostream>
#include <thread>
#include <cstdlib>
#include <ctime>

using namespace std;

const int n = 100;
int a[n];

// Hàm đếm số phần tử trong mảng a
int count_elements() {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] != 0) {
            count++;
        }
    }
    return count;
}


// Hàm thread thêm phần tử vào mảng a
void add_element() {
    srand(time(NULL)); 
    int random_num = rand() % 1000;
    a[rand() % n] = random_num;
    cout << "Đã thêm phần tử " << random_num << " vào mảng a." << endl;
    cout << "Số phần tử trong mảng a là: " << count_elements() << endl;
}

// Hàm thread lấy phần tử ra khỏi mảng a
void remove_element() {
    if (count_elements() == 0) {
        cout << "Nothing in array a." << endl;
        return;
    }
    int random_index = rand() % count_elements(); 
    int removed_element = a[random_index];
    for (int i = random_index; i < count_elements() - 1; i++) {
        a[i] = a[i + 1];
    }
    cout << "Đã lấy phần tử " << removed_element << " ra khỏi mảng a." << endl;
    cout << "Số phần tử trong mảng a là: " << count_elements() << endl;
}


int main() {
    // Tạo và chạy hai thread
    thread t1(add_element);
    thread t2(remove_element);
    t1.join();
    t2.join();
    return 0;
}