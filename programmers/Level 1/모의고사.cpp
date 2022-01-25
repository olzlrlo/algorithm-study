#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    int ans1 = 0, ans2 = 0, ans3 = 0;

    vector<int> student1 = {1,2,3,4,5};
    vector<int> student2 = {2,1,2,3,2,4,2,5};
    vector<int> student3 = {3,3,1,1,2,2,4,4,5,5};

    for(int i = 0; i < answers.size(); i++){
        if(student1[i%5] == answers[i]) ans1++;
        if(student2[i%8] == answers[i]) ans2++;
        if(student3[i%10] == answers[i]) ans3++;
    }

    int max_ans = max(max(ans1, ans2), ans3);
    if (max_ans == ans1)
        answer.push_back(1);
    if (max_ans == ans2)
        answer.push_back(2);
    if (max_ans == ans3)
        answer.push_back(3);

    return answer;
}
