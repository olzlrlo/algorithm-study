#include <string>
#include <vector>
#include <cmath>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> days;

    for (int i = 0; i < progresses.size(); i++){
        double day = double(100 - progresses[i]) / double(speeds[i]);
        day = ceil(day);
        days.push_back(day);
    }

    int now = 0;
    int deploy = 1;
    for (auto day: days){
        if (day > now){
            answer.push_back(deploy);
            now = day;
            deploy = 1;
        }
        else
            deploy++;
    }
    answer.push_back(deploy);
    answer.erase(answer.begin());

    return answer;
}
