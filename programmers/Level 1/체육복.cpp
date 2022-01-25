#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;

    map<int, int> students; // 학생 별 체육복 수 저장
    for(int i = 1; i <= n; i++)
        students[i] = 1;
    for (int l: lost)
        students[l] -= 1;
    for (int r: reserve)
        students[r] += 1;

    // 앞번호 학생의 체육복 빌리기 -> 뒷번호 학생의 체육복 빌리기
    for (int i = 1; i <= n; i++){
        if(students[i] == 0){
            if (i != 1 && students[i - 1] > 1){
                students[i] += 1;
                students[i - 1] -= 1;
            }
            else if (i != n && students[i + 1] > 1){
                students[i] += 1;
                students[i + 1] -= 1;
            }
        }
    }

    // 체육복 없는 학생의 수
    for (auto a: students){
        if(a.second != 0)
            answer++;
    }
    return answer;
}
