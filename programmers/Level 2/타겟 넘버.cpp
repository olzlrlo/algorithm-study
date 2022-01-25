#include <string>
#include <vector>

using namespace std;

int answer = 0;

void dfs(vector<int> &v, int target, int sum, int count){
    if(count != v.size()){
        dfs(v, target, sum + v[count], count + 1);
        dfs(v, target, sum - v[count], count + 1);
    }
    else if(target == sum)
        answer++;
}

int solution(vector<int> numbers, int target) {
    dfs(numbers, target, 0, 0);
    return answer;
}
