#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int n = (brown - 4) / 2; // 꼭짓점 제외, 가로와 세로만 고려
    for(int i = 1; i < n; i++){
        int j = n - i;
        int m = i * j;
        if (m == yellow){
            answer.push_back(j + 2);
            answer.push_back(i + 2);
            break;
        }
    }
    return answer;
}
